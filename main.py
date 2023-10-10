from cnnClassifier.utils.common import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline





STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    stage_obj = DataIngestionTrainingPipeline()
    stage_obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e
