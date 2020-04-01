import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(dataframe):
    pairplot = sns.pairplot(dataframe, kind="reg")
    plt.show()
    return pairplot

def months_to_years(tenure_months, df):
    df["tenure_years"] = (df.tenure / 12).round().astype("int")
    return df

def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    plt.figure(figsize=(32, 18))
    
    plt.subplot(221)
    barplot = sns.barplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.xlabel("Years")
    plt.ylabel("Dollars")
    plt.title("Total Charges in Dollars by Tenure in Years")
    plt.show()
    
    plt.figure(figsize=(32, 18))
    
    plt.subplot(222)
    boxplot = sns.boxplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.xlabel("Years")
    plt.ylabel("Dollars")
    plt.title("Total Charges in Dollars by Tenure in Years")
    plt.show()
    
    plt.figure(figsize=(32, 18))
    
    plt.subplot(223)
    swarmplot = sns.swarmplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.xlabel("Years")
    plt.ylabel("Dollars")
    plt.title("Total Charges in Dollars by Tenure in Years")
    plt.show()

    return barplot, boxplot, swarmplot