#it is useful for any project 
#run time error can be triggered and tag as an exceptionn and can be stored in the log
#in this project the development will go through the pipelines and it should be registered there in the log
# all the process should be registerd there in the logs of all the processes 
#logger python documentation can be referred as a source
import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #setting the format of the log file
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   # setting the path for the log file in the current working directory
os.makedirs(log_path,exist_ok=True)  #it will make the directory if the folder is not exist

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)  #complete file path of the log
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s",
    level=logging.INFO,
)
#asctime for time... lineno is for line number.... name show filename... levelname logging.INFO... message is the type of mesage want to show
#it is a generic logging code can be used 
