import pandas as pd
df =pd.read_excel(r"C:\Users\manis\OneDrive\Desktop\pandaprac.xlsx")
df.to_csv(r"C:\Users\manis\OneDrive\Desktop\datset1.csv",index=False)
#ndex=False → prevents pandas from adding an extra index column
#r"path"	Raw string → safest for Windows paths
#"path"	Normal string → must escape backslashes
print("original:",df)
print(df.isnull().sum())
dffilled= df.fillna(0)
print(dffilled)
new_df = df[(df['Amount'] > 20) & (df['Region'] == 'North')]
print(new_df)