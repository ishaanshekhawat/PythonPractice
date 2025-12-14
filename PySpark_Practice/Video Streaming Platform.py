# https://code.datavidhya.com/coding-problems/questionDetails/question/video-streaming-platform

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
from datetime import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(video_stream_df):
    curr_year = datetime.now().year
    video_stream_df = video_stream_df[(video_stream_df['view_count'] > 1000000) & (video_stream_df['release_year'] >= curr_year - 6)].select(['duration', 'genre', 'release_year', 'title', 'video_id', 'view_count']).orderBy('duration', ascending=True)
    return video_stream_df
