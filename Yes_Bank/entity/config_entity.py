import os
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_path: str = os.path.join("artifacts", "train.csv")
    test_path: str = os.path.join("artifacts", "test.csv")
    test_size: float = 0.2

@dataclass
class DataTransformationConfig:
    transformed_train_path: str = "artifacts/train.npy"
    transformed_test_path: str = "artifacts/test.npy"
    transformed_object_path: str = "artifacts/preprocessor.pkl"

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = "artifacts/model.pkl"