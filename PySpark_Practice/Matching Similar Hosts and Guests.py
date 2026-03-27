# https://platform.stratascratch.com/coding/10078-find-matching-hosts-and-guests-in-a-way-that-they-are-both-of-the-same-gender-and-nationality?code_type=6

# Import your libraries
import pyspark

# Start writing code
df = airbnb_hosts.crossJoin(airbnb_guests) \
    .filter((airbnb_hosts["nationality"] == airbnb_guests["nationality"]) & 
            (airbnb_hosts["gender"] == airbnb_guests["gender"])) \
    .select("host_id", "guest_id") \
    .distinct()

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
