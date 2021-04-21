# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
sf_permits = pd.read_csv("../data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0)
# Use the code cell below to print the first five rows of the sf_permits DataFrame.
sf_permits.head()

# What percentage of the values in the dataset are missing? Your answer should be a number between 0 and 100.
# (If 1/4 of the values in the dataset are missing, the answer is 25.)
# Count values missing by columns
missing_values_count_columns = sf_permits.isnull().sum()
missing_values_count = missing_values_count_columns.sum()
total_cells = np.product(sf_permits.shape)
percent_missing = (missing_values_count / total_cells) * 100
# Look at the columns "Street Number Suffix" and "Zipcode" from the San Francisco Building Permits dataset.
# Both of these contain missing values.
# Which, if either, are missing because they don't exist? Street Number Suffix
# Which, if either, are missing because they weren't recorded? Zipcode

# If you removed all of the rows of sf_permits with missing values, how many rows are left?
sf_permits.dropna()
# Create a new DataFrame called sf_permits_with_na_dropped that has all of the columns with empty values removed.
# How many columns were removed from the original sf_permits DataFrame? Use this number to set the value of the
# dropped_columns variable below
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
dropped_columns = sf_permits.shape[1] - sf_permits_with_na_dropped.shape[1]
# Try replacing all the NaN's in the sf_permits data with the one that comes directly after it and then replacing
# any remaining NaN's with 0. Set the result to a new DataFrame sf_permits_with_na_imputed.
sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)

