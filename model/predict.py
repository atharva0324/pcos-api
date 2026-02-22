import pickle
import pandas as pd
#importing the ML Model
with open('model/model_1.pkl','rb') as f:
    model=pickle.load(f)

def predict_output(input:dict):
    input_df=pd.DataFrame([input])
    X_t = model["transformer"].transform(input_df)
    proba = model["model"].predict_proba(X_t)[:, 1]
    pred = int((proba >= model["threshold"]).astype(int)[0])
    prob_value = float(proba[0])
    return {
        "prediction": int(pred),
        "probability": prob_value
    }



