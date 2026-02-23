import streamlit as st
import pandas as pd
import joblib

# STYLE BLOCK
st.markdown("""
<style>

/* =========================
   MAIN BACKGROUND
========================= */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}


/* =========================
   TEXT COLORS
========================= */
h1, h2, h3, label, .stMarkdown, .stText {
    color: white !important;
}


/* =========================
   SIDEBAR
========================= */
section[data-testid="stSidebar"] {
    background: #111827;
    color: white;
}


/* =========================
   INPUT BOXES (LIGHT STYLE)
========================= */
div[data-baseweb="input"] {
    background-color: white !important;
    border-radius: 8px !important;
}

/* INPUT TEXT — VERY IMPORTANT FIX */
div[data-baseweb="input"] input {
    color: #111827 !important;
    -webkit-text-fill-color: #111827 !important;
    font-weight: 600 !important;
}

/* Placeholder text */
div[data-baseweb="input"] input::placeholder {
    color: #6b7280 !important;
}


/* =========================
   SELECT BOX TEXT
========================= */
div[data-baseweb="select"] * {
    color: #111827 !important;
}


/* =========================
   SLIDER COLOR
========================= */
.stSlider > div > div > div > div {
    background: #22c55e !important;
}


/* =========================
   BUTTON STYLE
========================= */
.stButton>button {
    background-color: #22c55e;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1em;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #16a34a;
}


/* =========================
   RESULT BOX IMPROVEMENT
========================= */
.stAlert {
    border-radius: 10px !important;
}


/* =========================
   REMOVE STREAMLIT HEADER SPACE
========================= */
header[data-testid="stHeader"] {
    background: transparent;
}


/* =========================
   OPTIONAL: nicer section spacing
========================= */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# HEADER WITH LOGO

col1, col2 = st.columns([1,6])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/4149/4149643.png", width=70)

with col2:
    st.markdown("""
    <h1 style='margin-bottom:0;'>Predictive Maintenance Failure Predictor</h1>
    <p style='margin-top:0;color:#cbd5e1;font-size:18px;'>
    AI-powered industrial machine risk detection system
    </p>
    """, unsafe_allow_html=True)

st.divider()

st.title("Predictive Maintenance Failure Predictor")
st.sidebar.title("About")
st.sidebar.write(
    "This app predicts machine failure risk using an ML model trained on the AI4I dataset."
)
st.sidebar.write("Enter machine parameters and click Predict.")


st.sidebar.title("About")
st.sidebar.write(
    "This app predicts machine failure risk using an ML model trained on the AI4I dataset."
)



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
        "Type": type_num,
        "Air temperature [K]": air,
        "Process temperature [K]": process,
        "Rotational speed [rpm]": rpm,
        "Torque [Nm]": torque,
        "Tool wear [min]": wear
    }])
    
    threshold = st.slider("Risk Threshold", 0.0, 1.0, 0.5)

if st.button("Predict"):

    proba = model.predict_proba(input_df)[0][1]

    st.subheader("Result")

    st.markdown(f"""
    <div style="
        background:#0b1220;
        padding:20px;
        border-radius:12px;
        margin-top:15px;
        border:1px solid #334155;
    ">
        <h3 style="color:white;">Failure Probability</h3>
        <h1 style="color:#22c55e;">{proba:.2%}</h1>
    </div>
    """, unsafe_allow_html=True)

    if proba > threshold:
        st.error("⚠ HIGH FAILURE RISK — maintenance recommended")
    else:
        st.success("✅ LOW FAILURE RISK — continue monitoring")