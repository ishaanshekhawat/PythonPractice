# https://code.datavidhya.com/coding-problems/questionDetails/question/crm-saas-platform

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(customers, orders, products):
    df1 = customers.join(orders, on='customer_id')
    df2 = df1.join(products, on='product_id')
    df2 = df2.withColumn('customer_name', F.concat(df2['first_name'], F.lit(' '), df2['last_name']))
    df2 = df2.withColumnRenamed('email', 'customer_email').withColumnRenamed('category', 'product_category')
    df2 = df2.select(['order_id', 'customer_name', 'customer_email', 'product_name', 'product_category', 'order_date'])
    return df2
