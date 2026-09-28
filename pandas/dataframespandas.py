import pandas as pd
data ={"reviews" :[" GREAT service ", "Bad item", "Loved IT "],
        "ratings":[5,1,4]
       }
df = pd.DataFrame(data) #You just opened a blank Excel sheet and pasted your data into columns.
df["clean_reviews"] = df["reviews"].str.strip().str.lower() #You created a new Column B and typed a formula at the top to fix Column A.
topreviews = df[df["ratings"] >= 4] # this creates a new dataframe its like selcting ratings column and applying filter

print(topreviews)

