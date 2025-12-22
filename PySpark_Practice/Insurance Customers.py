# https://code.datavidhya.com/coding-problems/questionDetails/question/insurance-customers

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(ic_data_1, ic_data_2):
    df = ic_data_1.union(ic_data_2)
    df = df.select('age', 'customer_id', 'first_name', 'last_name', 'policy_type').orderBy('age')
    return df
