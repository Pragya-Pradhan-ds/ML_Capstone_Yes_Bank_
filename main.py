from Yes_Bank.components.data_ingestion import DataIngestion
from Yes_Bank.components.data_transformation import DataTransformation
from Yes_Bank.components.model_trainer import ModelTrainer

from Yes_Bank.entity.config_entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)

print("Starting Pipeline")

# 🔹 STEP 1: INGESTION
ingestion = DataIngestion(DataIngestionConfig())
ingestion_artifact = ingestion.initiate_data_ingestion()
print("Ingestion Done")

# 🔹 STEP 2: TRANSFORMATION
transformation = DataTransformation(
    ingestion_artifact,
    DataTransformationConfig()
)

transformation_artifact = transformation.initiate_data_transformation()
print("Transformation Done")

# 🔹 STEP 3: MODEL TRAINING
trainer = ModelTrainer(
    transformation_artifact,
    ModelTrainerConfig()
)

trainer_artifact = trainer.initiate_model_trainer()
print("Model Training Done")

print("Model saved at:", trainer_artifact.trained_model_file_path)

from Yes_Bank.components.model_evaluation import ModelEvaluation

# 🔹 STEP 4: EVALUATION
evaluation = ModelEvaluation(
    transformation_artifact,
    trainer_artifact
)

evaluation_artifact = evaluation.initiate_model_evaluation()

print("Model Evaluation Done")
print("R2 Score:", evaluation_artifact.r2_score)
print("MAE:", evaluation_artifact.mae)

from Yes_Bank.pipeline.prediction_pipeline import PredictionPipeline
from Yes_Bank.pipeline.input_data import CustomData

print("Testing Prediction Pipeline")

data = CustomData(
    Date="Dec-20",
    Open=100,
    High=110,
    Low=95
)

df = data.get_data_as_dataframe()

pipeline = PredictionPipeline()
prediction = pipeline.predict(df)

print("Predicted Close Price:", prediction)