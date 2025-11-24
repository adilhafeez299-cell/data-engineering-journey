# Phase 3: Databricks & Spark - Learning Notes

**Duration:** Weeks 9-12 (Month 3)
**Status:** Not Started

---

## Key Concepts

### Apache Spark Fundamentals
- Distributed computing concepts
- RDDs, DataFrames, Datasets
- Transformations vs. actions
- Lazy evaluation
- Spark execution model

### PySpark Programming
- DataFrame API
- SQL in Spark
- Data transformations
- Aggregations and joins
- User-defined functions (UDFs)

### Databricks Platform
- Workspace and notebooks
- Clusters and compute
- Databricks File System (DBFS)
- Jobs and workflows
- Databricks SQL

### Delta Lake
- ACID transactions
- Time travel
- Schema evolution
- Merge operations
- Optimization techniques

### ETL Patterns
- Medallion architecture (bronze/silver/gold)
- Incremental processing
- Change data capture (CDC)
- Streaming vs. batch processing

---

## Code Patterns

### Reading and Writing Data
```python
# Reading data
df = spark.read.format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    .load("/path/to/data.csv")

# Writing to Delta Lake
df.write.format("delta")
    .mode("overwrite")
    .save("/path/to/delta/table")
```

### PySpark Transformations
```python
from pyspark.sql import functions as F

# Data transformation example
cleaned_df = (df
    .filter(F.col("value").isNotNull())
    .withColumn("processed_date", F.current_date())
    .withColumn("value_upper", F.upper(F.col("value")))
    .groupBy("category")
    .agg(
        F.count("*").alias("count"),
        F.avg("amount").alias("avg_amount")
    )
)
```

### Delta Lake Merge Pattern
```python
from delta.tables import DeltaTable

delta_table = DeltaTable.forPath(spark, "/path/to/delta/table")

delta_table.alias("target").merge(
    source_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()
```

### Medallion Architecture Pattern
```python
# Bronze layer - raw data ingestion
bronze_df = spark.read.format("json").load("/raw/data")
bronze_df.write.format("delta").mode("append").save("/bronze/table")

# Silver layer - cleaned and conformed
silver_df = (spark.read.format("delta").load("/bronze/table")
    .filter(F.col("value").isNotNull())
    .dropDuplicates()
)
silver_df.write.format("delta").mode("append").save("/silver/table")

# Gold layer - business-level aggregates
gold_df = (spark.read.format("delta").load("/silver/table")
    .groupBy("category", "date")
    .agg(F.sum("amount").alias("total_amount"))
)
gold_df.write.format("delta").mode("overwrite").save("/gold/table")
```

---

## Resources Used

### Primary Resources
- Databricks Academy (free courses)
- Databricks documentation
- Progress: 0%

### Supplementary Resources
- Apache Spark documentation: https://spark.apache.org/docs/
- Databricks Community Edition: https://community.cloud.databricks.com/
- Delta Lake documentation: https://docs.delta.io/
- PySpark API reference: https://spark.apache.org/docs/latest/api/python/

### Learning Paths
- Databricks Fundamentals
- Apache Spark Programming with Databricks
- Data Engineering with Databricks

---

## Personal Notes

### Week 9
[Add your notes about what you learned]

### Week 10
[Add your notes about what you learned]

### Week 11
[Add your notes about what you learned]

### Week 12
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

## Performance Tips

[Document optimization strategies you learn]