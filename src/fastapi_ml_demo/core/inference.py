from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from typing import Sequence

# -------------------------------------------------------------------
# Artifact loading
# -------------------------------------------------------------------

ARTIFACT_PATH = Path(__file__).resolve().parents[3] / "artifacts" / "housing_regression_v1.joblib"

_artifact = joblib.load(ARTIFACT_PATH)

_model = _artifact["model"]
_scaler = _artifact["scaler"]
_features = _artifact["features"]
_target = _artifact["target"]

# -------------------------------------------------------------------
# Public inference function
# -------------------------------------------------------------------

def predict(features: Sequence[float]) -> float:
    """
    Run inference using the trained regression model.

    Returns the raw model prediction in dataset units
    (MedHouseVal, units of $100,000).
    """

    if len(features) != len(_features):
        raise ValueError(
            f"Expected {len(_features)} features "
            f"({', '.join(_features)}), "
            f"got {len(features)}."
        )

    # Preserve feature semantics
    # If you trained with DataFrames, you must infer with DataFrames — otherwise you’re relying on silent assumptions
    X = pd.DataFrame([features], columns=_features)

    X_scaled = _scaler.transform(X)
    prediction = _model.predict(X_scaled)

    return float(prediction[0])


def predict_price_usd(features: Sequence[float]) -> float:
    """
    Returns predicted median house value in USD.
    """
    return predict(features) * 100_000
