import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(dataframe):
    sns.pairplot(dataframe, kind="reg")

def months_to_years(tenure_months, df, rounding=False):
    if rounding:
        df["tenure_years"] = np.round(tenure_months / 12)
    else:
        df["tenure_years"] = np.round(tenure_months // 12)
    return df

# make this function more dynamic
def plot_categorical_and_continuous_vars(categorical_var, continuous_var, df):
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