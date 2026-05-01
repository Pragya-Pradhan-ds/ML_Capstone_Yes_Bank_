import sys
import pandas as pd

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.utils.utils import load_object


class PredictionPipeline:

    def __init__(self):
        self.model_path = "artifacts/model.pkl"
        self.preprocessor_path = "artifacts/preprocessor.pkl"

    # ✅ ADD THIS METHOD INSIDE CLASS
    def convert_date(self, df: pd.DataFrame) -> pd.DataFrame:
        df["Date"] = pd.to_datetime(df["Date"], format="%b-%y")
        df["Month"] = df["Date"].dt.month
        df["Year"] = df["Date"].dt.year
        df.drop(columns=["Date"], inplace=True)
        return df

    def predict(self, input_data: pd.DataFrame):
        try:
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)

            # ✅ APPLY SAME TRANSFORMATION
            input_data = self.convert_date(input_data)

            data_transformed = preprocessor.transform(input_data)

            prediction = model.predict(data_transformed)

            return prediction

        except Exception as e:
            raise YesBankException(e, sys)