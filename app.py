import streamlit as st
import pandas as pd
import joblib

st.title("Predictive Maintenance Failure Predictor")
st.sidebar.title("About")
st.sidebar.write(
    "This app predicts machine failure risk using an ML model trained on the AI4I dataset."
)
st.sidebar.write("Enter machine parameters and click Predict.")

# load model
model = joblib.load("model/pipeline.joblib")
# helper: get expected number of input features
expected_n = getattr(model, "n_features_in_", None)
st.caption(f"Model expects {expected_n} numeric features." if expected_n else "Model loaded.")
type_ = st.selectbox("Machine Type", ["L","M","H"])
air = st.number_input("Air temperature [K]", value=300.0)
process = st.number_input("Process temperature [K]", value=310.0)
rpm = st.number_input("Rotational speed [rpm]", value=1500.0)
torque = st.number_input("Torque [Nm]", value=40.0)
wear = st.number_input("Tool wear [min]", value=120.0)

# Encode machine type (simple ordinal encoding)
type_map = {"L": 0.0, "M": 1.0, "H": 2.0}
type_num = type_map[type_]

# Try to match what the model expects:
# Case A: model trained with Type included as ONE numeric column (6 features total)
# Case B: model trained WITHOUT Type (5 features total)
if expected_n == 5:
    input_df = pd.DataFrame([{
        "Air temperature [K]": air,
        "Process temperature [K]": process,
        "Rotational speed [rpm]": rpm,
        "Torque [Nm]": torque,
        "Tool wear [min]": wear
    }])
else:
    # default: include Type as numeric
    input_df = pd.DataFrame([{
    "Type": type_,
    "Air temperature [K]": air,
    "Process temperature [K]": process,
    "Rotational speed [rpm]": rpm,
    "Torque [Nm]": torque,
    "Tool wear [min]": wear
}])
    
    threshold = st.slider("Risk Threshold", 0.05, 0.95, 0.50, 0.01)

if st.button("Predict"):
    proba = model.predict_proba(input_df)[0][1]
    pred = model.predict(input_df)[0]

    st.subheader("Result")
    st.metric("Failure Probability", f"{proba:.2%}")

    if proba >= threshold:
        st.error("⚠️ HIGH FAILURE RISK")
        st.write("Recommended action: Inspect machine and schedule maintenance.")
    else:
        st.success("🟢 LOW FAILURE RISK")
        st.write("Recommended action: Continue monitoring.")