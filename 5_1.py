"""Naive Bayes Classifier Implementation"""

random_state = 47

import pandas as pd
import numpy as np

laplace_correction = True

def nbc(t_frac):
    train_df = pd.read_csv('trainingSet.csv')
    test_df = pd.read_csv('testSet.csv')

    # sample the training data from training dataframe
    sampled_train_df = train_df.sample(frac = t_frac, random_state = random_state, ignore_index = True)

    attributes = sampled_train_df.columns[:-1]

    # calculating prior probability
    prior = sampled_train_df.groupby(by = 'decision').size().div(len(sampled_train_df))

    # calculating conditional probabilities
    conditional_prob = {}
    for attribute in attributes:
        numerator = sampled_train_df.groupby(by = ['decision'])[attribute].value_counts().unstack('decision')
        denominator = numerator.sum()
        k = sampled_train_df[attribute].nunique()
        if laplace_correction and numerator.isna().any(axis=None):
            numerator.fillna(value=0, inplace=True)
            numerator += 1
            denominator += k
        conditional_prob[attribute] = numerator.div(denominator)

    # calculating posterior probability for all training examples
    def predict(row, label):
        result = 1
        for attribute in attributes:
            try:
                result *= conditional_prob[attribute][label][row[attribute]]
            except:
                # if there is a new attribute value not known at the training time
                # laplace correction wouldn't work here, since the attr val is not known at the training time
                continue
        result *= prior[label]
        return result

    predicted_training_no = np.array([ predict(row, 0) for idx, row in sampled_train_df.iterrows() ])
    predicted_training_yes =  np.array([ predict(row, 1) for idx, row in sampled_train_df.iterrows() ])
    predicted_training_labels = predicted_training_yes > predicted_training_no
    train_accuracy = accuracy(sampled_train_df.iloc[:,-1], predicted_training_labels)
    print(f'Training Accuracy: {round(train_accuracy,2)}')

    predicted_test_no = np.array([ predict(row, 0) for idx, row in test_df.iterrows() ])
    predicted_test_yes =  np.array([ predict(row, 1) for idx, row in test_df.iterrows() ])
    predicted_test_labels = predicted_test_yes > predicted_test_no
    test_accuracy = accuracy(test_df.iloc[:,-1], predicted_test_labels)
    print(f'Testing Accuracy: {round(test_accuracy,2)}')

    return train_accuracy, test_accuracy

def accuracy(original_labels, predicted_labels):
    count = 0
    total_num = len(original_labels)
    for idx in range(total_num):
        if original_labels[idx] == predicted_labels[idx]:
            count += 1
    return float(count)/total_num

if __name__ == '__main__':
    nbc(1)
