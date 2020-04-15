import numpy as np
import pandas as pd

import sklearn.impute
import sklearn.model_selection
import sklearn.preprocessing



def drop_iris_columns(df):
    return df.drop(columns=["species_id", "measurement_id"])

def rename_iris_columns(df):
    return df.rename(columns={"species_name": "species"})

def encode_species(train, test):
    encoder = sklearn.preprocessing.LabelEncoder()
    encoder.fit(train.species)
    train.species = encoder.transform(train.species)
    test.species = encoder.transform(test.species)
    return encoder, train, test

def prep_iris(df):
    df = drop_iris_columns(df)
    df = rename_iris_columns(df)
    train, test = sklearn.model_selection.train_test_split(df, train_size=.8, random_state=56, stratify=df.species)
    encoder, train, test = encode_species(train, test)
    return train, test






def drop_titanic_columns(df):
    return df.drop(columns="deck")

def impute_embark_town(train, test):
    train.embark_town = train.embark_town.fillna("Southampton")
    test.embark_town = test.embark_town.fillna("Southampton")
    return train, test

def impute_embarked(train, test):
    train.embarked = train.embarked.fillna("S")
    test.embarked = test.embarked.fillna("S")
    return train, test

def encode_embarked(train, test):
    encoder = sklearn.preprocessing.LabelEncoder()
    encoder.fit(train[["embarked"]])
    train.embarked = encoder.transform(train[["embarked"]])
    test.embarked = encoder.transform(test[["embarked"]])
    return encoder, train, test

def impute_age(train, test):
    imputer = sklearn.impute.SimpleImputer(strategy="median")
    imputer.fit(train[["age"]])
    train.age = imputer.transform(train[["age"]])
    test.age = imputer.transform(test[["age"]])
    return train, test

def min_max_scaler(train, test):
    scaler = sklearn.preprocessing.MinMaxScaler()
    scaler.fit(train[["age", "fare"]])
    train[["age", "fare"]] = scaler.transform(train[["age", "fare"]])
    test[["age", "fare"]] = scaler.transform(test[["age", "fare"]])
    return scaler, train, test

def prep_titanic(df):
    drop_titanic_columns(df)
    train, test = sklearn.model_selection.train_test_split(df, train_size=.8, random_state=56, stratify=df.survived)
    train, test = impute_embark_town(train, test)
    train, test = impute_embarked(train, test)
    encoder, train, test = encode_embarked(train, test)
    train, test = impute_age(train, test)
    scaler, train, test = min_max_scaler(train, test)
    return train, test