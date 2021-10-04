"""Visualizing interesting trends in the data 2(i)"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

preference_scores_of_participant = ['attractive_important', 'sincere_important', 'intelligence_important', \
'funny_important', 'ambition_important', 'shared_interests_important']

def plot_2_1():
    df = pd.read_csv('dating.csv')

    grouped = df.groupby(by='gender')
    df_female = grouped.get_group(0)
    df_male = grouped.get_group(1)

    mean_df_female = []
    mean_df_male = []

    for attribute in preference_scores_of_participant:
        mean_df_female.append(df_female[attribute].mean())
        mean_df_male.append(df_male[attribute].mean())

    x = np.arange(len(preference_scores_of_participant))  # the label locations
    width = 0.4  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, mean_df_male, width, label='male')
    rects2 = ax.bar(x + width/2, mean_df_female, width, label='female')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('mean')
    ax.set_title('Mean Values by Gender')
    ax.set_xticks(x)
    ax.set_xticklabels(preference_scores_of_participant)
    plt.xticks(fontsize=5)
    ax.legend()

    plt.show()

if __name__ == '__main__':
    plot_2_1()
