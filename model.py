import os
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,normalize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import matplotlib.pyplot as plt
df=pd.read_csv('matches.csv',header=0)

##df=pd.DataFrame(data)
##print(df)
##df.dropna(inplace=True)
df=df.drop(['id','Season','date','dl_applied','win_by_runs',
           'win_by_wickets','player_of_match','venue','umpire1','umpire2',
           'umpire3','result'],axis=1)
df.dropna(inplace=True)
##print('df',df)
df=df.reset_index()
x=df.drop(['index','winner'],axis=1)
y_series=df['winner']
y=pd.DataFrame(y_series)
##print(x.columns,x.iloc[2])
##print(y.head())
##print(y.columns)
df2=pd.read_csv('teams.csv',header=0)
##df2=pd.DataFrame(data2)
df3=pd.read_csv('team_average.csv',header=0)
##df3=pd.DataFrame(data3)
df3=df3[['team','home_win_percentage','away_win_percentage']]
##print(x.columns)
##print(df2.columns)
##for team1 in x.iloc[0]:
##    print(team1)
##for i in x:
##print(x.iloc[0][0])
##print(x.iloc[0]['city'])
##print(df2['team1'])
x[['team1_home','team2_home','team1_toss_win','team1_bat',
   'team1_win_percentage','team2_win_percentage']]=None
y[['team1_win']]=None
##print(x.columns)
##print(x[['team1','team2']].head())
##print(y)
x=x.replace('Rising Pune Supergiant','Rising Pune Supergiants')
y=y.replace('Rising Pune Supergiant','Rising Puzne Supergiants')
labelenc_x=LabelEncoder()

##x['toss_decision']=labelenc_x.fit_transform(x['toss_decision'])
y['winner']=labelenc_x.fit_transform(y['winner'])
##x.rename(columns={'toss_winner':'team1_toss_win','toss_decision':'team1_bat'},
##         inplace=True)
##y.rename(columns={'winner':'team1_win'},inplace=True)
##print(x)
##print(y)
##print(x.columns)
##print(y.columns)
##print(x.iloc[3])
for i in x.index:
    if x.iloc[i][1]==x.iloc[i][3]:
        x.iat[i,7]=1
    else:
        x.iat[i,7]=0
    if (x.iloc[i][7]==0 and x.iloc[i][4]=='field') or \
       (x.iloc[i][7]==1 and x.iloc[i][3]=='bat'):
        x.iat[i,8]=1
    else:
        x.iat[i,8]=0
##for i in range(2):
##    for x.iloc[i][0] in x.iloc[i]:
##        if x.iloc[i][0]==df2['team1']['home
    city=str(x.iloc[i][0])
    team1=x.iloc[i][1]
##    print(type(city),type(team1))
##    print(type(df2.iloc[0][0]),type(df2.iloc[1][0]))
##    print(city,team1)
    for j in df2.index:
        if ((df2.iloc[j][0] == team1) and (city in df2.iloc[j][1])):
##            x.iloc[i][7],x.iloc[i][8]=1,0
            x.iat[i,5]=1
            x.iat[i,6]=0
            break
        if ((df2.iloc[j][0] == team1) and (city not in df2.iloc[j][1])):
##            x.iloc[i][7],x.iloc[i][8]=0,1
            x.iat[i,5]=0
            x.iat[i,6]=1
            break
x[['team1_home']]=x[['team1_home']].fillna(0)
##    x.x[[7]].fillna(value=np.nan, inplace=True)
x[['team2_home']]=x[['team2_home']].fillna(0)
x['toss_winner']=labelenc_x.fit_transform(x['toss_winner'])
x['team1']=labelenc_x.fit_transform(x['team1'])
x['team2']=labelenc_x.fit_transform(x['team2'])
df3['team']=labelenc_x.fit_transform(df3['team'])
##print(x[['team1','team2']].head())
##print(df.team)
x=x.drop(['city','toss_winner','toss_decision','team2_home'],axis=1)
##for i in x.index:
##    if x.iloc[i][0]==x.iloc[i][2]:
##        x.iat[i,2]=1
##    else:
##        x.iat[i,2]=0
##    if (x.iloc[i][2]=='0' and x.iloc[i][3]=='field') or\
##    (x.iloc[i][2]=='1' and x.iloc[i][3]=='bat'):
##        x.iat[i,3]=1
##    else:
##        x.iat[i,3]=0
##print(x)
##print(x.iloc[3])
##print(y)
##print(x.columns)
##print(y.columns)
for i in x.index:
    team1,team2=x.iloc[i][0],x.iloc[i][1]
    if x.iloc[i][2]==1:
        for j in df3.index:
            if df3.iloc[j][0]==team1:
                x.iat[i,5]=df3.iloc[j][1]
            if df3.iloc[j][0]==team2:
                x.iat[i,6]=df3.iloc[j][2]
    else:
        for j in df3.index:
            if df3.iloc[j][0]==team1:
                x.iat[i,5]=df3.iloc[j][2]
            if df3.iloc[j][0]==team2:
                x.iat[i,6]=df3.iloc[j][1]
    if y.iloc[i][0]==team1:
        y.iat[i,1]=1
    else:
        y.iat[i,1]=0
y.drop(['winner'],axis=1,inplace=True)
##y=pd.Series(y[:])                
z=x[['team1']]
onehotencoder_x=OneHotEncoder()
z=onehotencoder_x.fit_transform(z).toarray()

z=pd.DataFrame(z,dtype=np.int64)
for i in x.index:
    team2=x.iloc[i][1]
    z.iat[i,team2]=1
z.rename(columns={0:'csk',1:'dch',2:'dca',3:'dd',4:'gl',5:'kxip',6:'kt',
                  7:'kkr',8:'mi',9:'pw',10:'rr',11:'rps',12:'rcb',13:'srh'},
         inplace=True)
x=x.join(z)
a=normalize(x[['team1_win_percentage','team2_win_percentage']])
a=pd.DataFrame(a)
a.rename(columns={0:'team1_win_percentage',1:'team2_win_percentage'},
         inplace=True)
x=x.drop(['team1','team2','team1_win_percentage','team2_win_percentage',
          'team1_toss_win'],axis=1)
x=x.join(a)
y=pd.DataFrame(y,dtype=np.int64)
y=y['team1_win']
z=x.join(y)
z.to_csv('data.csv')
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,
                                               random_state=200)
#model1:logistic Regression

log_model=LogisticRegression()
log_model.fit(x_train,y_train)
acc=0
predictions=log_model.predict((x_test.iloc[0]).values.reshape(1,-1))
##for c,p in enumerate(predictions,start=1):
##    if p == y_test[c]:
##        acc+=1
acc=acc/len(y_test)
##score_log_model = log_model.score(x_test, y_test)
##logmodel_file='logmodel.sav'
##pickle.dump(log_model,open(logmodel_file,'wb'))
##logmod=pickle.load(open('logmodel.sav','rb'))
##print(logmod.score(x_test, y_test))
#model2: svm

svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train, y_train)
##predictions=svclassifier.predict((x_test.iloc[180]).values.reshape(1,-1))
##y_pred=svclassifier.predict(x_test)
##score_svm=svclassifier.score(x_test,y_test)
svmodel_file='svmmodel.sav'
pickle.dump(svclassifier,open(svmodel_file,'wb'))
##plt.scatter(x,)
##plt.show()
#################################################################
##class MyModel:
##    def __init__(self,option=1):
##        self.option=option
##    def 
