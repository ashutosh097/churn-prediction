# Customer Churn Prediction — Assignment

**Objective:**
- Build a model to predict customer churn from the provided Telco dataset and produce a simple web service + UI to demonstrate predictions.

**Files produced / used:**
- **Notebook:** [notebook/churn_analysis.ipynb](notebook/churn_analysis.ipynb)
- **Model:** [model/churn_model.pkl](model/churn_model.pkl)
- **API server:** [app.py](app.py)
- **Web UI:** [static/index.html](static/index.html)

**Dataset:**
- `data/Telco_Customer_Churn.csv` — customer subscription and usage records (demographics, services, billing, churn label).

**Exploratory Data Analysis (EDA):**
- Inspected distributions of numeric features (`tenure`, `MonthlyCharges`, `TotalCharges`) and categorical features (contract type, payment method, services).
- Observed churn correlates: shorter tenure, higher monthly charges, and month-to-month contracts tend to churn more.
- Visualizations and concise observations are included in the notebook.

**Preprocessing:**
- Convert `TotalCharges` to numeric, coerce/handle missing or whitespace values.
- Fill or drop rows as required by the chosen preprocessing strategy.
- Use a `ColumnTransformer` to apply scaling for numeric features and one-hot encoding for categorical features so the trained pipeline is end-to-end reproducible.

**Modeling approach:**
- Baseline: Decision Tree classifier (simple, interpretable) to sanity-check pipeline behavior.
- Final model: CatBoost (handles categorical features, robust to defaults) and `GridSearchCV`-style tuning for a small set of hyperparameters.
- The notebook contains training, cross-validation, and evaluation steps.

**Evaluation:**
- Evaluate models using accuracy, precision/recall as appropriate, and ROC-AUC for ranking performance.
- Example: a sample curl/predict returned probability ~0.8335 for the example input used in testing.

**Saved artifacts:**
- Final fitted pipeline + model saved to `model/churn_model.pkl` (loaded by `app.py` for inference).

**API & UI (how it works):**
- `app.py` exposes a POST endpoint `/api/predict` that accepts a JSON payload containing the same input features used in training and returns a JSON response with `prediction` and `churn_probability` (when available).
- `static/index.html` is a single-page UI that:
  - Provides a compact form matching the training features.
  - Has a "Paste JSON" mode for directly submitting a JSON payload.
  - Shows an interactive badge and probability bar for prediction confidence.
  - Includes a "Use sample payload" and "Use sample JSON" for quick testing.

**Run instructions (local):**
1. Create a Python environment and install dependencies. Example (adjust if using a different environment manager):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requiremnts.txt
```

2. Start the API server (from repository root):

```bash
uvicorn app:app --host 127.0.0.1 --port 8000
```

3. Open the UI in a browser: http://127.0.0.1:8000/

4. Example curl request (replace values as needed):

```bash
curl -X POST "http://127.0.0.1:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{"gender":"Female","SeniorCitizen":0,"Partner":"Yes","Dependents":"No","tenure":5,"PhoneService":"Yes","MultipleLines":"No","InternetService":"Fiber optic","OnlineSecurity":"No","OnlineBackup":"No","DeviceProtection":"No","TechSupport":"No","StreamingTV":"No","StreamingMovies":"No","Contract":"Month-to-month","PaperlessBilling":"Yes","PaymentMethod":"Electronic check","MonthlyCharges":85.5,"TotalCharges":427.5}'
```

_Last updated: 2026-09-11_
