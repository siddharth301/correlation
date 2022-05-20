import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row['Marks']))
            days_present.append(float(row['Present']))

    return{"x": Marks, "y": Present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'], datasource['y'])
    print("correlation between marks in percentage and days present: /n", correlation[0,1])



def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)


setup()
            
