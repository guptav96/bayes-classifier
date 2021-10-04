"""Split data into training and test sets"""

import sys

import pandas as pd
import numpy as np

random_state = 47
frac = 0.2

def split(input, output_train, output_test):
    df = pd.read_csv(str(input))

    test_df = df.sample(frac = frac, random_state = random_state)
    train_df = df.drop(test_df.index)

    # Output training and test csv files
    train_df.to_csv(str(output_train), index=False)
    test_df.to_csv(str(output_test), index=False)

if __name__ == '__main__':
    split(sys.argv[1], sys.argv[2], sys.argv[3])
