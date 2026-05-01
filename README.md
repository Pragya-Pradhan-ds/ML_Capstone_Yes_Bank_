# 📈 Yes Bank Stock Price Prediction - ML Pipeline

## 🔍 Overview

This project implements an end-to-end machine learning pipeline to predict Yes Bank stock closing prices using historical stock data.

The pipeline is modular and production-ready, covering:

* Data Ingestion
* Data Transformation
* Model Training
* Model Evaluation
* Prediction Pipeline

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* NumPy, Pandas
* Logging & Exception Handling
* Streamlit (optional)

---

## 📁 Project Structure

```
ML_YES_BANK/
│
├── artifacts/
├── data/
│   └── data_YesBank_StockPrices.csv
│
├── Yes_Bank/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── pipeline/
│   │   ├── prediction_pipeline.py
│   │   └── input_data.py
│   │
│   ├── entity/
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── utils/
│   ├── logging/
│   └── exception/
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🚀 Pipeline Workflow

### 1. Data Ingestion

* Loads dataset
* Splits into train/test
* Stores artifacts

### 2. Data Transformation

* Feature engineering
* Data preprocessing
* Converts data into NumPy arrays

### 3. Model Training

* Linear Regression
* Ridge, Lasso, ElasticNet
* KNN Regressor
* Random Forest
* Selects best model based on R² score

### 4. Model Evaluation

* R² Score
* MAE (Mean Absolute Error)

### 5. Prediction Pipeline

* Takes user input
* Returns predicted closing price

---

## 📊 Results

| Metric   | Value |
| -------- | ----- |
| R² Score | ~0.99 |
| MAE      | ~5.89 |

All models performed strongly with minimal variation.
KNN performed slightly better than others.

---

## ▶️ How to Run

### Clone Repository

```
https://github.com/Pragya-Pradhan-ds/ML_Capstone_Yes_Bank_.git
```

### Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run Pipeline

```
python main.py
```

---

## 🔮 Example Prediction

```
from Yes_Bank.pipeline.prediction_pipeline import PredictionPipeline
from Yes_Bank.pipeline.input_data import CustomData

data = CustomData(
    Date="Dec-20",
    Open=100,
    High=110,
    Low=95
)

df = data.get_data_as_dataframe()

pipeline = PredictionPipeline()
prediction = pipeline.predict(df)

print(prediction)
```

---

## 🌐 Streamlit App (Optional)

```
streamlit run app.py
```

---

## ⚠️ Notes

* High R² (~0.99) indicates strong feature correlation
* Ensure no data leakage
* Model differences are minimal

---

## 💡 Future Improvements

* Hyperparameter tuning
* Feature importance analysis
* Cloud deployment
* Real-time stock data

---

## 👤 Author

Pragya Pradhan

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
