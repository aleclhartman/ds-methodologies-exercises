import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error

from math import sqrt

def plot_residuals(y, yhat, yhat_baseline, df):
    residual_baseline = yhat_baseline - y
    residual = yhat - y
    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(16, 9))
    ax1 = axs[0]
    ax2 = axs[1]
    ax1.set_title("Baseline Residuals")
    ax2.set_title("Residuals")
    fig.text(.1, 0.5, "yhat - y", ha="center", va="center", rotation="vertical")
    sns.scatterplot(x=y, y=residual_baseline, data=df, color="crimson", ax=axs[0]) # residual baseline
    sns.scatterplot(x=y, y=residual, data=df, color="navy", ax=axs[1]) # residual
    plt.show()

# consider returning a dictionary (or Series or DataFrame) of your calculations
def regression_errors(y, yhat, df):
    SSE = mean_squared_error(y, yhat)*df.shape[0]
    ESS = sum((yhat - y.mean())**2)
    TSS = ESS + SSE
    MSE = mean_squared_error(y, yhat)
    RMSE = sqrt(MSE)
    return SSE, ESS, TSS, MSE, RMSE

# consider returning a dictionary (or Series or DataFrame) of your calculations
# perhaps, add a baseline_calc argument that can be set to either mean or median so that logic can be added to the function to calculate the baseline within the function
def baseline_mean_errors(y, yhat_baseline, df):
    SSE_baseline = mean_squared_error(y, yhat_baseline)*df.shape[0]
    MSE_baseline = mean_squared_error(y, yhat_baseline)
    RMSE_baseline = sqrt(MSE_baseline)
    return SSE_baseline, MSE_baseline, RMSE_baseline

def better_than_baseline(y, yhat, yhat_baseline, df):
    SSE, ESS, TSS, MSE, RMSE = regression_errors(y=y, yhat=yhat, df=df)
    SSE_baseline, MSE_baseline, RMSE_baseline = baseline_mean_errors(y=y, yhat_baseline=yhat_baseline, df=df)
    if RMSE < RMSE_baseline:
        return True
    else:
        return False

def model_significance(ols_model):
    """
    Takes in an ordinary least squares model and returns the p-value of the F-statistic
    """
    f_pval = ols_model.f_pvalue
    return print(f"p-value for model significance = {f_pval}")