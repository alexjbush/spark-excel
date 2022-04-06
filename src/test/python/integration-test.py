from pyspark import SparkSession
import sys

if __name__ == '__main__':
    spark = SparkSession.builder.appName('integration-test').master("local").getOrCreate()
    spark.read \
        .format("excel") \
        .option("dataAddress", "'Coefficient Table'!A6") \
        .option("ignoreAfterHeader", "2") \
        .option("inferSchema", "true") \
        .load(sys.argv[1]) \
        .show()