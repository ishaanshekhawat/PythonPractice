# https://code.datavidhya.com/coding-problems/questionDetails/question/monthly-ratings

from pyspark.sql import SparkSession
from pyspark.sql.functions import month, avg, col

def etl(input_df):
    df = input_df.groupBy(['product_id', 'month']).agg(F.avg('stars').alias('avg_stars')).withColumnRenamed('month','mth').withColumnRenamed('product_id','product').select('mth', 'product', 'avg_stars').orderBy(['mth', 'product'])
    return df
