#Merge CSV files from different folders
import os
import pandas as pd
from glob import glob

path = "C:/Users/Nenad/Desktop/Data"
EXT = "data1.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(path)
                 for file in glob(os.path.join(path, EXT))]

for f in all_csv_files:
    df=pd.read_csv(f, header=None)
    print("The number of rows: ",df.shape[0])
    combined_csv_data =pd.concat([pd.read_csv(f, header=None),df])
    combined_csv_data =pd.concat([combined_csv_data,df])
print('\n')
combined_csv_data.to_csv('combined_data.csv')
print("Combined CSV file: ")
print(combined_csv_data)
print("The number of rows is: ",combined_csv_data.shape[0])
print('\n')
exe='combined_data.csv'
print("The path from new file is: ")
print(os.path.abspath(exe))
