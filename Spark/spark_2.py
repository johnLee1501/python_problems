import sys
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

df = spark.read.options(header='True', inferSchema='True').csv(
    "../data/*.csv")
df.count()
df.printSchema()

df.select("brand").distinct().show()


def myFunc(s):
    if s["brand"] == "riche" and s["event_type"] == "cart":
        return [(s["product_id"], 1)]
    return []


lines = df.rdd.flatMap(myFunc).reduceByKey(lambda a, b: a + b)

for element in lines.collect():
    print(element)

print(lines.take(20))
print(lines.take(20))
for el in lines.take(20):
    print(el)
lines.toDF().show()

lines.saveAsTextFile("spark2")
