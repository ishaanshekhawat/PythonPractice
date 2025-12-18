# https://code.datavidhya.com/coding-problems/questionDetails/question/ai-research

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(authors, research_papers):
    df = authors.join(research_papers, on='paper_id')
    df.createOrReplaceTempView("table1")
    result = spark.sql("""
        SELECT author_id, name, paper_id,
               row_number() OVER (PARTITION BY paper_id ORDER BY paper_id) AS row_number
        FROM table1
    """)
    return result
