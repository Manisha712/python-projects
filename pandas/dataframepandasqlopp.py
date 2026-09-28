import pandas as pd
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
dimonds=pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
#print(dimonds.head())
#print(dimonds[dimonds['cut']=='Ideal'])
#print(dimonds.loc[(dimonds['cut']=='Ideal')&(dimonds['clarity']!='IF')])
#print(dimonds.sort_values('price', ascending=False).head(10)) #df.sort_values(by='column_name', ascending=True)
#.head(10) grabs top 10 rows
Dimondsort=dimonds.groupby(['cut','carat'])['price'].mean().reset_index()
#Take the things currently being used as the index and turn them back into regular columns.
#print(Dimondsort)
#Dimondsort.to_excel(r"C:\Users\manis\OneDrive\Desktop\dimond_sort.xlsx", index=False)
print(dimonds.groupby('cut', as_index=False)['price'].sum())