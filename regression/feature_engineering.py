import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression

def select_kbest(features, target_variable, k):
    f_selector = SelectKBest(f_regression, k=k)
    f_selector.fit(features, target_variable)
    X_reduced = f_selector.transform(features)
    f_support = f_selector.get_support()
    f_feature = features.loc[:,f_support].columns.tolist()
    return f_feature

def rfe(features, target_variable, k):
    lm = LinearRegression()
    rfe = RFE(lm, k)
    rfe.fit(features, target_variable)
    X_rfe = rfe.transform(features)
    mask = rfe.support_
    rfe_features = features.loc[:, mask].columns.tolist()
    return rfe_features