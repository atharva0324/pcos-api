import pickle
import pandas as pd

with open("model_2/model_2.pkl","rb") as f:
    model_2=pickle.load(f)

def predict_output2(input:dict):
    input_df=pd.DataFrame([input])
    X_t = model_2["transformer"].transform(input_df)
    pred = int(model_2["model"].predict(X_t)[0])
    proba = model_2["model"].predict_proba(X_t)[:, 1]
    prob_value = float(proba[0])
    return {
            "prediction": int(pred),
            "probability": prob_value
        }
