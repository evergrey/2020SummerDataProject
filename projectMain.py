# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os

def debugInfoBasic():
    #list CSVs in our input folder
    print(os.listdir("../input"))

#nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")
vg_data = pd.read_csv("../input/videogamesales/vgsales.csv")



class dataLoader:
    my_csv = None

    def __init__(self, csv_file):
        
        #check csv exists
        if(os.path.isfile(csv_file)):
            print("file found... loading")
            #load into pandas DataFrame
            self.my_csv = pd.read_csv(csv_file)
            print("loading complete")
        else:
            print("csv load failed... exiting")
            exit()
            
    def data_test(self):
        # look at a few rows of the nfl_data file. I can see a handful of missing data already!
        print(self.my_csv.sample(5))
        # get the number of missing data points per column
        missing_values_count = self.my_csv.isnull().sum()
        # look at the # of missing points in the first ten columns
        missing_values_count[0:10]
        for i in range(1,10):
            print("Missing values" + str(i) + ":" + str(missing_values_count[i]))

    #https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan        
    def filterEssentialColumnsNonNull(self,nonNullColumnList):
        
        for columnName in nonNullColumnList:
            #take only rows where specified column is not NA
            self.my_csv = self.my_csv[self.my_csv[columnName].notna()]


test0 = dataLoader("../input/videogamesales/vgsales.csv")
nonNullList = [ "Name", "Platform", "Year" ]
test0.filterEssentialColumnsNonNull(nonNullList)
test0.data_test()

#debugInfoBasic()
#data_test(vg_data)
