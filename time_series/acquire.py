import numpy as np
import pandas as pd

import requests

from os import path

def get_items(base_url, api):
    """
    This function does the following:
    1. Looks for an existing items.csv file, reads the csv, and returns a DataFrame
    2. If the file does not exist, the function iterates through the items pages concatenating each page to the existing DataFrame,
        writes the DataFrame to a csv file, and returns a DataFrame
    """
    
    response = requests.get(base_url + api)
    data = response.json()
    df = pd.DataFrame({})

    if path.exists("items.csv"):
        df = pd.read_csv("items.csv", index_col=0)
    else:
        for i in range(1, data["payload"]["max_page"] + 1):
            if data["payload"]["next_page"] != None:
                df = pd.concat([df, pd.DataFrame(data["payload"]["items"])]).reset_index().drop(columns="index")
                response = requests.get(base_url + data["payload"]["next_page"])
                data = response.json()
            else:
                df = pd.concat([df, pd.DataFrame(data["payload"]["items"])]).reset_index().drop(columns="index")
        df.to_csv("items.csv")
    
    return df

def get_stores(base_url, api):
    """
    This function does the following:
    1. Looks for an existing stores.csv file, reads the csv, and returns a DataFrame
    2. If the file does not exist, the function iterates through the stores pages concatenating each page to the existing DataFrame,
        writes the DataFrame to a csv file, and returns a DataFrame
    """
    
    response = requests.get(base_url + api)
    data = response.json()
    df = pd.DataFrame({})

    if path.exists("stores.csv"):
        df = pd.read_csv("stores.csv", index_col=0)
    else:
        for i in range(1, data["payload"]["max_page"] + 1):
            if data["payload"]["next_page"] != None:
                df = pd.concat([df, pd.DataFrame(data["payload"]["stores"])]).reset_index().drop(columns="index")
                response = requests.get(base_url + data["payload"]["next_page"])
                data = response.json()
            else:
                df = pd.concat([df, pd.DataFrame(data["payload"]["stores"])]).reset_index().drop(columns="index")
        df.to_csv("stores.csv")
    
    return df

def get_sales(base_url, api):
    """
    This function does the following:
    1. Looks for an existing sales.csv file, reads the csv, and returns a DataFrame
    2. If the file does not exist, the function iterates through the sales pages concatenating each page to the existing DataFrame,
        writes the DataFrame to a csv file, and returns a DataFrame
    """
    
    response = requests.get(base_url + api)
    data = response.json()
    df = pd.DataFrame({})

    if path.exists("sales.csv"):
        df = pd.read_csv("sales.csv", index_col=0)
    else:
        for i in range(1, data["payload"]["max_page"] + 1):
            if data["payload"]["next_page"] != None:
                df = pd.concat([df, pd.DataFrame(data["payload"]["sales"])]).reset_index().drop(columns="index")
                response = requests.get(base_url + data["payload"]["next_page"])
                data = response.json()
            else:
                df = pd.concat([df, pd.DataFrame(data["payload"]["sales"])]).reset_index().drop(columns="index")
        df.to_csv("sales.csv")
    
    return df

def combine_data(items, stores, sales):
    """
    This function does the following:
    1. Left joins the items DataFrame to the sales DataFrame to create a sales_and_items DataFrame
    2. Left joins the stores DataFrame to the sales_and_items DataFrame to create a master DataFrame
    3. Returns the master DataFrame with all the data from the three originating DataFrames
    """
    
    sales_and_items = pd.merge(sales, items, left_on="item", right_on="item_id", how="left")
    
    master = pd.merge(sales_and_items, stores, left_on="store", right_on="store_id", how="left")
    
    return master

def get_germany():
    """
    This function does the following:
    1. Looks for an existing germany.csv file, reads the csv, and returns a DataFrame
    2. If the file does not exist, the function uses the link variable to get the Open Power Systems Data for Germany, writes the DataFrame to a csv file,
        and returns a DataFrame
    """
    
    link = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    
    if path.exists("germany.csv"):
        df = pd.read_csv("germany.csv", index_col=0)
    else:
        df = pd.read_csv(link)
        df.to_csv("germany.csv")
    
    return df