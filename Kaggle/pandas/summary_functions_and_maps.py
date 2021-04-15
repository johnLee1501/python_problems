import pandas as pd

pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)
reviews.describe()

# What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()