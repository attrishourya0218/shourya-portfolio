print("Swiggy Sales Analysis Project Started!")

from calendar import month

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("swiggy_data.xlsx")
print(df.head())

print(df.shape)
print(df.columns)
print(df.info())

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())

total_records=len(df)
print("\nTotal Records:",total_records)

average_price=df["Price (INR)"].mean()
round(average_price, 2)

average_rating=df["Rating"].mean()
print("\nAverage_rating:",round(average_rating,2))

total_ratings=df["Rating Count"].sum()
print("\nTotal Rating Count:",total_ratings)

category_count=df["Category"].value_counts()
print("\n========== CATEGORY COUNT=========")
print(category_count)

category_count.head(10).plot(kind="bar",figsize=(10,5))
plt.title("Top Food Categories")
plt.xlabel("Category")
plt.ylabel("Number of Dishes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

location_count=df["Location"].value_counts()
print("\n========== TOP LOCATIONS ==========")
print(location_count.head(10))

location_count.head(10).plot(kind="bar",figsize=(10,5))
plt.title("Top 10 Locations")
plt.xlabel("Location")
plt.ylabel("Number of Dishes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

category_price=df.groupby("Category")["Price (INR)"].mean().sort_values(ascending=False)
print("\n========== AVERAGE PRICE BY CATEGORY ==========")
print(category_price)

category_price.head(10).plot(kind="bar",figsize=(10,5))
plt.title("Top 10 Categories by Average Price")
plt.xlabel("Category")
plt.ylabel("Average Price (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


top_rated_dishes=df.sort_values(by="Rating",ascending=False).head(10)
print("\n========== TOP 10 RATED DISHES ==========")
print(top_rated_dishes[["Dish Name","Rating","Rating Count"]])


plt.figure(figsize=(10,5))
plt.hist(df["Price (INR)"].dropna(),bins=30)
plt.title("Price Distribution")
plt.xlabel("Price (INR)") 
plt.ylabel("Number of Dishes")
plt.tight_layout()
plt.show()


print("\n============================================")
print("Swiggy Sales Analysis Project Completed!")
print("============================================")


location_count=df["Location"].value_counts()
print("\n========== TOP LOCATIONS ==========")
print(location_count.head(10))

location_count.head(10).plot(kind="bar",figsize=(10,5))
plt.title("Top 10 Locations")
plt.xlabel("Location")
plt.ylabel("Number of Dishes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.columns = df.columns.str.strip()

print("\nCleaned column names:")
print(df.columns.tolist())

print("\nUnique values in each column:")
for column in df.columns:
    print("\n",column)
    print(df[column].unique()[:20])

    print("\nData types:")
    print(df.dtypes)


# Totle number of records
total_records = len(df)
print("/nTotal Records:",total_records)


plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()