# PROJECT LIBRARY
## Authoritative List of 6 Portfolio Projects

**Status:** Version 1.0 - November 18, 2025  
**Note:** All projects are **working, deployed portfolio pieces**. No theoretical projects. All must be on GitHub with comprehensive READMEs.

---

## PROJECT 1: Python Automation Tool
**Phase:** 1 - Python Foundations (Nov-Dec 2025)  
**Status:** In Progress (Week 2)

### Overview
Practical Python tool solving a real problem, demonstrating fundamentals.

### Options (Choose ONE):
1. **File Organizer** - Read directory, organize files by type/date into folders
2. **CSV Analyzer** - Load CSV, calculate statistics (mean, median, std dev), identify outliers
3. **Log File Parser** - Parse server logs, extract patterns, generate summary report

### Requirements
- [ ] Command-line interface (argparse or simple sys.argv)
- [ ] File I/O operations (read and/or write)
- [ ] Data structures (lists, dicts, sets)
- [ ] Error handling (try/except blocks)
- [ ] Functions with clear purposes
- [ ] At least one loop

### Deliverables
- [ ] Python script(s) working without errors
- [ ] Comprehensive README with:
  - What problem it solves
  - How to install/run
  - Example usage
  - Sample output
- [ ] .gitignore file
- [ ] Committed to GitHub
- [ ] At least 3 commits showing progress

### GitHub Repo Structure
```
project1-[name]/
├── main.py
├── README.md
├── .gitignore
├── sample_data/ (sample input files)
└── requirements.txt (if external libraries used)
```

### Success Criteria
- ✅ Works without errors on test data
- ✅ README is clear enough for someone else to use it
- ✅ Demonstrates Python fundamentals (functions, loops, error handling)
- ✅ Code is readable and commented

### Estimated Time
8-10 hours total across Weeks 3-4

---

## PROJECT 2: Financial Dataset Analysis
**Phase:** 2 - SQL & Data Analysis (Dec 2025 - Jan 2026)  
**Status:** Not Started

### Overview
Analyze real financial data using SQL + Python, demonstrating data analysis capability.

### Data Source
Choose ONE:
- Kaggle dataset (stocks, transactions, customer data, company financials)
- Public financial API
- Sample data you create

### Requirements
- [ ] Load data into PostgreSQL or SQLite database
- [ ] Write 20+ analytical SQL queries including:
  - Basic queries (SELECT, WHERE, ORDER BY)
  - Joins (multiple tables)
  - Aggregations (GROUP BY, HAVING)
  - Window functions (RANK, ROW_NUMBER, LAG/LEAD, NTILE)
  - CTEs (Common Table Expressions WITH clause)
  - Subqueries
- [ ] Create simple visualizations (matplotlib or seaborn)
- [ ] Document findings and insights

### Deliverables
- [ ] Database schema (SQL CREATE TABLE statements)
- [ ] 20+ SQL queries in separate files or one organized notebook
- [ ] 3-5 visualizations (charts, graphs)
- [ ] README documenting:
  - Dataset source and description
  - Questions asked and answers found
  - Key insights and patterns
  - How to reproduce the analysis
- [ ] Jupyter notebook showing analysis flow (optional but good)
- [ ] Committed to GitHub

### GitHub Repo Structure
```
project2-financial-analysis/
├── data/
│   └── sample_data.csv
├── sql/
│   ├── schema.sql
│   ├── queries.sql (or numbered files)
│   └── views.sql
├── analysis.ipynb (optional)
├── visualizations/
│   ├── chart1.png
│   ├── chart2.png
│   └── ...
├── README.md
└── .gitignore
```

### Success Criteria
- ✅ SQL queries are correct and efficient
- ✅ Visualizations clearly show insights
- ✅ README explains the analysis well
- ✅ Someone could reproduce your analysis from the files

### Estimated Time
10-12 hours total across Weeks 5-8

---

## PROJECT 3: AWS Data Pipeline
**Phase:** 3 - AWS & Cloud (Mar–May 2026)  
**Status:** Not Started

### Overview
Cloud-based ETL pipeline demonstrating AWS services and data engineering patterns.

### Architecture
```
Data Source (CSV/API/RDS)
    ↓
AWS S3 (Raw data storage)
    ↓
Lambda / Glue (Transformation)
    ↓
Redshift / RDS (Data warehouse)
    ↓
Analytics / Reporting
```

### Requirements
- [ ] **Data Ingestion:**
  - Data uploaded to S3 (raw zone)
  - Automated trigger (S3 event or scheduled)
  - Error handling for bad files

- [ ] **Transformation:**
  - Lambda function or Glue job
  - Clean, validate, enrich data
  - Handle nulls, duplicates, type conversions
  - Store intermediate results (processed zone)

- [ ] **Loading:**
  - Load to Redshift (if using data warehouse)
  - Or RDS (if using relational database)
  - Or keep in S3 with Athena queries

- [ ] **Orchestration:**
  - EventBridge or Step Functions
  - Schedule pipeline (daily/hourly)
  - Dependency management
  - Error handling and retries

- [ ] **Monitoring & Alerts:**
  - CloudWatch logs
  - SNS notifications on failure
  - Basic metrics (records processed, execution time)

### Data Source
Choose ONE:
- CSV files (upload to S3)
- Public API (invoke from Lambda)
- RDS database (read from)

### Deliverables
- [ ] Working Lambda function(s) or Glue job
- [ ] CloudFormation or Terraform template
- [ ] S3 bucket with proper folder structure
- [ ] Redshift/RDS tables configured
- [ ] EventBridge/Step Functions workflow
- [ ] README with:
  - Architecture diagram
  - How to deploy (CloudFormation/Terraform)
  - How to test
  - Cost estimation
  - Monitoring setup
- [ ] Committed to GitHub

### GitHub Repo Structure
```
project3-aws-pipeline/
├── infrastructure/
│   ├── cloudformation.yaml (or main.tf)
│   └── parameters.json
├── lambda/
│   ├── transform.py
│   └── requirements.txt
├── sql/
│   └── create_tables.sql
├── docs/
│   ├── architecture.md
│   └── deployment_guide.md
├── README.md
└── .gitignore
```

### Success Criteria
- ✅ Pipeline runs end-to-end without errors
- ✅ Data quality checks work
- ✅ Each layer is clearly defined and purposeful
- ✅ Architecture diagram is clear
- ✅ Someone could reproduce the pipeline from your docs

### Key Technologies
- AWS S3, Lambda, Glue, Redshift/RDS
- EventBridge/Step Functions, CloudWatch, IAM
- Python

### Estimated Time
15-18 hours total across Weeks 21–24

---

## PROJECT 4: ML Classification Pipeline
**Phase:** 5 - AWS Data Engineering (Mar 2026)  
**Status:** Not Started

### Overview
End-to-end ML model training and evaluation, demonstrating data + ML integration.

### Problem Statement
Choose ONE problem:
1. **Fraud Detection** - Classify transactions as fraudulent or legitimate
2. **Credit Risk** - Classify loan applicants as high/medium/low risk
3. **Financial Prediction** - Similar classification problem in finance domain

### Requirements
- [ ] **Data Preparation:**
  - Load data from CSV or SQL database
  - Explore data (shape, types, missing values)
  - Basic statistics and distributions
  
- [ ] **Feature Engineering:**
  - Create new features from raw data
  - Handle missing values (imputation or removal)
  - Scale numerical features
  - Encode categorical variables
  - Feature importance analysis
  
- [ ] **Model Training:**
  - Train at least 2 different models (logistic regression, random forest, etc.)
  - Use scikit-learn
  - Proper train/test split (80/20 or 70/30)
  - Hyperparameter tuning (grid search or random search)
  
- [ ] **Model Evaluation:**
  - Appropriate metrics (accuracy, precision, recall, F1, ROC-AUC)
  - Confusion matrix
  - Comparison of models
  - Error analysis
  
- [ ] **Model Tracking:**
  - Document model version, hyperparameters, metrics
  - MLflow or simple JSON tracking

### Deliverables
- [ ] Python scripts or Jupyter notebook
- [ ] Trained model (pickled or saved)
- [ ] Model Card document with:
  - Problem definition
  - Data description
  - Model architecture and hyperparameters
  - Performance metrics
  - Limitations and bias discussion
  - How to make predictions
- [ ] Visualization of results:
  - Feature importance plot
  - Confusion matrix
  - ROC curve or other performance curves
- [ ] README explaining the project
- [ ] Committed to GitHub

### GitHub Repo Structure
```
project4-ml-classification/
├── data/
│   ├── raw/
│   │   └── sample_data.csv
│   └── processed/ (optional)
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── data_preparation.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── evaluation.py
├── models/
│   └── model_v1.pkl
├── results/
│   ├── feature_importance.png
│   ├── confusion_matrix.png
│   └── metrics.json
├── model_card.md
├── README.md
└── .gitignore
```

### Success Criteria
- ✅ Model performs better than baseline (random guessing)
- ✅ Evaluation metrics are properly calculated
- ✅ Feature engineering is thoughtful (not random)
- ✅ Code is clean and reproducible
- ✅ Model card clearly documents the model

### Key Technologies
- Python (pandas, scikit-learn, numpy)
- Jupyter notebooks
- Visualization (matplotlib, seaborn)
- MLflow or model versioning

### Estimated Time
12-15 hours total in March 2026

---

## PROJECT 5: Databricks Medallion ETL
**Phase:** 4 - Databricks + Capstone (Jun–Jul 2026)  
**Status:** Not Started

### Overview
Production-grade ETL on Databricks implementing the Medallion architecture to prepare you for the Capstone build.

### Architecture
```
Data Source (CSV/API)
    ↓
[BRONZE] Raw ingestion (auto-loader or batch)
    ↓
[SILVER] Cleaning, standardization, validation
    ↓
[GOLD] Business aggregates and marts
    ↓
Dashboards / Consumers
```

### Requirements
- [ ] **Bronze Layer:**
  - Ingest raw data into Delta tables
  - Schema inference + evolution settings
  - Partitioning strategy

- [ ] **Silver Layer:**
  - Deduplicate + standardize types
  - Handle nulls and invalid records
  - Data quality checks with simple expectations

- [ ] **Gold Layer:**
  - Star-schema style outputs (facts/dims)
  - 3–5 business KPIs materialized

- [ ] **Workflows & Orchestration:**
  - Databricks Workflows job chaining Bronze→Silver→Gold
  - Retry and notifications on failure

- [ ] **Documentation:**
  - Diagram of medallion flow
  - README with setup, run instructions, and troubleshooting

### Deliverables
- [ ] Databricks notebooks for Bronze/Silver/Gold
- [ ] Workflow configuration (exported JSON/YAML or screenshots)
- [ ] Data quality helper (simple Python module)
- [ ] Architecture diagram
- [ ] README with reproduction steps
- [ ] Committed to GitHub

### GitHub Repo Structure
```
project5-databricks-medallion/
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformations.py
│   └── 03_gold_marts.py
├── src/
│   └── dq_checks.py
├── workflows/
│   └── medallion_job.json
├── docs/
│   ├── architecture.md
│   └── runbook.md
├── README.md
└── .gitignore
```

### Success Criteria
- ✅ Bronze→Silver→Gold runs end-to-end in Workflows
- ✅ Delta features used correctly (partitioning, schema evolution)
- ✅ KPIs computed and validated
- ✅ Docs clear enough to reproduce

### Key Technologies
- Databricks, PySpark, Delta Lake, Databricks Workflows

### Estimated Time
12-15 hours total in June–July 2026

---

## PROJECT 6: CAPSTONE - Commodity Price Monitoring System
**Phase:** 4 - Databricks + Capstone (Weeks 25–36, May 17 – Aug 3, 2026)  
**Status:** Not Started

### Overview
Production-grade end-to-end data platform demonstrating mastery of all skills.

**Scope:** 60% Data Engineering / 40% ML  
(Position as DE specialist with ML capability, not ML engineer doing DE work)

### Architecture

```
Daily API Calls (Gold, Silver, Oil, Gas)
    ↓
[BRONZE] Raw API responses
    ↓
[SILVER] Cleaned, validated, deduplicated
    ↓
[GOLD] Business metrics and analytics
    ↓
ML Model (Predict price movements)
    ↓
API Service (Serve predictions)
    ↓
Dashboard & Alerts
```

### Component 1: Data Ingestion (10%)
- [ ] Fetch commodity prices from public API daily
- [ ] Store raw responses in Databricks DBFS or S3
- [ ] Error handling and retries
- [ ] Scheduled job (Databricks Workflows or Airflow)

### Component 2: ETL Pipeline (40%)
- [ ] **Bronze → Silver:**
  - Validate price ranges (realistic values)
  - Handle missing data
  - Type conversions
  - Deduplication
  
- [ ] **Silver → Gold:**
  - Calculate daily metrics:
    - Price change %
    - Volatility (rolling std dev)
    - Moving averages
    - Trend indicators
  - Create fact tables (daily prices)
  - Create dimension tables (commodities, dates)
  - SCD Type 2 for dimension history

### Component 3: Data Quality (10%)
- [ ] Validation rules:
  - Price ranges (e.g., gold $900-2500/oz)
  - Completeness (all 4 commodities each day)
  - Freshness (data < 24 hrs old)
  
- [ ] Anomaly detection:
  - Z-score > 3 triggers alert
  - Unexpected price spikes logged
  
- [ ] Quality metrics:
  - Validation pass/fail rate
  - Records processed count
  - Data latency

### Component 4: ML Model (20%)
- [ ] Classification or regression:
  - Predict price direction (up/down/flat)
  - Or predict volatility (high/medium/low)
  
- [ ] Model pipeline:
  - Feature engineering (from Silver data)
  - Train/test split
  - Model training (scikit-learn or Spark MLlib)
  - Model evaluation metrics
  - Model versioning (MLflow)
  
- [ ] Serving:
  - Batch predictions (daily)
  - Simple REST API (Flask) or Lambda function
  - Store predictions in database

### Component 5: Orchestration (10%)
- [ ] Databricks Workflows:
  - Task 1: Data ingestion
  - Task 2: ETL (Bronze → Silver → Gold)
  - Task 3: ML predictions
  - Task 4: Quality checks
  - Task 5: Notifications
  
- [ ] Error handling:
  - Retry logic for failed tasks
  - Email/Slack alert on critical failures
  - Graceful degradation (skip ML if data bad)

### Component 6: Monitoring & Observability (10%)
- [ ] Dashboard showing:
  - Pipeline execution status
  - Data quality metrics
  - Model performance
  - Latest prices and predictions
  
- [ ] Logging:
  - All steps logged to Databricks / CloudWatch
  - Searchable and queryable
  
- [ ] Alerts:
  - Pipeline failures
  - Data quality issues
  - Anomalies detected

### Deliverables
- [ ] **Complete Databricks Workspace:**
  - All notebooks (ingestion, ETL, ML, monitoring)
  - Exported as .py files committed to GitHub
  
- [ ] **Complete Documentation:**
  - Architecture diagram (detailed)
  - Data dictionary (all columns, types, meanings)
  - Setup guide (how to reproduce)
  - API documentation (for prediction service)
  - Model card (model details, performance, limitations)
  
- [ ] **Demo Materials:**
  - 5-minute demo video (recorded)
  - Screenshots of dashboard
  - Sample prediction output
  
- [ ] **GitHub Repository:**
  - All code, notebooks, configs
  - CloudFormation/Terraform templates
  - Clear README
  - Reproducible setup instructions

### GitHub Repo Structure
```
project6-capstone-commodity-system/
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformations.py
│   ├── 03_gold_aggregations.py
│   ├── 04_ml_pipeline.py
│   └── 05_monitoring_dashboard.sql
├── src/
│   ├── data_quality.py
│   ├── model_training.py
│   ├── model_serving.py
│   └── orchestration.yaml
├── infrastructure/
│   ├── cloudformation.yaml
│   └── terraform/
├── docs/
│   ├── architecture.md
│   ├── data_dictionary.md
│   ├── setup_guide.md
│   ├── model_card.md
│   └── api_docs.md
├── visualizations/
│   ├── dashboard.png
│   ├── architecture.png
│   └── data_flow.png
├── demo/
│   └── demo_video_link.txt
├── README.md
└── .gitignore
```

### Success Criteria
- ✅ Pipeline runs end-to-end daily without errors
- ✅ Data quality checks working and alerting
- ✅ ML model training and prediction serving
- ✅ Architecture is clear and well-documented
- ✅ Someone could set up from your README
- ✅ Dashboard shows live system status
- ✅ Demo clearly shows capability

### Key Technologies
- Databricks (PySpark, Delta Lake, Workflows, SQL)
- Python (pandas, scikit-learn, MLflow)
- APIs (requests library or similar)
- Cloud storage (S3 or DBFS)
- Visualization (matplotlib, seaborn, simple dashboard)
- Flask or Lambda (for predictions)

### Estimated Time
25-30 hours total across Weeks 25-36

---

## SUMMARY TABLE

| Project | Phase | Duration | Status | Tech Stack |
|---------|-------|----------|--------|-----------|
| 1. Python Automation | Phase 1 (Python) | Nov–Dec | In Progress | Python, CLI |
| 2. Financial Analysis | Phase 2 (SQL) | Dec–Jan | Not Started | SQL, Python, Viz |
| 3. AWS Pipeline | Phase 3 (AWS & Cloud) | Mar–May | Not Started | AWS, IaC |
| 4. ML Classification | Phase 4 (Databricks + Capstone) | Jun–Jul | Not Started | scikit-learn, pandas |
| 5. Databricks Medallion ETL | Phase 4 (Databricks + Capstone) | May–Jun | Not Started | PySpark, Delta |
| 6. CAPSTONE | Weeks 25–36 | May 17–Aug 3 | Not Started | Full stack |

**Total Time:** ~90-100 hours across 7 months  
**Portfolio Value:** High (demonstrates full-stack capability)  
**Job Interview Value:** Strong talking points for each project

---

## PROJECT SUBMISSION CHECKLIST

For each project, before considering it "done":

- [ ] Code runs without errors
- [ ] README is comprehensive (problem, setup, usage, output)
- [ ] Code is well-commented and readable
- [ ] Git history shows multiple commits (not 1 giant commit)
- [ ] .gitignore is set up (don't commit data files, secrets, etc.)
- [ ] All files are on GitHub (not just local)
- [ ] Architecture/flow is documented (diagram or text)
- [ ] Someone else could run it from your README
- [ ] No credentials/secrets in code
- [ ] At least one interesting insight or "lesson learned" in README

---

## NOTES

1. **These are real projects**, not theoretical exercises
2. **Working code > perfect code**—ship it, don't polish forever
3. **Each project teaches multiple concepts**—stack your learning
4. **Projects get progressively complex**—builds confidence
5. **Projects are portfolio pieces**—show them in interviews with pride

---

**Version:** 1.0 - Authoritative Project Library  
**Created:** November 18, 2025  
**Note:** All other "project lists" are deprecated. This is your source of truth.
