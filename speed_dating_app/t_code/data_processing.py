import pandas as pd
def read_data():
    data = pd.read_csv('Speed Dating Data.csv', encoding="ISO 8859-1")
    return data

#extract the most important attributes
def extract_attributes(data):
    data_reduced = data[['iid', 'gender', 'pid', 'match', 'int_corr', 'samerace',
                         'age_o', 'race_o', 'dec_o', 'dec', 'attr_o', 'age',
                         'field', 'field_cd', 'race', 'imprace', 'imprelig',
                         'income', 'goal', 'date', 'go_out', 'career', 'career_c',
                         'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art',
                         'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater',
                         'movies', 'concerts', 'music', 'shopping', 'yoga', 
                         'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1',
                         'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1',
                         'attr3_1', 'sinc3_1', 'intel3_1', 'fun3_1', 'amb3_1']]
    
    data_reduced = data_reduced.fillna(method='ffill');
    data_reduced.loc[:,'income'] = data_reduced.loc[:,'income'].str.replace(",","").astype(float)
    return data_reduced

def attribute_corr(data):
    df_corr = data.corr().dropna()
    subset_index = df_corr["match"].abs().sort_values(ascending = False)[:20].index.tolist()
    data_subset = data[subset_index]
    df_subset_corr = data_subset.corr()
    return data_subset


data = read_data()
data_reduced = extract_attributes(data)
print(data_reduced.shape)