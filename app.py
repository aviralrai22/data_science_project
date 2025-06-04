from src.DATA_SCIENCE_PROJECT.logger import logging
from src.DATA_SCIENCE_PROJECT.exception import customException
import sys
from src.DATA_SCIENCE_PROJECT.components.data_ingestion import DataIngestionConfig
from src.DATA_SCIENCE_PROJECT.components.data_ingestion import DataIngestion
if __name__=="__main__":
    logging.info("the execution has started")
    
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise customException(e,sys)