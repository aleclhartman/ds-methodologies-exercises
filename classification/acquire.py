import numpy as np
import pandas as pd

from env import get_db_url





titanic_query = """
SELECT *
FROM passengers;
"""
titanic_url = get_db_url("titanic_db")

def get_titanic_data():
    df = pd.read_sql(titanic_query, titanic_url)
    # df.drop(columns=["passenger_id"], inplace=True)
    return df





iris_query = """
SELECT m.measurement_id, m.sepal_length, m.sepal_width, m.petal_length, m.petal_width, m.species_id, s.species_name
FROM measurements AS m
JOIN species AS s ON m.species_id = s.species_id;
"""
iris_url = get_db_url("iris_db")

def get_iris_data():
    df = pd.read_sql(iris_query, iris_url)
    return df
