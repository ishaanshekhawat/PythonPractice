# https://code.datavidhya.com/coding-problems/questionDetails/question/social-media-pii

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(input_df):
    df = input_df.withColumn('phone', F.concat(F.lit('******'), F.substring('phone', 7, 10))).withColumn('email', F.split('email', '@')[1])
    df = df.withColumnRenamed('phone', 'anon_phone').withColumnRenamed('email', 'email_domain')
    return df.select(['anon_phone', 'email_domain', 	'user_id']).orderBy('anon_phone', ascending=True)
