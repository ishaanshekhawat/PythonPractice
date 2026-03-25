# https://platform.stratascratch.com/coding/2131-user-streaks?code_type=6

# Import your libraries
import pyspark
from pyspark.sql.window import Window
import pyspark.sql.functions as F

windowSpec1 = Window.partitionBy("user_id").orderBy("date_visited")
windowSpec2 = Window.orderBy(F.desc("dq"))

# Start writing code
df = user_streaks.filter(F.col("date_visited") <= "2022-08-10") \
    .distinct() \
    .withColumn("rnk1", F.rank().over(windowSpec1)) \
    .withColumn("diff", F.expr("date_sub(date_visited, rnk1)")) \
    .groupBy("user_id", "diff") \
    .agg(F.count("diff").alias("ct")) \
    .groupBy("user_id") \
    .agg(F.max("ct").alias("dq")) \
    .withColumn("rnk2", F.dense_rank().over(windowSpec2)) \
    .filter(F.col("rnk2") <= 3) \
    .select("user_id", "dq")
    

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
