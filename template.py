#this file is used to make the required files with all the components of the project 
#this file is useful when there is need of multiple file for the project and you want to setup the files and make the files automatically 
#this may be done with cookie cutter but here we are going to do it manually


import os
#os gives us the generic path of the current working directory
from pathlib import  Path
import logging
logging.basicConfig(level=logging.INFO) #gives the generic info
project_name="DATA_SCIENCE_PROJECT"
list_of_file=[
   # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",#to make it package use init
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    'app.py','dockerfile',
#all these files are needed for this project

]

for filepath in list_of_file:
    filepath=Path(filepath)  #path of the files of the list given above
    filedir,filename=os.path.split(filepath) #split the path into the dir and the file name 
    if filedir != "":  # if the file is not present then it will make one 
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'creating directory:{filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  #if the file size is 0 and the path  not exists then it will open the file even it wil create and open the file
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}')
    else:
        logging.info(f'{filename} is already exists')