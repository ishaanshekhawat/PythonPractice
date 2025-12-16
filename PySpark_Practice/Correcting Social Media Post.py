# https://code.datavidhya.com/coding-problems/questionDetails/question/correct-social-media-post

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(social_media):
    df = social_media.withColumn('text', F.regexp_replace('text', 'Python', 'PySpark')).select('comments', 'date', 'id', 'likes', 'platform', 'shares', 'text').orderBy('comments', ascending = True)
    return df
