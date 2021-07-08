##import pandas as pd
##import numpy as np
##file=pd.read_csv("ground.csv")
##index=len(file)
##j=[['venue','counts']]
##for i in range(index):
##    j.append([file.iloc[i].values])
##for i in file.values:
##    j=np.append(j,i)
import csv
j=''
with open('ground.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        j+=''
