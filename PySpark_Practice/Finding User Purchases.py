# https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=6

# Import your libraries
import pyspark
from pyspark.sql.window import Window
import pyspark.sql.functions as F

windowSpec = Window.partitionBy("user_id").orderBy("created_at")

# Start writing code
df = amazon_transactions.withColumn("rnk", F.row_number().over(windowSpec)) \
    .filter(F.col("rnk") <= 2)

df = df.withColumn("next_created_at", F.lead("created_at", 1).over(windowSpec))

df = df.withColumn("diff", F.datediff(F.col("next_created_at"), F.col("created_at"))) \
    .filter(F.col("diff").isNotNull() & (F.col("diff") <= 7) & (F.col("diff") != 0)) \
    .select("user_id")

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
