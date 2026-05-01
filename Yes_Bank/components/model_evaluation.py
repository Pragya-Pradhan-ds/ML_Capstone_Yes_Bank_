import sys
import numpy as np

from sklearn.metrics import r2_score, mean_absolute_error

from Yes_Bank.exception.exception import YesBankException
from Yes_Bank.logging import logger
from Yes_Bank.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
)
from Yes_Bank.utils.utils import load_numpy_array_data, load_object


class ModelEvaluation:

    def __init__(
        self,
        transformation_artifact: DataTransformationArtifact,
        trainer_artifact: ModelTrainerArtifact,
    ):
        self.transformation_artifact = transformation_artifact
        self.trainer_artifact = trainer_artifact

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            # Load test data
            test_arr = load_numpy_array_data(
                self.transformation_artifact.transformed_test_path
            )

            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            # Load model
            model = load_object(
                self.trainer_artifact.trained_model_file_path
            )

            # Predict
            y_pred = model.predict(X_test)

            # Metrics
            r2 = r2_score(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)

            logger.info(f"R2 Score: {r2}")
            logger.info(f"MAE: {mae}")

            return ModelEvaluationArtifact(
                r2_score=r2,
                mae=mae
            )

        except Exception as e:
            raise YesBankException(e, sys)