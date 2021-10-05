"""Visualizing interesting trends in the data 2(ii)"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rating_of_partner_from_participant = ['attractive_partner', 'sincere_partner', 'intelligence_parter', \
'funny_partner', 'ambition_partner', 'shared_interests_partner']

def plot_2_2():
    df = pd.read_csv('dating.csv')

    n_unique = {}
    for attribute in rating_of_partner_from_participant:
        elems, count = np.unique(df[attribute], return_counts = True)
        n_unique[attribute] = {}
        for idx in range(len(elems)):
            n_unique[attribute][elems[idx]] = count[idx]

    def calc_success_rate(attribute, value):
        num = len(df[(df[attribute] == value) & (df['decision'] == 1)])
        den = n_unique[attribute][value]
        return float(num)/den

    success_rate = {}
    for attribute in rating_of_partner_from_participant:
        success_rate[attribute] = {}
        for distinct_val in n_unique[attribute].keys():
            success_rate[attribute][distinct_val] = calc_success_rate(attribute, distinct_val)

    ax = {}
    for idx, attribute in enumerate(rating_of_partner_from_participant):
        x = success_rate[attribute].keys()
        y = success_rate[attribute].values()
        # print(f'{attribute}: {len(y)}')
        ax[idx] = plt.subplot(2, 3, idx + 1)
        ax[idx].set_ylabel('Success Rate')
        ax[idx].set_xlabel(f'{attribute}')
        ax[idx].scatter(x, y)
    plt.suptitle('Success Rates vs Attribute Value for different attributes')
    plt.show()

if __name__ == '__main__':
    plot_2_2()
