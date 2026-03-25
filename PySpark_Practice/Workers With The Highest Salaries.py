# https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries

# Import your libraries
import pyspark
from pyspark.sql.window import Window
import pyspark.sql.functions as F

windowSpec = Window.orderBy(F.desc("salary"))

# Start writing code
df = worker.join(title, worker.worker_id == title.worker_ref_id).withColumn("rnk", F.rank().over(windowSpec)).filter(F.col("rnk") == 1).select("worker_title").alias("best_paid_title")

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
