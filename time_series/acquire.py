import numpy as np
import pandas as pd

import requests

from os import path

def get_df(name):
    """
    This function does the following:
    1a. Looks for an existing items, stores, or sales .csv file.
        1b. If the .csv file exists it reads the .csv and returns a DataFrame
    2. If the file does not exist, the function iterates through the pages for items, stores, or sales concatenating each page to the existing DataFrame,
        writes the DataFrame to a csv file, and returns a DataFrame
    """
    
    # variables
    base_url = "https://python.zach.lol"
    api_url = base_url + "/api/v1/"
    response = requests.get(api_url + name)
    data = response.json()
    df = pd.DataFrame(data["payload"][name])

    # conditional based on existence of .csv file
    if path.exists(name + ".csv"):
        # read .csv if the file exists
        df = pd.read_csv(name + ".csv", index_col=0)
    else:
        # iterate through pages and concatenate data if .csv does not exist
        while data["payload"]["next_page"] != None:
            response = requests.get(base_url + data["payload"]["next_page"])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data["payload"][name])]).reset_index().drop(columns="index")

        # write DataFrame to .csv
        df.to_csv(name + ".csv")
    
    return df

def combine_data():
    """
    This function does the following:
    1. Left joins the items DataFrame to the sales DataFrame to create a sales_and_items DataFrame
    2. Left joins the stores DataFrame to the sales_and_items DataFrame to create a master DataFrame
    3. Returns the master DataFrame with all the data from the three originating DataFrames
    """
    
    # conditional based on existence of .csv file
    if path.exists("items.csv"):
        # read .csv if the file exists
        items = pd.read_csv("items.csv", index_col=0)
    else:
        # else call get_df function
        items = get_df("items")

    if path.exists("stores.csv"):
        # read .csv if the file exists
        stores = pd.read_csv("stores.csv", index_col=0)
    else:
        # else call get_df function
        stores = get_df("stores")

    if path.exists("sales.csv"):
        # read .csv if the file exists
        sales = pd.read_csv("sales.csv", index_col=0)
    else:
        # else call get_df function
        sales = get_df("sales")

    if path.exists("master.csv"):
        # read .csv if the file exists
        df = pd.read_csv("master.csv", index_col=0)
    else:
        # merge .csv files if the master.csv file does not exist
        sales_and_items = pd.merge(sales, items, left_on="item", right_on="item_id", how="left")
        df = pd.merge(sales_and_items, stores, left_on="store", right_on="store_id", how="left")
        df.to_csv("master.csv")
    
    return df

def get_germany():
    """
    This function does the following:
    1. Looks for an existing germany.csv file, reads the csv, and returns a DataFrame
    2. If the file does not exist, the function uses the link variable to get the Open Power Systems Data for Germany, writes the DataFrame to a csv file,
        and returns a DataFrame
    """
    
    url = "https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv"
    
    if path.exists("germany.csv"):
        df = pd.read_csv("germany.csv")
    else:
        df = pd.read_csv(url)
        df.to_csv("germany.csv")
    
    return df