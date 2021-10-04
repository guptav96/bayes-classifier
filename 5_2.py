"""Varying the number of bins during discretization"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import discretize
import split
nbc = __import__('5_1')

def vary_bins(B):
    train_accuracy_bin = []
    test_accuracy_bin = []
    for bin_size in B:
        print(f'Bin Size: {bin_size}')
        discretize.discretize('dating.csv', f'dating-binned-{bin_size}.csv', bin_size)
        split.split(f'dating-binned-{bin_size}.csv', f'trainingSet-{bin_size}.csv', f'testSet-{bin_size}.csv')
        train_accuracy, test_accuracy = nbc.nbc(1)
        train_accuracy_bin.append(train_accuracy)
        test_accuracy_bin.append(test_accuracy)
    return train_accuracy_bin, test_accuracy_bin

def plot_bins(B, train_data, test_data):
    plt.plot(B, train_data)
    plt.plot(B, test_data)
    plt.legend(['training_data', 'test_data'])
    plt.xlabel('Number of Bins')
    plt.ylabel('Accuracy')
    plt.xticks(B)
    plt.show()

if __name__ == '__main__':
    B = [ 2, 5 ,10, 50, 100, 200]
    train, test = vary_bins(B)
    plot_bins(B, train, test)
