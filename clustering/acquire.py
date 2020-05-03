import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from os import path

from env import host, user, password

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(user, password, host, dbname)

def get_zillow_data():
    """
    Docstring
    """
    # query zillow data
    zillow_query = """
    SELECT prop.*, pred.logerror, pred.transactiondate, ac.airconditioningdesc, ar.architecturalstyledesc, bu.buildingclassdesc, he.heatingorsystemdesc, la.propertylandusedesc, st.storydesc, co.typeconstructiondesc
    FROM properties_2017 AS prop
    JOIN predictions_2017 AS pred USING(parcelid)
    LEFT JOIN airconditioningtype AS ac USING(airconditioningtypeid)
    LEFT JOIN architecturalstyletype AS ar USING(architecturalstyletypeid)
    LEFT JOIN buildingclasstype AS bu USING(buildingclasstypeid)
    LEFT JOIN heatingorsystemtype AS he USING(heatingorsystemtypeid)
    LEFT JOIN propertylandusetype AS la USING(propertylandusetypeid)
    LEFT JOIN storytype AS st USING(storytypeid)
    LEFT JOIN typeconstructiontype as co USING(typeconstructiontypeid)
    WHERE prop.latitude IS NOT NULL
    AND prop.longitude IS NOT NULL;"""
    
    # get database url
    zillow_url = get_db_url("zillow")
    
    # get pandas to read sql query + db url and return a DataFrame if the .csv of the data doesn't already exist
    if path.exists("zillow_clustering.csv"):
        df = pd.read_csv("zillow_clustering.csv", index_col=0)
    else:
        df = pd.read_sql(zillow_query, zillow_url)
        df.to_csv("zillow_clustering.csv")
    
    return df

def nulls_by_col(df):
    """
    Docstring
    """
    num_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_missing = num_missing / rows
    cols_missing = pd.DataFrame({
        "num_rows_missing": num_missing,
        "pct_rows_missing": pct_missing
    })
    return cols_missing

def nulls_by_row(df):
    """
    Docstring
    """
    num_cols_missing = df.isnull().sum(axis=1)
    pct_cols_missing = df.isnull().sum(axis=1) / df.shape[1]
    rows_missing = pd.DataFrame({
        'num_cols_missing': num_cols_missing,
        'pct_cols_missing': pct_cols_missing
    }).reset_index().groupby(['num_cols_missing','pct_cols_missing']).count().rename(index=str, columns={'index': 'num_rows'}).reset_index()
    return rows_missing