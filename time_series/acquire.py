import numpy as np
import pandas as pd

import requests

from os import path

def get_items(base_url, api):
    """
    This function does the following:
    1. 
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
    Docstring
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
    Docstring
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