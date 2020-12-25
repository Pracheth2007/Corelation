import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path) :
    ice_cream_sales=[]
    cold_drink_sales=[] 
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Size of TV"]))
            cold_drink_sales.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x" : ice_cream_sales, "y" : cold_drink_sales}

def findCorelation(datasource):
    corelation = np.corrcoef(datasource["x"],datasource["y"])    
    print("corelation between Size of TV and Average time spent watching TV in a week (hours)",corelation[0,1])

def setup():
    data_path = "tV.csv"
    datasource = getDataSource(data_path)
    findCorelation(datasource)
setup()