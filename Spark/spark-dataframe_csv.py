from pyspark.python.pyspark.shell import sc
from pyspark.shell import spark
from pyspark.sql import SQLContext

df = spark.read.options(header='True', inferSchema='True').csv('../data/*.csv')
# Number of rows
count_rows = df.count()
# Name of columns
df.printSchema()
# Unique values for field event_type
df.select('event_type').distinct().show()
# Unique values for field brand
df.select('brand').distinct().show()
# Id products in the cart
df.select('product_id').filter("event_type ='cart'").show()
# First id_producto in the cart
df.select('product_id').filter("event_type ='cart'").first()
# Sesiones donde el producto se ha agregado a cart
sessions = df.select(['user_session']).filter("event_type ='cart'  AND product_id=5844305")
# Listado de productos que se han vendido conjuntamente con el producto 5844305
products = df.select(['product_id']).filter("event_type ='cart'  AND product_id<>5844305").filter(
    df['user_session'].isin(sessions['user_session']))
# Conteo de productos de la linea anterior
products.select("product_id").count()
# Dejar solo los productos distintos
products = products.select("product_id").distinct()
products.select("product_id").count()
# Exportar datos de productos
products.write.mode("overwrite").csv('products')
# Leer carpeta exportada
products_import = spark.read.options(header='True', inferSchema='True').csv('./products/*.csv')
# Trabajar con dataframe sql
df.createOrReplaceTempView("data")
spark.sql("select * from data limit 3").show()
spark.sql("select * from data where event_type='cart' limit 3").show()
spark.sql("select count(*) from data where event_type='cart'").show()
"""sqlContext = SQLContext(sc)
df = sqlContext.read.format('com.databricks.spark.csv') \
    .options(header='true', inferschema='true') \
    .load('../data/2019-Dec.csv')"""

