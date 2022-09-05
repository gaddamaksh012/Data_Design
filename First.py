import json
import glob
import pandas as pd
import numpy as np
from datetime import datetime
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
import os

# Extraction phase  

traget_file = "Target_file2.csv"

def csv_read(file_to_read):
    dataframe = pd.read_csv(file_to_read)
    return dataframe

def json_read(file_to_read):
    dataframe = pd.read_json(file_to_read,lines = True)
    return dataframe

def xml_read(file_to_read):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_to_read)
    root = tree.getroot()
    for name in root:
        car_model = name.find("car_model").text
        year_of_manufacture = int(name.find("year_of_manufacture").text)
        price = float(name.find("price").text)
        fuel = name.find("fuel").text
        dataframe = dataframe.append({"car_model":car_model,"year_of_manufacture":year_of_manufacture,"price":price,"fuel":fuel},ignore_index=True)

    return dataframe

try:

    def exicutes():

        global extracted_file
        extracted_file = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])

        for file in glob.glob("C:/Users/GAKASH/Downloads/data/datasource (1)/*.csv"):
            extracted_file = pd.concat([extracted_file, csv_read(file)],ignore_index=True)

        for file in glob.glob("C:/Users/GAKASH/Downloads/data/datasource (1)/*.json"):
            extracted_file = pd.concat([extracted_file,json_read(file)],ignore_index=True)

        for file in glob.glob("C:/Users/GAKASH/Downloads/data/datasource (1)/*.xml"):
            extracted_file = pd.concat([extracted_file, xml_read(file)],ignore_index=True)

        print(extracted_file)

    exicutes()

except Exception as e:
    print("error is {}".format(e))

#Transforming Phase

def trans(data):
    data.price = round(data.price,2)
    return data

# Loading Phase

def Loading(traget_file,extracted_file):
    extracted_file.to_csv(traget_file)

# logging gphase
def logging(message):
    timestamps = '%H:%M:%S-%h-%d-%Y' #Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now()
    timestamp = now.strftime(timestamps)

    with open("logfile.txt","a") as f:
        f.write(timestamp+','+message+'\n')



logging("ETL Process starts from here : ")

logging("Extraction phase start here: ")

exicutes()

logging("Extraction phase ends here: ")

logging("Transforamation phase starts here")

trans(extracted_file)

logging("Transforamation phase ends here")

logging("Loading process starts here")

Loading(traget_file,extracted_file)

logging("Loading process ends here")