import pandas as pd

pd.set_option('max_rows', 5)
reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)
# Rename column
reviews.rename(columns={'points': 'score'})

# Rename index
reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# Rename row index and column index
reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

# Concat two csv
canadian_youtube = pd.read_csv("../data/CAvideos.csv")
british_youtube = pd.read_csv("../data/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

# The middlemost combiner in terms of complexity is join(). join() lets you combine different DataFrame objects which
# have an index in common. For example, to pull down videos that happened to be trending on the same day in both Canada
# and the UK, we could do the following:

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

# EXERCISES

# region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews with
# these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'})

# Set the index name in the dataset to wines
reindexed = reviews.rename_axis("wines", axis='rows')

gaming_products = pd.read_csv("../data/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../data/movies.csv")
movie_products['subreddit'] = "r/movies"
# Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])

"""powerlifting_meets = pd.read_csv("../input/powerlifting-database/meets.csv")
powerlifting_competitors = pd.read_csv("../input/powerlifting-database/openpowerlifting.csv")

# Both tables include references to a MeetID, a unique key for each meet (competition) included in the database.
# Using this, generate a dataset combining the two tables into one.
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))"""
