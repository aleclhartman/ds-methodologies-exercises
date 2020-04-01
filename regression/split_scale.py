import numpy as np
import pandas as pd

import sklearn.preprocessing
from sklearn.model_selection import train_test_split

def split_my_data(X, y, train_pct):
    return train_test_split(X, y, train_size=train_pct, random_state=56)

def standard_scaler(train, test):
    # create the object
    scaler = sklearn.preprocessing.StandardScaler()
    # fit the object
    scaler.fit(train)
    # use the object
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train_scaled, test_scaled

def scale_inverse(scaler, train_scaled, test_scaled):
    train_revert = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns, index=train_scaled.index)
    test_revert = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns, index=test_scaled.index)
    return train_revert, test_revert

def uniform_scaler(train, test):
    # create the object
    scaler = sklearn.preprocessing.QuantileTransformer(output_distribution="uniform")
    # fit the object
    scaler.fit(train)
    # use the object
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train_scaled, test_scaled

def gaussian_scaler(train, test):
    # create the object
    scaler = sklearn.preprocessing.PowerTransformer(method="yeo-johnson")
    # fit the object
    scaler.fit(train)
    # use the object
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train_scaled, test_scaled

def min_max_scaler(train, test):
    # create the object
    scaler = sklearn.preprocessing.MinMaxScaler()
    # fit the object
    scaler.fit(train)
    # use the object
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train_scaled, test_scaled

def iqr_robust_scaler(train, test):
    # create the object
    scaler = sklearn.preprocessing.RobustScaler()
    # fit the object
    scaler.fit(train)
    # use the object
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns, index=train.index)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return scaler, train_scaled, test_scaled