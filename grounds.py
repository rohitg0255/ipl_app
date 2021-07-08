##import pandas as pd
##import numpy as np
##df=pd.read_csv('matches.csv')
##ground_stats=df[['venue']].value_counts().\
##              to_frame()
##ground_stats.reset_index(level=0,inplace=True)
##ground_stats=ground_stats.rename(columns=\
##                            {0:'count'})
##x=ground_stats[['venue']]
##y=ground_stats[['count']]
##ground_stats.to_csv('ground.csv',index=False)
##df2=pd.read_csv('static/js/ground.csv')
##df2.to_json('ground.json')
import csv,json
j = []
with open('ground.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            j.append(row)
k=json.dumps(j)
