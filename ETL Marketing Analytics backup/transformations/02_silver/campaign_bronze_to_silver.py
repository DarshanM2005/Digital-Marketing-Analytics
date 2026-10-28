from pyspark import pipelines as dp
from pyspark.sql.functions import *

# Create the target streaming table in the silver schema
dp.create_streaming_table(
    name="02_silver.dim_campaign",
    
)

# Apply CDC flow from bronze campaign to silver dim_campaign (SCD Type 1)
dp.create_auto_cdc_flow(
    target="02_silver.dim_campaign",
    source="marketing_analytics_project.`01_bronze`.campaign",
    keys=["campaign_id"],
    sequence_by="start_date",
    stored_as_scd_type=1
)