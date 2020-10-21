import pandas as pd
import numpy as np


def clean_data(dataframe):
    dataframe.drop(columns='Unnamed: 0', inplace=True)
    dataframe['date'] = pd.to_datetime(dataframe['date'])

    dataframe['sale_year'] = pd.DatetimeIndex(dataframe['date']).year
    dataframe['sale_month'] = pd.DatetimeIndex(dataframe['date']).month
    dataframe.drop(columns='date', inplace=True)

    return dataframe.head(5)

def no_bedrooms(dataframe, df2):
    index=dataframe.loc[dataframe.bedrooms == 0].index.to_list()
    dataframe.drop(dataframe.index[[index]], inplace=True)
    frames= [dataframe, df2]
    dataframe = pd.concat(frames)
    print(dataframe.shape)
    return dataframe

def price_distribution(dataframe):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.hist(dataframe['price'], bins=100);
    ax.set_title('Housing Prices');

def multicolinear_features(data):
    df=data.corr().abs().stack().reset_index().sort_values(0, ascending=False)
    df['pairs'] = list(zip(df.level_0, df.level_1))
    df.set_index(['pairs'], inplace = True)
    df.drop(columns=['level_1', 'level_0'], inplace = True)
    df.columns = ['cc']
    return df[(df.cc>.75) & (df.cc <1)]

def remove_outliers(dataframe, feature):

    Q1 = dataframe[feature].quantile(.25)
    Q3 = dataframe[feature].quantile(.75)
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    dataframe.drop(dataframe[(dataframe[feature] > upper_b) | (dataframe[feature] < lower_b)].index , inplace=True)
    print('Removed {} outliers above or below {}, {}'.format(feature, lower_range, upper_range))
