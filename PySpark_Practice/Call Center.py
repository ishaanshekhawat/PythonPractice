# https://code.datavidhya.com/coding-problems/questionDetails/question/call-center

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(calls_df, customers_df):
    df = calls_df.groupBy('date').agg(F.countDistinct('cust_id').alias('num_customers'), F.sum('duration').alias('total_duration'))
    df = df.select('date', 'num_customers', 'total_duration')
    return df.orderBy('date')
