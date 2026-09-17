# Customer Churn Prediction — Assignment

This project builds a customer churn prediction system for a telecom company and exposes it through a FastAPI-based web service.

## GitHub repository
https://github.com/ashutosh097/churn-prediction

## Project structure
- Notebook: [notebook/churn_analysis.ipynb](notebook/churn_analysis.ipynb)
- Trained model: [model/churn_model.pkl](model/churn_model.pkl)
- API app: [app.py](app.py)
- UI: [static/index.html](static/index.html)
- Sample payloads: [sample_request_for_churn_true.json](sample_request_for_churn_true.json), [sample_request_for_churn_false.json](sample_request_for_churn_false.json)
- Root sample request: [sample_request.json](sample_request.json)

## Objective
Predict whether a customer is likely to churn so that the retention team can proactively engage with at-risk customers.

## Dataset
The project uses the Telco Customer Churn dataset from [data/Telco_Customer_Churn.csv](data/Telco_Customer_Churn.csv). The dataset contains customer demographics, service usage, billing information, and the target variable `Churn`.

## Workflow covered
- Data loading and structure checks
- Missing value and duplicate analysis
- Numerical and categorical feature identification
- Target variable analysis
- Data cleaning and preprocessing
- Feature engineering
- Train/test split with `random_state=42`
- EDA with business insights
- Decision tree model development and comparison
- Model evaluation using accuracy, precision, recall, F1-score, and confusion matrix
- Model interpretation and feature importance
- Model saving and API deployment

## Install dependencies
Create a virtual environment and install the project requirements:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the application
Start the API server from the project root:

```bash
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

Open the UI in a browser:
- http://127.0.0.1:8000/

## API endpoint
The application exposes a POST endpoint at `/predict` and returns a churn prediction plus the estimated probability.

The UI is served at the root URL `/`, while the API is available at `/predict`.

### Example request
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.5,
    "TotalCharges": 427.5
  }'
```

### Example response
```json
{
  "prediction": "Yes",
  "churn_probability": 0.82
}
```

## Notes
- The API expects a JSON payload with the same feature names used in training.
- Invalid or incomplete input is handled with an error response.
- The saved model and preprocessing logic are used for consistent predictions on new customer data.

