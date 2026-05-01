import sys
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
from Yes_Bank.entity.config_entity import DataTransformationConfig
from Yes_Bank.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
)
from Yes_Bank.utils.utils import save_object, save_numpy_array_data


class DataTransformation:

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        config: DataTransformationConfig,
    ):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.config = config

    def read_data(self, file_path: str) -> pd.DataFrame:
        try:
            df = pd.read_csv(file_path)
            logger.info(f"Read data from {file_path}")
            return df
        except Exception as e:
            raise YesBankException(e, sys)

    def convert_date_column(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            if "Date" in df.columns:
                df["Date"] = pd.to_datetime(df["Date"], format="%b-%y")
                df["Month"] = df["Date"].dt.month
                df["Year"] = df["Date"].dt.year
                df.drop(columns=["Date"], inplace=True)
                logger.info("Date column converted")
            return df
        except Exception as e:
            raise YesBankException(e, sys)

    def get_preprocessor(self) -> Pipeline:
        try:
            pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy="median"))
            ])
            return pipeline
        except Exception as e:
            raise YesBankException(e, sys)

    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            train_df = self.read_data(self.data_ingestion_artifact.train_path)
            test_df = self.read_data(self.data_ingestion_artifact.test_path)

            train_df = self.convert_date_column(train_df)
            test_df = self.convert_date_column(test_df)

            target_column = "Close"

            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]

            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            preprocessor = self.get_preprocessor()

            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)

            train_arr = np.c_[X_train_transformed, y_train]
            test_arr = np.c_[X_test_transformed, y_test]

            save_numpy_array_data(self.config.transformed_train_path, train_arr)
            save_numpy_array_data(self.config.transformed_test_path, test_arr)

            save_object(self.config.transformed_object_path, preprocessor)

            logger.info("Data Transformation completed")

            return DataTransformationArtifact(
                transformed_train_path=self.config.transformed_train_path,
                transformed_test_path=self.config.transformed_test_path,
                preprocessor_object_path=self.config.transformed_object_path,
            )

        except Exception as e:
            raise YesBankException(e, sys)