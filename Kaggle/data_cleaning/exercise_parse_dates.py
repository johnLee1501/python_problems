# modules we'll use
import pandas as pd
import numpy as np
import seaborn as sns
import datetime

# read in our data
earthquakes = pd.read_csv("../data/database.csv")

# set seed for reproducibility
np.random.seed(0)

# You'll be working with the "Date" column from the `earthquakes` dataframe.
# Investigate this column now: does it look like it contains dates?  What is the dtype of the column?
type_date = earthquakes.Date.dtype
# Most of the entries in the "Date" column follow the same format: "month/day/four-digit year".
# However, the entry at index 3378 follows a completely different pattern. Run the code cell below to see this.
print(earthquakes[3378:3383])
# This does appear to be an issue with data entry: ideally, all entries in the column have the same format.
# We can get an idea of how widespread this issue is by checking the length of each entry in the "Date" column.
date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()
# Looks like there are two more rows that has a date in a different format.
# Run the code cell below to obtain the indices corresponding to those rows and print the data.
indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
print(earthquakes.loc[indices])
# Given all of this information, it's your turn to create a new column "date_parsed" in the earthquakes dataset that has
# correctly parsed dates in it.
earthquakes.loc[3378, "Date"] = "02/23/1975"
earthquakes.loc[7512, "Date"] = "04/28/1985"
earthquakes.loc[20650, "Date"] = "03/13/2011"
earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")
# Create a Pandas Series day_of_month_earthquakes containing the day of the month from the "date_parsed" column.
day_of_month_earthquakes = earthquakes['date_parsed'].dt.day
# Plot the days of the month from your earthquake dataset.
sns.distplot(day_of_month_earthquakes, kde=False, bins=31)
