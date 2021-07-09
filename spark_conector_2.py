from pyspark import SparkConf
from pyspark.sql import SQLContext, SparkSession

conf = SparkConf().set("spark.jars", "./spark-cassandra-connector_2.12-3.0.1.jar")

spark = SparkSession.builder \
    .appName('SparkCassandraApp') \
    .config('spark.cassandra.connection.host', 'localhost') \
    .config('spark.cassandra.connection.port', '9042') \
    .master('local[2]') \
    .getOrCreate()

sqlContext = SQLContext(spark.sparkContext)

table1 = sqlContext.read.format("org.apache.spark.sql.cassandra").options(table="terminal_monitoring",
                                                                          keyspace="polaris_cloud_monitoreo").load()

table1.show()
