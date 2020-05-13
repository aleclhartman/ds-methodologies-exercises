import numpy as np
import pandas as pd
from datetime import timedelta, datetime

import matplotlib.pyplot as plt

import acquire as ac


def convert_sale_date_dtype(df):
    """
    This function converts the sales_date dtype from an object to datetime
    """
    
    df["sale_date"] = pd.to_datetime(df["sale_date"], format='%a, %d %b %Y %H:%M:%S %Z')
    
    return df

def plot_sale_amount_dist(df):
    """
    This function plots the distribution of the sale amount variable from the DataFrame passed into the function
    """

    plt.figure(figsize=(16, 8))

    df.sale_amount.hist()
    plt.title("Distribution of Sale Amount")
    plt.show()

def plot_item_price_dist(df):
    """
    This function plots the distribution of the item_price variable from the DataFrame passed into the function
    """

    plt.figure(figsize=(16, 8))

    df.item_price.hist()
    plt.title("Distribution of Item Price")
    plt.show()

def set_sale_date_index(df):
    """
    This function sorts the sale_date field and sets it as the index of the DataFrame passed into the function
    """
    
    df = df.sort_values("sale_date").set_index("sale_date")
    
    return df

def create_month_weekday_variables(df):
    """
    This function create a month and year variable in the DataFrame passed into the function
    """
    
    df["month"] = df.index.month_name()
    df["weekday"] = df.index.day_name()
    
    return df

def create_sale_amount_variable(df):
    """
    This function renames the existing sale_amount variable to quantity and then creates a more appropriate sale_amount variable
    """

    # rename sale_amount to quantity
    df.rename(columns={"sale_amount": "quantity"}, inplace=True)

    # creates new sale_amount
    df["sale_amount"] = df.quantity * df.item_price

    return df

def daily_sales_diff(df):
    """
    This function upsamples the sales DataFrame for a daily frequency, and then calculates the daily difference in sales.
    """
    # upsampling df for daily frequency
    daily_sales = pd.DataFrame(df.sale_amount.resample("D").sum())

    # calculate daily_sales diff
    daily_sales["diff"] = daily_sales.sale_amount.diff(1)

    return daily_sales

def wrangle_sales():
    """
    This function calls all the functions above necessary to prepare the sales DataFrame
    """

    # acquire sales data
    df = ac.get_sales()

    # convert date dtype
    df = convert_sale_date_dtype(df)

    # sets sales_date as index
    df = set_sale_date_index(df)

    # create new month and weekday variables
    df = create_month_weekday_variables(df)

    # create new sale amount variable
    df = create_sale_amount_variable(df)

    return df


def convert_date_dtype(df):
    """
    This function converts the Date dtype from an object to datetime
    """
    
    df["Date"] = pd.to_datetime(df.Date)
    
    return df

def plot_dist(df):
    """
    This function plots the distributions of each variable from the DataFrame passed into the function
    """
    
    df.hist(figsize=(16, 16))
    plt.show()

def set_date_index(df):
    """
    This function sorts the Date field and sets it as the index of the DataFrame passed into the function
    """
    
    df = df.sort_values("Date").set_index("Date")
    
    return df

def create_month_year_variables(df):
    """
    This function create a month and year variable in the DataFrame passed into the function
    """
    
    df["month"] = df.index.month_name()
    df["year"] = df.index.year
    
    return df

def wrangle_germany():
    """
    This function calls all the functions above necessary to prepare the germany DataFrame
    """

    # acquire germany data
    df = ac.get_germany()

    # convert data types
    df = convert_date_dtype(df)

    # set date as index
    df = set_date_index(df)

    # make new variables
    df = create_month_year_variables(df)

    return df