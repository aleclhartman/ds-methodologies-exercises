import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split

def remove_columns(df, cols_to_remove):
    """
    Docstring
    """
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .60, prop_required_row = .60):
    """
    Docstring
    """
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def impute_regionidcity(train, validate, test):
    """
    This function does the following:
    1. Takes in the train, validate, and test datasets
    2. Creates the KNNImputer object
    3. Fits the object to the regionidcity feature in the train dataset
    4. Transforms the regionidcity feature in the train, validate, and test datasets
    """
    imputer = KNNImputer(n_neighbors=5)
    imputer.fit(train[["regionidcity"]])
    train["regionidcity"] = imputer.transform(train[["regionidcity"]])
    validate["regionidcity"] = imputer.transform(validate[["regionidcity"]])
    test["regionidcity"] = imputer.transform(test[["regionidcity"]])
    return imputer, train, validate, test

def prep_zillow(df):
    """
    Docstring
    """

    # removing any properties that are likely to be something other than single unit properties
    df = df[df.propertylandusetypeid.isin([260, 261, 262, 279])]
    df = df[(df.bedroomcnt > 0) & (df.bathroomcnt > 0)]

    # unitcnt imputation
    df.unitcnt = df.unitcnt.fillna(1.0)

    # filter out units with more than one unit
    df = df[df.unitcnt == 1.0]

    # dropping unnecessary columns
    df.drop(columns="id", inplace=True)

    # calling handle_missing_values to remove columns and rows that do not meet the default threshold critera necessary to retain variable or index
    df = handle_missing_values(df)

    # dropping id columns
    df = df.drop(columns=["propertylandusetypeid", "heatingorsystemtypeid"])

    # heatingorsystemdesc imputation with "None" as properties are in SoCal so "None" is reasonable
    df.heatingorsystemdesc = df.heatingorsystemdesc.fillna("None")

    # dropping propertyzoningdesc we have already filtered the data to single unit properties
    df = df.drop(columns="propertyzoningdesc")

    # buildingqualitytypeid imputation
    df.buildingqualitytypeid = df.buildingqualitytypeid.fillna(df.buildingqualitytypeid.median())

    # lotsizesquarefeet imputation with mode
    df.lotsizesquarefeet = df.lotsizesquarefeet.fillna(6000.0)

    # calculatedbathnbr imputation
    df.calculatedbathnbr = df.calculatedbathnbr.fillna(df.calculatedbathnbr.median())

    # calculatedfinishedsquarefeet imputation with mode
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.fillna(1120.0)

    # drop finishedsquarefeet12 as the info appears to be redundant when compared to calculatedfinishedsquarefeet
    df.drop(columns="finishedsquarefeet12", inplace=True)

    # fullbathcnt imputation
    df.fullbathcnt = df.fullbathcnt.fillna(df.fullbathcnt.median())

    # yearbuilt
    df.yearbuilt = df.yearbuilt.fillna(round(df.yearbuilt.mean()))

    # structuretaxvaluedollarcnt imputation based on the difference between taxvaluedollarcnt and and landtaxvaluedollarcnt as 
    # 99.9% of the values in structuretaxvaluedollarcnt are equal to this difference
    df.structuretaxvaluedollarcnt = df.structuretaxvaluedollarcnt.fillna(df.taxvaluedollarcnt - df.landtaxvaluedollarcnt)

    # drop the remaining row with no structuretaxvaluedollarcnt value as taxvaluedollarcnt and landtaxvaluedollarcnt are also missing
    df.drop(index=62533, inplace=True)

    # drop the four rows with missing taxamount
    df.drop(index=df[df.taxamount.isna() == True].index.tolist(), inplace=True)

    # drop rows where censustractandblock is missing
    df.drop(index=df[df.censustractandblock.isna() == True].index.tolist(), inplace=True)

    # drop rows where regionidzip is missing
    df.drop(index=df[df.regionidzip.isna() == True].index.tolist(), inplace=True)

    # split data into train, validate, test
    train, test = train_test_split(df, train_size=.8, random_state=56)
    train, validate = train_test_split(train, train_size=.75, random_state=56)

    # KNN imputation for regionidcity
    imputer, train, validate, test = impute_regionidcity(train, validate, test)

    return imputer, train, validate, test

