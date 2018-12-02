import pandas as pd

df = pd.read_csv("GroupLeader.csv",index_col=0)
for index, row in df.iterrows():
   print (index, row['Grp'], row['Name'])


