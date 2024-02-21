import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def filereader(filePath):
    return pd.read_excel(filePath)


def save_to_excel(data, file_path):
    """
    Save DataFrame to an Excel file.

    Parameters:
    - data: pandas DataFrame
    - file_path: str, path to the Excel file
    """
    try:

        data.to_excel(file_path, index=False)
        print(f"DataFrame successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving DataFrame to {file_path}: {e}")


def cleanDate(train_data):
    train_data.dropna(inplace=True)


def change_to_Datatime(data, col):
    data[col] = pd.to_datetime(data[col])


def extract_Date(df, col):
    df[col + "_day"] = df[col].dt.day
    df[col + "_Month"] = df[col].dt.month
    df[col + "_Year"] = df[col].dt.year
    df[col + "_time_hour"] = df[col].dt.hour
    df[col + "_time_minute"] = df[col].dt.minute


def dataPreprocessing():
    filePath = 'Data/raw_data/Consumer Behaviour_Data.xlsx'
    train_data = filereader(filePath)
    data = train_data.copy()
    print(data.columns)
    print(data['Date'].head())
    change_to_Datatime(data, 'Date')
    extract_Date(data, 'Date')
    label_encoder = LabelEncoder()
    data['Itemname'] = label_encoder.fit_transform(data['Itemname'])
    print(data.columns)
    data.drop(['Date'], axis=1, inplace=True)
    print(data.columns)
    All_Purchases = data.copy()
    with_CustomerID = data.copy()
    # save_to_excel(data, 'Data/processed_data/All_Purchases.xlsx')
    with_CustomerID = with_CustomerID.dropna(subset=['CustomerID'])
    print(with_CustomerID[['CustomerID', 'BillNo']].loc[with_CustomerID['CustomerID'].isnull()])
    without_CustomerID = All_Purchases[All_Purchases['CustomerID'].isnull()].copy()
    without_CustomerID = without_CustomerID.drop(['CustomerID'], axis=1)
    All_Purchases.drop(['CustomerID'], axis=1, inplace=True)

    return All_Purchases, with_CustomerID, without_CustomerID
