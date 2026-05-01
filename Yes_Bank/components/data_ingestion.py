import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
from Yes_Bank.entity.config_entity import DataIngestionConfig
from Yes_Bank.entity.artifact_entity import DataIngestionArtifact


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Starting data ingestion")

            # 👉 read dataset
            df = pd.read_csv("C:\ML_YES_BANK\data\data_YesBank_StockPrices.csv")

            logger.info("Dataset loaded")

            # 👉 split
            train_df, test_df = train_test_split(
                df,
                test_size=self.config.test_size,
                random_state=42
            )

            # 👉 create artifacts folder
            os.makedirs("artifacts", exist_ok=True)

            # 👉 save
            train_df.to_csv(self.config.train_path, index=False)
            test_df.to_csv(self.config.test_path, index=False)

            logger.info("Train-test split completed")

            return DataIngestionArtifact(
                train_path=self.config.train_path,
                test_path=self.config.test_path
            )

        except Exception as e:
            raise YesBankException(e, sys)