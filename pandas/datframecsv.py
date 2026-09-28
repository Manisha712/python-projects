import pandas as pd

# Load the file into a DataFrame
df = pd.read_csv("products.csv")

# Instantly inspect the first 5 rows
print(df.head())
df["clean_name"]= df["product_name"].str.strip().str.lower()
print(df.head())
expensive_product = df[df["price"]>20]
print(expensive_product)

#Save to a new CSV file
# index=False stops Pandas from adding extra 0,1,2 row numbers into your saved file
expensive_product.to_csv("cleaned_expensive_product.csv", index=False)




