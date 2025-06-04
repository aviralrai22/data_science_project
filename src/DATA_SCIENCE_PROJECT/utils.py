import os
import sys
from src.DATA_SCIENCE_PROJECT.exception import customException
from src.DATA_SCIENCE_PROJECT.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv("db")
def read_sql_data():
    logging.info("reading sql database started")
    try:
        #trying to establish the connection to the database
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        logging.info("connection established",mydb)
        #reading the csv file student table
        df=pd.read_sql_query('select * from student',mydb)
        print(df.head())
        return df
    except Exception as e:
        raise customException(e)