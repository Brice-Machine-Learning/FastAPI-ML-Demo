# FastAPI + Machine Learning: From Model to API (End-to-End)

## Overview

This project demonstrates how a **machine learning model is built
first**,\
*before* any API code is written, and how FastAPI is later used as a
**thin delivery layer**.

The goal is to show students the **correct order of operations**:

1. Understand the data\
2. Engineer features\
3. Train a model\
4. Export a model artifact\
5. Write inference code\
6. Wrap inference with FastAPI

FastAPI does **not** train models.\
FastAPI does **not** contain ML logic.\
FastAPI simply calls inference code.

------------------------------------------------------------------------

## Project Structure

    fastapi_ml_demo/
    ├── artifacts/
    │   ├── feature_metadata.json
    │   └── housing_regression_v1.joblib
    │
    ├── notebooks/
    │   ├── 00_baseline.ipynb
    │   ├── 01_eda.ipynb
    │   ├── 02_feature_engineering.ipynb
    │   └── 03_model_training.ipynb
    │
    ├── src/
    │   └── fastapi_ml_demo/
    │       ├── core/
    │       │   └── inference.py
    │       ├── schemas/
    │       │   └── prediction.py
    │       ├── main.py
    │       └── __init__.py
    │
    └── pyproject.toml

------------------------------------------------------------------------

## Step 1: Dataset & Baseline

We used the **California Housing dataset**, a regression dataset where
the target is:

- `MedHouseVal`: median house value\
- Units: **hundreds of thousands of dollars**

Example: - Prediction `2.5` → \~\$250,000

------------------------------------------------------------------------

## Step 2: Exploratory Data Analysis (EDA)

EDA was performed to answer **decision questions**, not to train models:

- What are we predicting?
- What features exist?
- Are there missing values?
- Are feature scales comparable?
- Is the target capped?

------------------------------------------------------------------------

## Step 3: Feature Engineering

Feature engineering was kept **explicit and minimal**.

### Decisions made

- Explicit feature list defined
- Target separated from features
- Scaling required (standardization)
- Scaling fit on training data only

Artifacts produced: - `feature_metadata.json`

------------------------------------------------------------------------

## Step 4: Model Training

A **baseline Linear Regression model** was trained.

Artifacts produced: - `housing_regression_v1.joblib`

------------------------------------------------------------------------

## Step 5: Inference Module

Inference logic was written **before FastAPI**.

Responsibilities: - Load model artifact - Validate inputs - Apply
scaling - Return prediction

------------------------------------------------------------------------

## Step 6: FastAPI as a Thin Wrapper

FastAPI was added **last** and only handles HTTP.

------------------------------------------------------------------------

## Demo

Use the built-in Swagger UI:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Key Takeaways

- Models come before APIs
- Artifacts are the contract
- FastAPI is transport only

------------------------------------------------------------------------

## Status

✔ Model trained\
✔ Artifact exported\
✔ Inference isolated\
✔ API serving predictions
