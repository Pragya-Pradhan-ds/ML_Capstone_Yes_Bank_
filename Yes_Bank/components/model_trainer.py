import sys
import numpy as np

from sklearn.linear_model import LinearRegression

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
from Yes_Bank.entity.config_entity import ModelTrainerConfig
from Yes_Bank.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
)
from Yes_Bank.utils.utils import load_numpy_array_data, save_object


class ModelTrainer:

    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        config: ModelTrainerConfig,
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.config = config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_arr = load_numpy_array_data(
                self.data_transformation_artifact.transformed_train_path
            )

            test_arr = load_numpy_array_data(
                self.data_transformation_artifact.transformed_test_path
            )

            # Split input/output
            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            logger.info("Training model started")

            model = LinearRegression()
            model.fit(X_train, y_train)

            logger.info("Model training completed")

            save_object(self.config.trained_model_file_path, model)

            return ModelTrainerArtifact(
                trained_model_file_path=self.config.trained_model_file_path
            )

        except Exception as e:
            raise YesBankException(e, sys)