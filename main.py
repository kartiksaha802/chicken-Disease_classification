
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

try:
    
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    
    
except Exception as e:
    logger.exception(e)
    raise e