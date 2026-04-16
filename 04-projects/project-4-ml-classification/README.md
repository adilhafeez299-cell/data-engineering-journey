# Project 4: ML Classification Pipeline

**Timeline:** Weeks 11-12 (Month 3)
**Status:** Not Started

---

## Overview

Build a machine learning classification pipeline with end-to-end data processing, model training, and evaluation. This project demonstrates ability to work with ML workflows, feature engineering, and model deployment concepts relevant to data engineering.

**What to Build:**
An ML data pipeline that:
- Processes raw data for ML consumption
- Engineers features for classification
- Trains and evaluates classification models
- Implements model versioning
- Creates prediction pipeline

---

## Learning Objectives

- Understand ML data pipeline requirements
- Practice feature engineering techniques
- Learn data preprocessing for ML
- Implement train/test/validation splits
- Evaluate model performance metrics
- Version and track ML experiments
- Build reproducible ML workflows

---

## Tech Stack

**Core:**
- Python
- Pandas, NumPy
- scikit-learn

**Supporting:**
- Matplotlib, Seaborn (visualization)
- MLflow (experiment tracking)
- Jupyter notebooks (exploration)

**Development:**
- Git for version control
- Virtual environment
- pytest for testing

---

## Success Criteria

- [ ] Pipeline handles raw data to predictions
- [ ] Implements feature engineering pipeline
- [ ] Trains at least 2 classification algorithms
- [ ] Includes proper train/test splits
- [ ] Evaluates models with multiple metrics
- [ ] Uses cross-validation
- [ ] Tracks experiments with MLflow
- [ ] Includes feature importance analysis
- [ ] Has reproducible results (set seeds)
- [ ] Documentation explains model choices

---

## Project Structure

```
project-4-ml-classification/
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── prediction_pipeline.py
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_experimentation.ipynb
├── tests/
│   ├── test_preprocessing.py
│   └── test_features.py
├── models/
│   └── .gitkeep
├── data/
│   ├── raw/
│   ├── processed/
│   └── .gitkeep
├── config/
│   └── config.yaml
├── README.md
└── requirements.txt
```

---

## Implementation Notes

**Pipeline Components:**
1. Data validation and cleaning
2. Feature engineering
3. Model training
4. Model evaluation
5. Prediction serving

**Models to Implement:**
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting (optional)

**Key Features:**
- Automated feature preprocessing
- Hyperparameter tuning
- Model comparison framework
- Performance visualization

---

## Resources

- Reference: PROJECT_LIBRARY_v1_AUTHORITATIVE.md for detailed specifications
- scikit-learn documentation: https://scikit-learn.org/
- MLflow documentation: https://mlflow.org/docs/
- Feature engineering best practices

---

## Next Steps

1. Select classification dataset
2. Perform exploratory data analysis
3. Build feature engineering pipeline
4. Implement model training workflow
5. Evaluate and compare models
6. Create prediction pipeline
7. Document findings and methodology