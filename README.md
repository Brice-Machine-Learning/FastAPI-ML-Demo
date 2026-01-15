# FastAPI + Machine Learning Demo

## Purpose

This project is a **minimal, instructional example** designed to
demonstrate the relationship between a **trained machine learning
model** and a **FastAPI application**.

The goal is **not** to build a highly accurate or production-ready
model.

The goal **is** to show:

- how a machine learning model is trained *before* any API code exists
- how that trained model is saved as an artifact
- how inference logic is isolated from web concerns
- how FastAPI acts as a thin wrapper around inference

This project was built to support a **small class** focused on
understanding ML-to-API workflows, not model optimization.

------------------------------------------------------------------------

## What This Project Is (and Is Not)

### This project **is**

- a basic supervised learning example
- a regression model trained with default settings
- an end-to-end ML → inference → FastAPI pipeline
- intentionally simple and readable
- focused on correct sequencing and separation of concerns

### This project **is not**

- a tuned or optimized ML model
- a production-ready system
- a showcase of advanced modeling techniques
- intended for real-world housing valuation
- an example of hyperparameter tuning or model comparison

------------------------------------------------------------------------

## High-Level Workflow

    Data → EDA → Feature Engineering → Model Training
         → Model Artifact → Inference Code → FastAPI

FastAPI is introduced **only after** a trained model and inference logic
exist.

------------------------------------------------------------------------

## Dataset

- Dataset: California Housing dataset
- Problem type: Regression
- Target variable: `MedHouseVal`
- Target units: **hundreds of thousands of USD**

Each row represents a **census tract (neighborhood)**, not a city or an
individual house.

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

## Machine Learning Approach

- Model: **Linear Regression**
- No hyperparameter tuning
- No model selection
- No cross-validation
- No feature engineering beyond scaling
- Default scikit-learn settings

This simplicity is **intentional**.

The model exists only to produce a real artifact that can be served via
an API.

------------------------------------------------------------------------

## Inference Design

- Inference logic is written **before FastAPI** and lives in a standalone module.
- Responsibilities of inference: - load the trained model artifact - validate input shape - apply scaling - return a numeric prediction
- Inference code is: - framework-agnostic - reusable - testable without FastAPI
- FastAPI simply calls this logic.

------------------------------------------------------------------------

## FastAPI Application

- FastAPI is used as a **thin transport layer**.
- It does: - define request and response schemas - accept HTTP requests -
call the inference function - return predictions
- It does **not**: - train models - load datasets - define features -
contain ML logic

------------------------------------------------------------------------

## Running the App

From the project root:

    uvicorn fastapi_ml_demo.main:app --reload

Then open:

    uvicorn fastapi_ml_demo.main:app --reload

Then open:

    http://127.0.0.1:8000/docs

Use the interactive Swagger UI to send prediction requests.

------------------------------------------------------------------------

## Common Pitfalls (Intentionally Avoided)

### 1. Training Models Inside FastAPI

- All model training happens offline. FastAPI only serves predictions.

### 2. Mixing ML Logic with API Code

- Inference logic is isolated from the web layer.

### 3. Skipping Artifacts

- The trained model is saved and reused --- never recreated.

### 4. Implicit Feature Order

- Feature order is explicit and validated.

### 5. Over-Optimizing the Model

- No tuning or model comparison is performed.

------------------------------------------------------------------------

## Class Demo Version (Read This First)

This project is a **teaching scaffold**, not a production blueprint.

- Focus on: - ML before APIs - artifacts as contracts - inference
- isolation - FastAPI as transport
- Ignore: - model accuracy - tuning - production concerns

------------------------------------------------------------------------

## Key Teaching Takeaway

>**Machine learning models come first.**  
>**APIs come last.**  
>**FastAPI is not where ML happens.**
