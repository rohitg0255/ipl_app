import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
z=pd.read_csv(r'D:\sem7\bda\ipl_app\data.csv')
x=z.drop(['Unnamed: 0','team1_win'],axis=1)
y=z.team1_win
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,
                                               random_state=200)
svcmod=pickle.load(open('svmmodel.sav','rb'))
##print(logmod.score(x_test,y_test))
##('svmmodel.sav').close()
predictions=svcmod.predict(x_test.iloc[10].values.reshape(1,-1))
