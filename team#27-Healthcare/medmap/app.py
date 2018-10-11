import os
import sqlite3
from sklearn.cluster import KMeans
from flask import Flask, jsonify
import pandas as pd
import numpy as np


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'test.db'),
)

conn = sqlite3.connect('test.db')
DISEASES = ["dengue", "malaria", "flu", "ebola", "lyphoma"]

df = pd.read_sql_query("SELECT * FROM APP", conn)
df['GEO_LAT'] = pd.to_numeric(df['GEO_LAT'], errors='coerce')
df['GEO_LONG'] = pd.to_numeric(df['GEO_LONG'], errors='coerce')


@app.route('/get_all')
def get_all():
    ret_dict = {}
    for disease in DISEASES:
        data = df[df.DISEASE == disease]
        geo_lat = data['GEO_LAT']
        geo_long = data['GEO_LONG']
        ret_dict[disease] = list(zip(geo_lat, geo_long))
    return jsonify(ret_dict)


def get_center_from_data(disease):
    kmeans = KMeans()
    data = df[df.DISEASE == disease]
    if data.shape[0] == 0:
        return (), ()
    data = data.dropna()
    array = data[['GEO_LAT', 'GEO_LONG']].values
    kmeans.fit(array)
    cent = kmeans.cluster_centers_
    count_list = [len(np.where(kmeans.labels_ == i)[0]) for i in range(kmeans.n_clusters)]
    return cent.tolist(), count_list


@app.route('/get_center')
def get_center():
    ret_dict = {}
    for disease in DISEASES:
        ret_dict[disease] = get_center_from_data(disease)
    ret_dict['status'] = 200
    return jsonify(ret_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
