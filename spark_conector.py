from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession
import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.0.1 --conf spark.cassandra.connection.host=127.0.0.1 pyspark-shell'
spark = SparkSession.builder \
    .appName('SparkCassandraApp') \
    .config('spark.cassandra.connection.host', 'localhost') \
    .config('spark.cassandra.connection.port', '9042') \
    .master('local[2]') \
    .getOrCreate()
conf = SparkConf()
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
table1 = sqlContext.read.format("org.apache.spark.sql.cassandra").options(table="terminal_monitoring",
                                                                          keyspace="polaris_cloud_monitoreo").load()
table1.show()