import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression




def select_kbest(features, target_variable, k):
    """
    This function takes in a pandas DataFrame, a target variable, and k as the amount of features to return according to the Select K Best class. 
    """
    X2 = SelectKBest(f_regression, k=k).fit_transform(features, target_variable)
    f_support = f_selector.get_support()
    f_feature = X_train.loc[:, f_support].columns.tolist()
    return f_feature