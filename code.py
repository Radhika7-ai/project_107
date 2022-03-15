from tkinter import Y
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('data.csv')
#print(df.groupby('level') ['attempt'].mean())

#2.   fig = go.Figure(go.Bar(
   # x = df.groupby('level') ['attempt'].mean() ,
   # y = ['Level 1' , 'Level 2' , 'Level 3' , 'Level 4'] ,
   # orientation = 'h'        
#))

#fig.show()

# 1.   s = df.loc[df['student_id'] == 'TRL_987']
#print(s.groupby('level') ['attempt'].mean())

#f = go.Figure(go.bar(
        #x = s.groupby('level') ['attempt'].mean() ,
       # y = ['level 1' , 'level 2' , 'level 3' , 'level 4'] ,
       # orientation = 'h'
 #))

#f.show()

mean = df.groupby(['student_id' , 'level'] , as_index=False) ['attempt'].mean()
fig = px.scatter(mean , x = 'student_id' , y = 'level' , size = 'attempt' , color = 'attempt')
fig.show()