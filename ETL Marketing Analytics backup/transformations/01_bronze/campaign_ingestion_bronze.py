from pyspark import pipelines as dp
from pyspark.sql.functions import *

VOL_LOCATION = spark.conf.get('camp_loc')

SCHEMA = '''
       campaign_id string,
       campaign_name STRING,
       channel STRING,
       start_date long,
       budget_usd double
'''

@dp.table(
    name = 'campaign'
)
def campaign():
    df = (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("header", "true")
        .schema(SCHEMA)
        .load(VOL_LOCATION)
    )

    return df.drop('_rescued_data')