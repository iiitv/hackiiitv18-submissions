import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect('test.db')
print("Opened database successfully")
DISEASES = ["dengue", "malaria", "flu", "ebola", "lyphoma"]

df = pd.read_sql_query("SELECT * FROM APP", conn)
df['GEO_LAT'] = pd.to_numeric(df['GEO_LAT'], errors='coerce')
df['GEO_LONG'] = pd.to_numeric(df['GEO_LONG'], errors='coerce')

print(df.shape)
fig, ax = plt.subplots()
df['DISEASE'].value_counts().plot(ax=ax, kind='bar')
plt.show()

flu_data = df[df.DISEASE == "flu"]
ebola_data = df[df.DISEASE == "ebola"]
dengue_data = df[df.DISEASE == 'dengue']
malaria_data = df[df.DISEASE == 'malaria']
plt.scatter(flu_data['GEO_LAT'], flu_data['GEO_LONG'])
plt.scatter(ebola_data['GEO_LAT'], ebola_data['GEO_LONG'])
plt.scatter(dengue_data['GEO_LAT'], dengue_data['GEO_LONG'])
plt.scatter(malaria_data['GEO_LAT'], malaria_data['GEO_LONG'])
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.show()
conn.close()
