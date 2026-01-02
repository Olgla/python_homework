import pandas as pd
import numpy as np
import json


#Task 1: Handling Missing Data
df = pd.read_csv("fake_data.csv")
#print(df)

df1 = df.dropna()
# print((df).info)
# print((df1).info)

df1 = df.fillna({'Name': 'Unknown', 
                 'Age': df['Age'].mean(), 
                 'Salary': df['Salary'].mean(), 
                 'Join Date': '2020-01-01'})

df2 = df1.dropna().reset_index(drop=True)
df2['Age'] = df2['Age'].astype(int)
#print(df2)


#Task 3: Validating Data Ranges
df2['Age'] = df2['Age'].apply(lambda age: age if age >18 and age <65 else np.nan)
#print(df2)
df2['Age'] = df2['Age'].fillna(df2["Age"].median())
#print(df2)


#Task 2: Data Transformation
df3 = pd.read_csv("eclipses.csv", sep = '|')
# print(df3.info(), df3.head(5))
df3["Date"] = pd.to_datetime(df3["Date"], errors='coerce')
#print(df3.head(20))


#Task 4: Removing Duplicates & Outliers
#df3.info()
duplicate_series = df3.duplicated()
#print(df3)
#print(duplicate_series[duplicate_series == True].head(10))
#print(duplicate_series.value_counts())

df3 = df3.drop_duplicates().reset_index(drop = True)
#df3.info()

#1
# df2['Age'] = df2['Age'].apply(lambda age: age if age >0 and age <100 else None)
# #print(df2)
# df2['Age'] = df2['Age'].fillna(df2["Age"].median())
# #print(df2)


#Task 5: Standardizing Data
df2['Name'] = df2['Name'].str.lower().str.strip()
#print(df2)

print(df2.groupby('City').agg({'Name': 'count'}))
df2['City'] = df2['City'].replace({'LA': 'Los Angeles', 
                                   'NY': "New York",
                                   'NYC': "New York",
                                   'New York City': "New York"})
#print(df2)


#Task 6 — Encoding Categorical Variables
df4 = pd.DataFrame({'Color': ['Red','Blue','Green','Blue']})
df4["Color_Label"] = df4["Color"].map({"Red":1,"Blue":2,"Green":3})
df_encoded = pd.get_dummies(df4["Color"], prefix="Color")
#print(df4)


#Task 7 — Consolidating Messy Files (Mini Project)
d0 = pd.read_csv("name_and_address_0.csv")
d1 = pd.read_csv("name_and_address_1.csv")
d2 = pd.read_csv("name_and_address_2.csv")
d3 = pd.read_csv("name_and_address_3.csv")

df_all = pd.concat([d0, d1, d2, d3], ignore_index = True)
#print(df_all)

# try:
#     from thefuzz import process
# except ImportError:
#     raise ImportError("Please install thefuzz: pip install thefuzz")

# df_names = df_all.value_counts("Name")
# good_names = list(df_names[df_names > 2].index)
# df_all["Name"] = df_all["Name"].map(
#        lambda x: x if x in good_names else process.extractOne(x, good_names)[0]
#    )

# df_addresses = df_all.value_counts("Name")
# good_addresses = list(df_addresses[df_addresses > 2].index)
# df_all["Address"] = df_all["Address"].map(
#        lambda x: x if x in good_addresses else process.extractOne(x, good_addresses)[0]
#    )

# def fix_anomaly(group):
#        group_na = group.dropna()
#        if group_na.empty:
#            return group
#        mode = group_na.mode()
#        if mode.empty:
#            return group
#        return mode.iloc[0]

# df_all["Zip"] = df_all.groupby(["Name","Address"])["Zip"].transform(fix_anomaly)
# df_all["Phone"] = df_all.groupby(["Name","Address"])["Phone"].transform(fix_anomaly)

# df_all.drop_duplicates().reset_index(drop = True)
# print(df_all.info)


#Task 8 — Regular Expressions for Validation
log_entries = pd.Series([
       "[2023-10-26 10:00:00] INFO: User logged in",
       "[2023-10-26 10:05:30] WARNING: Invalid input",
       "[2023-10-26 10:10:15] ERROR: Database connection failed"
   ])
extracted_logs = log_entries.str.extract(r"\[(.*?)\]\s(\w+):\s(.*)")

text_data = pd.Series([
       "Value is {amount}.",
       "The price is [value].",
       "Cost: (number)",
       "Quantity = <qty>"
   ])
standardized_text = text_data.replace(
       [r"\{.*?\}", r"\[.*?\]", r"\(.*?\)", r"\<.*?\>"],
       "<VALUE>",
       regex=True,
   )

df = pd.DataFrame({
       "order_id":[1,2],
       "created_at":["2021-01-05","2021-01-06"],
       "updated_at":["2021-01-07","2021-01-08"]
   })
time_cols = df.filter(regex="_at$")

orders = pd.Series([
       "Order #123 has been shipped on 2021-01-05",
       "Order #124 has been cancelled",
       "Shipment #125 confirmed on 02/06/2021"
   ])
shipped_orders = orders[orders.str.contains("ship", case=False)]


#Task 9 — Reflection & Validation
# - **Missing values**: Many rows had missing 
# - **Duplicates**: Duplicate rows
# - **Invalid data**

#Task 10: Start Your Final Project
df = pd.read_csv("../csv/tmdb_5000_movies.csv")
print(", ".join(df.columns))
df = df.drop_duplicates()

df = df.replace(["", "None", "none", "null", "NULL", "N/A", "n/a"], pd.NA)
# print(df)

df['release_date'] = pd.to_datetime(df['release_date'], errors = 'coerce')
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)
df["budget"] = pd.to_numeric(df["budget"], errors="coerce").fillna(0)


#**Changed release date to date format
#**Converted numbers to numeric type

json_columns = [
    "genres",
    "keywords",
    "production_companies",
    "production_countries",
    "spoken_languages",  
]

for col in json_columns:
    df[col] = df[col].apply(
        lambda x: json.loads(x) if pd.notna(x) else []
    )


text_columns = [
    "title", "original_title", "overview",
    "tagline", "status", "original_language"
]

for col in text_columns:
    df[col] = df[col].str.strip()


genres = []
df.apply(
    lambda row: genres.extend(
        [{'movie_id': row['id'], 'genre': g['name']} for g in row['genres']]
    ),
    axis=1
)
genres_df = pd.DataFrame(genres)
print(genres_df)


companies = []
df.apply(
    lambda row: companies.extend(
        [{'movie_id': row['id'], 'company': c['name']} for c in row['production_companies']]
    ),
    axis=1
)

companies_df = pd.DataFrame(companies)


# Profit
df["profit"] = df["revenue"] - df["budget"]

# Return on Investment
df["roi"] = np.where(
    df["budget"] > 0,
    df["profit"] / df["budget"],
    np.nan
)

# Release year
df["release_year"] = df["release_date"].dt.year

genres = []

df.apply(
    lambda row: genres.extend(
        {
            "movie_id": row["id"],
            "genre": g["name"],
            "revenue": row["revenue"],
            "budget": row["budget"],
            "profit": row["profit"],
            "vote_average": row["vote_average"],
            "vote_count": row["vote_count"]
        }
        for g in row["genres"]
    ),
    axis=1
)

genres_df = pd.DataFrame(genres)


genre_revenue = (genres_df.groupby("genre")["revenue"]
                 .mean()
                 .sort_values(ascending=False)
)

genre_roi = (genres_df.groupby("genre")["profit"]
             .sum()
             /genres_df.groupby("genre")["budget"].sum()
             ).sort_values(ascending=False)

genre_popularity = (genres_df.groupby("genre")["vote_count"]
                    .sum()
                    .sort_values(ascending=False)
)
