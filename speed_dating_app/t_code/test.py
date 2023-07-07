import pandas as pd

def read_data():
    data = pd.read_csv('Speed Dating Data.csv', encoding="ISO 8859-1")
    print(data.head())

read_data()