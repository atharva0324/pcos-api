# PCOS Risk Prediction System

A machine learning system that predicts the risk of Polycystic Ovary Syndrome (PCOS) using two prediction modes — one for users without lab reports, and one for users with clinical data. Built with XGBoost, FastAPI, and Streamlit.

---

## What It Does

PCOS affects roughly 1 in 10 women of reproductive age and often goes undiagnosed. This system allows users to get a risk probability score based on either:

- **Personal mode** — uses basic health and lifestyle information (no lab reports needed)
- **Medical mode** — uses clinical lab values for a more accurate prediction

---

## Models

| | Model 1 (Personal) | Model 2 (Clinical) |
|---|---|---|
| **Algorithm** | XGBoost | XGBoost |
| **Input Features** | 17 personal/lifestyle features | 34 personal + clinical features |
| **Threshold** | 0.54 | 0.50 |
| **Recall (PCOS class)** | 0.80 | 0.89 |
| **Precision (PCOS class)** | 0.78 | 0.75 |
| **Recall (No PCOS class)** | 0.89 | 0.86 |
| **Precision (No PCOS class)** | 0.90 | 0.94 |

Both models were trained, tuned, and tracked using **MLflow** — experiments include baseline comparisons (Random Forest, SVC, XGBoost), hyperparameter tuning, and threshold optimization.

---

## Project Structure

```
pcos-api/
│
├── model/                      # Model 1 - personal prediction
│   └── predict.py
│
├── model_2/                    # Model 2 - clinical prediction
│   └── predict_2.py
│
├── schema/                     # Pydantic input schemas
│   ├── user_input.py
│   └── user_input_2.py
│
├── notebooks/                  # Jupyter notebooks
│   ├── eda.ipynb               # Exploratory Data Analysis
│   ├── model1_training.ipynb   # Model 1 training + MLflow tracking
│   └── model2_training.ipynb   # Model 2 training + MLflow tracking
│
├── pcos_1.py                   # FastAPI backend
├── frontend.py                 # Streamlit frontend
└── requirements.txt
```

---

## Tech Stack

- **ML** — XGBoost, Scikit-learn
- **Experiment Tracking** — MLflow
- **API** — FastAPI
- **Frontend** — Streamlit
- **Language** — Python

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/atharva0324/pcos-api.git
cd pcos-api
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start the FastAPI backend**
```bash
uvicorn pcos_1:app --reload
```

**4. Start the Streamlit frontend** (in a new terminal)
```bash
streamlit run frontend.py
```

**5. Open your browser**
```
http://localhost:8501
```

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Home |
| `/health` | GET | Health check |
| `/predict_personal` | POST | Predict using personal features |
| `/predict_clinical` | POST | Predict using clinical features |

---

## Experiment Tracking with MLflow

All training experiments were tracked using MLflow including:
- Model comparisons (Random Forest, SVC, XGBoost)
- Hyperparameter tuning runs
- Threshold optimization
- Class-wise precision, recall, and F1 scores per run

To view the experiment dashboard locally:
```bash
cd "path/to/pcos-api"
mlflow ui --backend-store-uri sqlite:///mlflow.db
```
Then open `http://127.0.0.1:5000`