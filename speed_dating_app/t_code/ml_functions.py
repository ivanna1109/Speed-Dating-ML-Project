import data_processing as dp
from scipy.spatial.distance import euclidean
import numpy as np

# Finding instances that are the most resembling to the instance passed by the parameter
def most_resembling(instance_attrs):
    data = dp.read_data()
    scale_evaluation_columns(data)
    data = data.fillna(method='ffill');
    data_reduced = dp.extract_attributes(data)
    # We decide to choose 3 of the most similiar profiles with at least 1 match
    data_reduced = data_reduced[data_reduced['match'] == 1]
    # Only some attributes are important for comparison
    data_reduced_resembling = data_transform(data_reduced)
    data1 = data_reduced_resembling

    # creating an instance based on the attributes passed by the parameter 'instance_attrs'
    new_instance = create_instance(instance_attrs, data.shape[0] + 1)

    closest_instances = find_closest_instance(data_reduced_resembling, new_instance)
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
    list = find_match_pct_list(data_potential_matches_tmp, list_of_all_matches)
    data_potential_matches_tmp.insert(data_potential_matches_tmp.shape[1], 'match_value', list, True)
    data_matches = data_potential_matches_tmp.sort_values(['iid', 'match_value'], ascending=True)
    print(data_matches.head(3))

    # the final list containing the 'iid' values for top 3 matches
    top_3_matches = [int(data_matches.iloc[0]['pid']), int(data_matches.iloc[1]['pid']), int(data_matches.iloc[2]['pid'])]
    print(top_3_matches)
    return top_3_matches

# finding a list that contains euclidean distances between all of the instances and their matches
def find_match_pct_list(data_potential_matches_tmp, list_of_all_matches):
    match_pct_list = []
    for index, row in data_potential_matches_tmp.iterrows():
        similar_people_vector = find_similar_people_vector1(row)
        match_df = list_of_all_matches[list_of_all_matches['iid'] == row['pid']]
        match_vector = find_similar_people_vector2(match_df.iloc[0])
        match_pct_list.append(euclidean(similar_people_vector, match_vector))
    return match_pct_list

# extracting the attributes representing someone's expectations
def find_similar_people_vector1(similar_people):
    vector = [similar_people['age'], similar_people['imprace'], similar_people['imprelig'],
              similar_people['goal'], similar_people['go_out'],
              similar_people['sports'], similar_people['tvsports'], similar_people['exercise'],
              similar_people['dining'], similar_people['museums'], similar_people['art'],
              similar_people['hiking'], similar_people['gaming'], similar_people['clubbing'], 
              similar_people['reading'], similar_people['tv'], similar_people['theater'],
              similar_people['movies'], similar_people['concerts'], similar_people['music'], 
              similar_people['shopping'], similar_people['yoga'], similar_people['attr1_1'], 
              similar_people['sinc1_1'], similar_people['intel1_1'], similar_people['fun1_1'], 
              similar_people['amb1_1'], similar_people['attr3_1'], 
              similar_people['sinc3_1'], similar_people['intel3_1'], similar_people['fun3_1'], 
              similar_people['amb3_1']]
    return vector

def find_similar_people_vector2(similar_people):
    vector = [similar_people['age'], similar_people['imprace'], similar_people['imprelig'],
              similar_people['goal'], similar_people['go_out'],
              similar_people['sports'], similar_people['tvsports'], similar_people['exercise'],
              similar_people['dining'], similar_people['museums'], similar_people['art'],
              similar_people['hiking'], similar_people['gaming'], similar_people['clubbing'], 
              similar_people['reading'], similar_people['tv'], similar_people['theater'],
              similar_people['movies'], similar_people['concerts'], similar_people['music'], 
              similar_people['shopping'], similar_people['yoga'], similar_people['attr3_1'], 
              similar_people['sinc3_1'], similar_people['intel3_1'], similar_people['fun3_1'], 
              similar_people['amb3_1'], similar_people['attr1_1'], 
              similar_people['sinc1_1'], similar_people['intel1_1'], similar_people['fun1_1'], 
              similar_people['amb1_1']]
    return vector

def data_transform(data_frame):
    return data_frame[['iid', 'gender', 'age',
                         'field_cd', 'race', 'imprace', 'imprelig',
                         'income', 'goal', 'date', 'go_out', 
                         'sports', 'tvsports', 'exercise', 'dining', 'museums', 'art',
                         'hiking', 'gaming', 'clubbing', 'reading', 'tv', 'theater',
                         'movies', 'concerts', 'music', 'shopping', 'yoga', 
                         'attr1_1', 'sinc1_1', 'intel1_1', 'fun1_1', 'amb1_1', 'shar1_1',
                         'attr3_1', 'sinc3_1', 'intel3_1', 'fun3_1', 'amb3_1']].drop_duplicates()


# scaling attr1_1, ..., shar1_1 attributes to a [1-10] interval
def attribute_scaling(x):
    return 1 + (x / 100) * 9

def scale_evaluation_columns(data_frame):
    data_frame['attr1_1'] = data_frame['attr1_1'].map(attribute_scaling)
    data_frame['sinc1_1'] = data_frame['sinc1_1'].map(attribute_scaling)
    data_frame['intel1_1'] = data_frame['intel1_1'].map(attribute_scaling)
    data_frame['fun1_1'] = data_frame['fun1_1'].map(attribute_scaling)
    data_frame['amb1_1'] = data_frame['amb1_1'].map(attribute_scaling)
 
def find_closest_instance(df, instance):
    distances = df.apply(lambda row: euclidean(row, instance), axis=1)
    top_tree = distances.sort_values()[:3]
    print(top_tree)
    return top_tree

def create_instance(instance_attributes, iid):
    instance = [iid] + instance_attributes
    return instance


most_resembling([0.0, 43.0, 1.0, 4.0, 2.0, 4.0, 85000.0, 2.0, 7.0, 1.0, 9.0, 2.0, 8.0, 9.0, 8.0, 8.0, 5.0, 9.0, 5.0, 6.0, 9.0, 1.0, 10.0, 10.0, 9.0, 8.0, 1.0,
                 2.35, 2.80, 2.80, 2.35, 2.35, 15.0, 1.0, 2.0, 1.0, 1.0, 2.0])

