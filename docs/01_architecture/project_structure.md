# Project Structure

fastapi-ml-demo/
│
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── schemas.py         # Pydantic request/response models
│   ├── model.py           # Model loading + prediction logic
│
├── models/
│   └── iris_model.joblib  # Pre-trained ML model
│
├── train_model.py         # One-time training script
├── requirements.txt
└── README.md
