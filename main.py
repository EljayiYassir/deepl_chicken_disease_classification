from cnnClassifier.utils.common import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline




STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    stage_obj = DataIngestionTrainingPipeline()
    stage_obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Prepare base model stage'

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    stage_obj = PrepareBaseModelPipeline()
    stage_obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Training stage'

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    stage_obj = TrainingPipeline()
    stage_obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e