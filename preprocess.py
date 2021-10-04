"""Preprocessing  Data"""

import sys

import pandas as pd

def preprocess(input_file, output_file):
    df = pd.read_csv(str(input_file))

    # 1(i) Removing Quotes
    df_temp = df.copy(deep = True)
    df[['race', 'race_o', 'field']] = df[['race', 'race_o', 'field']].applymap(lambda x: x.strip("'"))
    count_of_changed_cells = df.count().sum() - (df == df_temp).astype(int).sum().sum()
    print(f'Quotes removed from {count_of_changed_cells} cells.')
    del df_temp

    # 1(ii) Lowercasing
    df_temp2 = df.copy(deep = True)
    df['field'] = df['field'].apply(lambda x: x.lower())
    count_of_changed_cells = df['field'].count().sum() - (df['field'] == df_temp2['field']).astype(int).sum().sum()
    print(f'Standardized {count_of_changed_cells} cells to lower case.')
    del df_temp2

    #1(iii) Categorical attributes
    categories = {}
    for attribute in ['gender', 'race', 'race_o', 'field']:
        df[attribute] = df[attribute].astype("category")
        categories[attribute] = df[attribute].cat.categories
        df[attribute] = df[attribute].cat.codes
    value_for_male = categories['gender'].get_loc('male')
    value_for_european_caucasian_american = categories['race'].get_loc('European/Caucasian-American')
    value_for_latino_hispanic_american = categories['race_o'].get_loc('Latino/Hispanic American')
    value_for_law = categories['field'].get_loc('law')
    print(f'Value assigned for male in column gender: {value_for_male}.')
    print(f'Value assigned for European/Caucasian-American in column race: {value_for_european_caucasian_american}.')
    print(f'Value assigned for Latino/Hispanic American in column race_o: {value_for_latino_hispanic_american}.')
    print(f'Value assigned for law in column field: {value_for_law}.')

    #1(iv) Normalization
    preference_scores_of_participant = ['attractive_important', 'sincere_important', 'intelligence_important', \
    'funny_important', 'ambition_important', 'shared_interests_important']
    preference_scores_of_partner = ['pref_o_attractive', 'pref_o_sincere', 'pref_o_intelligence', 'pref_o_funny', \
    'pref_o_ambitious', 'pref_o_shared_interests']
    preference_scores_of_participant_sum = df[preference_scores_of_participant].sum(axis = 1)
    preference_scores_of_partner_sum = df[preference_scores_of_partner].sum(axis = 1)
    df[preference_scores_of_participant] = df[preference_scores_of_participant].div(preference_scores_of_participant_sum, axis = 0)
    df[preference_scores_of_partner] = df[preference_scores_of_partner].div(preference_scores_of_partner_sum, axis = 0)
    for attribute in preference_scores_of_participant:
        mean_of_attribute = round(df[attribute].mean(), 2)
        print(f'Mean of {attribute}: {mean_of_attribute:.2f}')
    for attribute in preference_scores_of_partner:
        mean_of_attribute = round(df[attribute].mean(), 2)
        print(f'Mean of {attribute}: {mean_of_attribute:.2f}')

    # Output file
    df.to_csv(str(output_file), index=False)

if __name__ == '__main__':
    preprocess(sys.argv[1], sys.argv[2])
