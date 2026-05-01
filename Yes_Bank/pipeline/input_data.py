import pandas as pd


class CustomData:
    def __init__(self, Date, Open, High, Low):
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low

    def get_data_as_dataframe(self):
        data = {
            "Date": [self.Date],
            "Open": [self.Open],
            "High": [self.High],
            "Low": [self.Low],
        }

        return pd.DataFrame(data)