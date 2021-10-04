""" Plotting Learning Curves """
random_state = 47

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
nbc = __import__('5_1')

def solve_5_3(F):
    train_accuracy_list = []
    test_accuracy_list = []
    for t_frac in F:
        print(f't_frac: {t_frac}')
        train_accuracy, test_accuracy  = nbc.nbc(t_frac)
        train_accuracy_list.append(train_accuracy)
        test_accuracy_list.append(test_accuracy)
    return train_accuracy_list, test_accuracy_list

def plot(F, train_data, test_data):
    plt.plot(F, train_data)
    plt.plot(F, test_data)
    plt.legend(['training_data', 'test_data'])
    plt.xlabel('t_frac')
    plt.ylabel('Accuracy')
    plt.xticks(F)
    plt.show()

if __name__ == '__main__':
    F = [ 0.01,0.1, 0.2, 0.5, 0.6, 0.75, 0.9, 1 ]
    train_accuracy_list, test_accuracy_list = solve_5_3(F)
    plot(F, train_accuracy_list, test_accuracy_list)
