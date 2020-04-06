import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression

def select_kbest(features, target_variable, k):
    kbest = SelectKBest(f_regression, k)
    kbest.fit(features, target_variable)
    return features.columns[kbest.get_support()]

def select_rfe(features, target_variable, k):
    lm = LinearRegression()
    rfe = RFE(lm, k)
    rfe.fit(features, target_variable)
    return features.columns[rfe.support_]