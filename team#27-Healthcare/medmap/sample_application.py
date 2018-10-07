import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from app import get_center_from_data

conn = sqlite3.connect('test.db')
DISEASES = ["dengue", "malaria", "flu", "ebola", "lyphoma"]

df = pd.read_sql_query("SELECT * FROM APP", conn)
df['GEO_LAT'] = pd.to_numeric(df['GEO_LAT'], errors='coerce')
df['GEO_LONG'] = pd.to_numeric(df['GEO_LONG'], errors='coerce')


flu_data = df[df.DISEASE == "flu"]
ebola_data = df[df.DISEASE == "ebola"]
dengue_data = df[df.DISEASE == 'dengue']
malaria_data = df[df.DISEASE == 'malaria']

flu_centers, flu_count = get_center_from_data("flu")
ebola_centers, ebola_count = get_center_from_data("ebola")
dengue_centers, dengue_count = get_center_from_data("dengue")
malaria_centers, malaria_count = get_center_from_data("malaria")


plt.scatter(flu_data['GEO_LAT'], flu_data['GEO_LONG'])
plt.scatter(ebola_data['GEO_LAT'], ebola_data['GEO_LONG'])
plt.scatter(dengue_data['GEO_LAT'], dengue_data['GEO_LONG'])
plt.scatter(malaria_data['GEO_LAT'], malaria_data['GEO_LONG'])

for i, flu_center in enumerate(flu_centers):
    if flu_count[i] > 10:
        plt.scatter(flu_center[0], flu_center[1], marker='x', c='k')
for i, ebola_center in enumerate(ebola_centers):
    if ebola_count[i] > 5:
        plt.scatter(ebola_center[0], ebola_center[1], marker='+', c='k')
for i, dengue_center in enumerate(dengue_centers):
    if dengue_count[i] > 5:
        plt.scatter(dengue_center[0], dengue_center[1], marker='>', c='k')
for i, malaria_center in enumerate(malaria_centers):
    if malaria_count[i] > 5:
        plt.scatter(malaria_center[0], malaria_center[1], marker='<', c='k')

plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.legend(('Flu', 'Ebola', 'Dengue ', 'Malaria'))
plt.title('x: Flu centers +: Ebola centers >: Dengue centers <: Malaria centers')
plt.show()
conn.close()
