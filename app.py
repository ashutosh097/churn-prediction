from fastapi import FastAPI, Body, HTTPException
import pandas as pd
import joblib
import numpy as np

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI()


# Load model 
model = joblib.load("model/churn_model.pkl")


# Serve the simple UI from the static folder at /static and expose index at /
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root_index():
    return FileResponse("static/index.html")


@app.post("/api/predict")
def predict_churn(payload: dict = Body(...)):
    try:
        df = pd.DataFrame([payload])

        if "TotalCharges" in df.columns:
            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        if "tenure" in df.columns:
            df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")

        df["AverageMonthlyCharges"] = df["TotalCharges"] / df["tenure"].replace(0, np.nan)

        df["TenureGroup"] = pd.cut(
            df["tenure"],
            bins=[-1, 12, 24, 48, 72],
            labels=["New", "Short-Term", "Medium-Term", "Long-Term"]
        )
        df["TenureGroup"] = df["TenureGroup"].astype(object)

        # Predict using the loaded model
        pred = model.predict(df)[0]
        prob = None
        try:
            prob = float(model.predict_proba(df)[0][1])
        except Exception:
            pass


        return {
            "prediction": "Yes" if int(pred) == 1 else "No",
            "churn_probability": round(prob, 4) if prob is not None else None,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")
