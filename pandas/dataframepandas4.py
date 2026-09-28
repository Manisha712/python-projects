#
import pandas as pd
df =pd.read_excel(r"C:\Users\manis\OneDrive\Desktop\pandaprac.xlsx")
df.to_csv(r"C:\Users\manis\OneDrive\Desktop\datset.csv",index=False)
#ndex=False → prevents pandas from adding an extra index column
#r"path"	Raw string → safest for Windows paths
#"path"	Normal string → must escape backslashes
print("original:",df)
print(df.isnull().sum())  # shows count of missing values per column
#df_cleaned = df.dropna()  # removes rows with any missing value
#print("AFTER DROPNA",df_cleaned)
df_slectiveclening =df.dropna(subset=['Discount'])
print(df_slectiveclening)
df_filled = df.fillna(0)
print(df_filled)
df["Amount"] = df["Amount"].fillna(df["Amount"].mean())
print(df["Amount"])
df.drop_duplicates(subset=['Customer'], inplace=True)
df_filled.to_csv(r"C:\Users\manis\OneDrive\Desktop\cleaned_sales.csv", index=False)


