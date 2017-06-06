# Hello World program in Python
    
import pandas as pd
train=pd.read_csv('Features32.csv')

df1=pd.DataFrame({'s1':train.iloc[:,11], 's2':train.iloc[:, -1]})
print(df1.corr('kendall'))