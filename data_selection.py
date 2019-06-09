import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('IMU_Mega.csv')

nintyDegree = []
zeroDegree = []
for i in range(0,275):
    if df.iloc[i][3]<=7.5 and df.iloc[i][3]>=6:
        nintyDegree.append(i)
    elif df.iloc[i][3]<=0 and df.iloc[i][3]>=-2:
        zeroDegree.append(i)

x=len(nintyDegree)
for i in range(1,x-1):
    if nintyDegree[i+1]-nintyDegree[i]<5:
        nintyDegree.pop(i)