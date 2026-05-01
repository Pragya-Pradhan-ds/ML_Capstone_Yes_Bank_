from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_path: str
    test_path: str

@dataclass
class DataTransformationArtifact:
    transformed_train_path: str
    transformed_test_path: str
    preprocessor_object_path: str

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str

from dataclasses import dataclass

@dataclass
class ModelEvaluationArtifact:
    r2_score: float
    mae: float