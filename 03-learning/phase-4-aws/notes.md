# Phase 4: AWS Data Services - Learning Notes

**Duration:** Weeks 13-16 (Month 4)
**Status:** Not Started

---

## Key Concepts

### AWS Core Services
- S3 (data lake storage)
- AWS Glue (ETL service)
- Amazon Athena (serverless queries)
- AWS Lambda (serverless compute)
- Amazon RDS (relational databases)
- Amazon Redshift (data warehouse)

### Data Lake Architecture
- S3 data lake patterns
- Data partitioning strategies
- Lifecycle policies
- Storage classes and optimization

### ETL with AWS Glue
- Glue Data Catalog
- Glue crawlers
- Glue jobs (PySpark)
- Glue workflows
- Job bookmarks for incremental processing

### Serverless Patterns
- Lambda functions for data processing
- EventBridge for orchestration
- Step Functions for workflows
- S3 event notifications

### Security and Governance
- IAM roles and policies
- Data encryption (at rest and in transit)
- VPC and networking
- AWS Lake Formation

---

## Code Patterns

### AWS Glue Job Pattern
```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Glue Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = "my_database",
    table_name = "my_table"
)

# Transform data
transformed = datasource.apply_mapping([
    ("old_field", "string", "new_field", "string"),
    ("amount", "double", "amount", "double")
])

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame = transformed,
    connection_type = "s3",
    connection_options = {"path": "s3://bucket/output/"},
    format = "parquet"
)

job.commit()
```

### Lambda Data Processing Pattern
```python
import json
import boto3
import pandas as pd
from io import StringIO

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get S3 object from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Read data
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))

    # Process data
    df_processed = df.dropna()

    # Write back to S3
    csv_buffer = StringIO()
    df_processed.to_csv(csv_buffer, index=False)
    s3_client.put_object(
        Bucket=bucket,
        Key=f"processed/{key}",
        Body=csv_buffer.getvalue()
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }
```

### Athena Query Pattern
```sql
-- Create external table in Athena
CREATE EXTERNAL TABLE IF NOT EXISTS my_table (
    id INT,
    name STRING,
    amount DOUBLE,
    date DATE
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET
LOCATION 's3://my-bucket/data/';

-- Add partitions
MSCK REPAIR TABLE my_table;

-- Query with partition pruning
SELECT
    name,
    SUM(amount) as total_amount
FROM my_table
WHERE year = 2024 AND month = 1
GROUP BY name;
```

### Infrastructure as Code (CloudFormation)
```yaml
Resources:
  DataLakeBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub 'data-lake-${AWS::AccountId}'
      VersioningConfiguration:
        Status: Enabled
      LifecycleConfiguration:
        Rules:
          - Id: MoveToIA
            Status: Enabled
            Transitions:
              - StorageClass: INTELLIGENT_TIERING
                TransitionInDays: 30

  GlueDatabase:
    Type: AWS::Glue::Database
    Properties:
      CatalogId: !Ref AWS::AccountId
      DatabaseInput:
        Name: my_data_catalog
        Description: Data catalog for analytics
```

---

## Resources Used

### Primary Resources
- AWS documentation (Glue, Athena, S3)
- AWS training and certification
- Progress: 0%

### Supplementary Resources
- AWS Glue documentation: https://docs.aws.amazon.com/glue/
- AWS Lambda documentation: https://docs.aws.amazon.com/lambda/
- Amazon Athena guide: https://docs.aws.amazon.com/athena/
- AWS Architecture Center: https://aws.amazon.com/architecture/

### Learning Paths
- AWS Data Engineering learning path
- AWS Solutions Architect concepts
- Serverless on AWS

---

## Personal Notes

### Week 13
[Add your notes about what you learned]

### Week 14
[Add your notes about what you learned]

### Week 15
[Add your notes about what you learned]

### Week 16
[Add your notes about what you learned]

---

## Key Takeaways

[Add your main learnings from this phase]

---

## Questions / Areas for Review

[Note any concepts that need more practice or clarification]

---

## Practical Applications

[Note how these concepts apply to data engineering work]

---

## Cost Optimization Notes

[Document strategies to minimize AWS costs while learning]

---

## Security Best Practices

[Document security patterns and IAM configurations]
