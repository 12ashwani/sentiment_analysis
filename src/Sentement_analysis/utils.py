import os
import sys
import pickle
import pymysql
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from src.Sentement_analysis.exception import CustomException
from src.Sentement_analysis import logger
from sklearn.metrics import r2_score


load_dotenv()
host= os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')


# here we creating a funcction for reading the data from the mysql database 
def read_sql_data():
    logger.logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db

        )
        logger.logging.INFO('Connection stablished')
        df=pd.read_sql_query("select * from 'Table_name' ")
        return df
    except Exception as ex:
        raise CustomException(ex)

