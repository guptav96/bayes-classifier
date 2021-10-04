"""Convert Continuous Attributes to Categorical Attributes"""

import sys
import pandas as pd
import numpy as np

not_continuous_valued_columns = ['gender', 'race', 'race_o', 'samerace', 'field', 'decision']
preference_scores_of_participant = ['attractive_important', 'sincere_important', 'intelligence_important', \
'funny_important', 'ambition_important', 'shared_interests_important']
preference_scores_of_partner = ['pref_o_attractive', 'pref_o_sincere', 'pref_o_intelligence', 'pref_o_funny', \
'pref_o_ambitious', 'pref_o_shared_interests']

def discretize(input_file, output_file, num_bins = 5):
    df = pd.read_csv(str(input_file))

    default_scale_min = 0
    default_scale_max = 10
    preference_scores_scale_min = 0
    preference_scores_scale_max = 1
    correlation_columns = ['interests_correlate']
    correlation_scale_scale_min = -1
    correlation_scale_scale_max = 1
    age_columns = ['age', 'age_o']
    age_scale_min = 18
    age_scale_max = 58
    lower_value, upper_value = 0, 10

    bin_value_counts = {}

    for column in df.columns:
        if column in not_continuous_valued_columns:
            continue
        elif column in preference_scores_of_participant or column in preference_scores_of_partner:
            lower_value = preference_scores_scale_min
            upper_value = preference_scores_scale_max
        elif column in correlation_columns:
            lower_value = correlation_scale_scale_min
            upper_value = correlation_scale_scale_max
        elif column in age_columns:
            lower_value = age_scale_min
            upper_value = age_scale_max
        else:
            lower_value = default_scale_min
            upper_value = default_scale_max
        df[column].clip(lower = lower_value, upper = upper_value, inplace = True)
        bins = np.linspace(lower_value, upper_value, num_bins + 1)
        labels = np.arange(0, num_bins, 1)
        df[column] = pd.cut(x = df[column], bins = bins, labels = labels, include_lowest = True)
        bin_value_counts[column] = df[column].value_counts(sort = False).to_numpy()

    # Output to a new csv file
    df.to_csv(str(output_file), index=False)

    return bin_value_counts

def print_output(bin_value_counts):
    for attribute, bin_values in bin_value_counts.items():
        print(f'{attribute}: {bin_values}')

if __name__ == '__main__':
    bin_value_counts = discretize(sys.argv[1], sys.argv[2])
    print_output(bin_value_counts)
