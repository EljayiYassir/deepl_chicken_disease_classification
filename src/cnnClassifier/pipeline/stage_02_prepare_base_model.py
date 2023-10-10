from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier.utils.common import logger




STAGE_NAME = 'Prepare base model stage'


class PrepareBaseModelPipeline():
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        prepare_base_model = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()





if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        stage_obj = PrepareBaseModelPipeline()
        stage_obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e

