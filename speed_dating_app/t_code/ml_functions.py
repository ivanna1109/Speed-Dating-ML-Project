import data_processing as dp
from scipy.spatial.distance import euclidean
import numpy as np

# Finding instances that are the most resembling to the instance passed by the parameter
def most_resembling(instance):
    data = dp.read_data()
    data_reduced = dp.extract_attributes(data)
    # We decide to choose 3 of the most similiar profiles with at least 1 match
    data_reduced = data_reduced[data_reduced['match'] == 1]
    # Only some attributes are important for comparison
    data_reduced_resembling = data_reduced[['iid', 'gender', 'age',
                         'field_cd', 'race', 'imprace', 'imprelig',
                         'income', 'goal', 'date', 'go_out', 
                         'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art',
                         'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater',
                         'movies', 'concerts', 'music', 'shopping', 'yoga', 
                         'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1',
                         'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1']]
    data_reduced_resembling = data_reduced_resembling.drop_duplicates()
    data1 = data_reduced_resembling
    closest_instances = []

    closest_instances = find_closest_instance(data_reduced_resembling, data1.iloc[0])
    max_row_ind = closest_instances.idxmax()
    middle_row_ind = closest_instances[:2].idxmax()
    min_row_ind = closest_instances.idxmin()
    print(data_reduced.shape)
    print(data.iloc[max_row_ind])
    print(data.iloc[middle_row_ind])
    print(data.iloc[min_row_ind])
    #print(c[0]])

def find_closest_instance(df, instance):
    distances = df.apply(lambda row: euclidean(row, instance), axis=1)
    top_tree = distances.sort_values()[:3]
    print(top_tree)
    return top_tree

most_resembling(None)

