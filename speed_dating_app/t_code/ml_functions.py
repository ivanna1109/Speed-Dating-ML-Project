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
    data_reduced_resembling = data_transform(data_reduced)
    data1 = data_reduced_resembling

    closest_instances = find_closest_instance(data_reduced_resembling, data1.iloc[0])
    max_row_ind = closest_instances.idxmax()
    middle_row_ind = closest_instances[:2].idxmax()
    min_row_ind = closest_instances.idxmin()
    print(data_reduced.shape)
    print(data.iloc[max_row_ind])
    print(data.iloc[middle_row_ind])
    print(data.iloc[min_row_ind])

    # collect three of the most similar instances and all of their matches
    data_potential_matches_tmp = data[(data['iid'] == data.iloc[min_row_ind]['iid']) |
              (data['iid'] == data.iloc[middle_row_ind]['iid']) |
              (data['iid'] == data.iloc[max_row_ind]['iid'])]

    # get their matches
    list_of_pids = data_potential_matches_tmp['pid'].tolist()
    list_of_all_matches = data[data['iid'].isin(list_of_pids)]
    # get rid of the duplicates and extract the important attributes
    list_of_all_matches = data_transform(list_of_all_matches)
        
    # calculating the 'match percentage' value in order to find the best ones
    #data_potential_matches_tmp['match_pct'] = find_match_pct_list(data_potential_matches_tmp, list_of_all_matches)

    print(list_of_all_matches)
    
# finding a list that contains euclidean distances between all of the instances and their matches
def find_match_pct_list(data_potential_matches_tmp, list_of_all_matches):
    match_pct_list = []
    for index, row in data_potential_matches_tmp.iterrows():
        similar_people_vector = find_similar_people_vector(row)
        match_vector = find_similar_people_match_vector(list_of_all_matches[list_of_all_matches['iid'] == row['pid']])
        match_pct_list.append(euclidean(similar_people_vector, match_vector))
    return match_pct_list

# extracting the attributes representing someone's expectations
def find_similar_people_vector(similar_people):
    pass

# extracting the attributes representing the needed characterstics of a match
def find_similar_people_match_vector(match):
    pass

def data_transform(data_frame):
    return data_frame[['iid', 'gender', 'age',
                         'field_cd', 'race', 'imprace', 'imprelig',
                         'income', 'goal', 'date', 'go_out', 
                         'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art',
                         'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater',
                         'movies', 'concerts', 'music', 'shopping', 'yoga', 
                         'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1',
                         'attr2_1', 'sinc2_1', 'intel2_1', 'fun2_1', 'amb2_1', 'shar2_1']].drop_duplicates()


def find_closest_instance(df, instance):
    distances = df.apply(lambda row: euclidean(row, instance), axis=1)
    top_tree = distances.sort_values()[:3]
    print(top_tree)
    return top_tree

most_resembling(None)

