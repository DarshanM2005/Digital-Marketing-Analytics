from pyspark import pipelines as dp
from pyspark.sql.functions import *

VOL_LOCATION = spark.conf.get('ad_perf_loc')

SCHEMA = '''
       campaign_id string,
       date DATE,
       impressions long,
       clicks long,
       spend_usd double,
       device string
'''

@dp.table(
    name = 'ad_performance'
)
def ad_performace():
    df = (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(SCHEMA)
        .load(VOL_LOCATION)
    )

    return df.drop('_rescued_data')