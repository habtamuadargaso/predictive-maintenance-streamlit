
# 🚀 Predictive Maintenance Failure Predictor

🔗 **Live Demo:**
[https://predictive-maintenance-app-mmvekivq54jgrdehkwyaxz.streamlit.app/](https://predictive-maintenance-app-mmvekivq54jgrdehkwyaxz.streamlit.app/)

---

## 📌 Project Overview

This project is an **end-to-end Machine Learning web application** that predicts the probability of industrial machine failure using operational sensor data.

The system helps organizations:

* Detect high-risk machines early
* Reduce downtime
* Optimize maintenance scheduling
* Prevent unexpected failures

The model is trained on the **AI4I 2020 Predictive Maintenance dataset** and deployed as a **public interactive Streamlit web app**.

---

## 🧠 Machine Learning Workflow

✔ Data loading and preprocessing
✔ Feature engineering and selection
✔ Handling categorical variables
✔ Model training using Logistic Regression
✔ Pipeline creation with preprocessing + model
✔ Model evaluation and probability prediction
✔ Saving trained pipeline with `joblib`
✔ Deploying interactive web app using Streamlit Cloud

---

## 📊 Input Features

The app predicts machine failure using:

* Machine Type (L / M / H)
* Air Temperature (K)
* Process Temperature (K)
* Rotational Speed (RPM)
* Torque (Nm)
* Tool Wear (minutes)

---

## 📈 Output

The application returns:

* **Failure probability (%)**
* **Risk classification (Low / High)**
* **Recommended maintenance action**

---



### Input Interface
![App Input](assets/app_input.png)

### Prediction Result
![Prediction Result](assets/app_result.png)
---

## ⚙️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Git & GitHub
* Streamlit Cloud (deployment)

---

## 📂 Project Structure

```
predictive-maintenance-streamlit/
│
├── app.py
├── requirements.txt
├── model/
│   └── pipeline.joblib
├── assets/        # screenshots (optional)
└── README.md
```

---

## ▶️ Run Locally

### 1️⃣ Clone repository

```bash
git clone https://github.com/habtamuadargaso/predictive-maintenance-streamlit.git
cd predictive-maintenance-streamlit
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Streamlit app

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🌍 Deployment

The app is deployed publicly using **Streamlit Community Cloud**.

👉 Live link:
[https://predictive-maintenance-app-mmvekivq54jgrdehkwyaxz.streamlit.app/](https://predictive-maintenance-app-mmvekivq54jgrdehkwyaxz.streamlit.app/)

---

## 👤 Author

**Habtamu Dargaso**

* Data Scientist | Machine Learning Engineer
* Master’s in Data Science & Computer Science
* Seattle, WA

GitHub:
[https://github.com/habtamuadargaso](https://github.com/habtamuadargaso)

LinkedIn:
linkedin.com/in/habtamu-dargaso-b81676119









