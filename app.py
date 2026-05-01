import streamlit as st
import pandas as pd

from Yes_Bank.pipeline.prediction_pipeline import PredictionPipeline
from Yes_Bank.pipeline.input_data import CustomData

st.set_page_config(page_title="Yes Bank Stock Predictor")

st.title("📈 Yes Bank Stock Price Prediction")

st.write("Enter stock details to predict Close price")

# 👉 User Inputs
date = st.text_input("Date (format: Dec-20)")
open_price = st.number_input("Open Price")
high = st.number_input("High Price")
low = st.number_input("Low Price")

# 👉 Button
if st.button("Predict"):

    try:
        data = CustomData(
            Date=date,
            Open=open_price,
            High=high,
            Low=low
        )

        df = data.get_data_as_dataframe()

        pipeline = PredictionPipeline()
        prediction = pipeline.predict(df)

        st.success(f"Predicted Close Price: {prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")