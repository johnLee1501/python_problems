import pandas as pd

reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# Agrupa el dataframe por puntos y suma el numero de apariciones de cada puntaje
count_points_occurrence = reviews.groupby('points').points.count()

# To get the cheapest wine in each point value category, we can do the following
cheap_wine_by_point = reviews.groupby('points').price.min()

# here's one way of selecting the name of the first wine reviewed from each winery in the dataset
first_wine_by_group = reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# For even more fine-grained control, you can also group by more than one column. For an example,
# here's how we would pick out the best wine by country and province:
best_wine_by_country_and_province = reviews.groupby(['country', 'province']).apply(
    lambda df: df.loc[df.points.idxmax()])

# we can generate a simple statistical summary of the dataset as follows
summary_country_price = reviews.groupby(['country']).price.agg([len, min, max])

# A multi-index differs from a regular index in that it has multiple levels. For example
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

# MultiIndex
mi = countries_reviewed.index
type(mi)

# However, in general the multi-index method you will use most often is the one for converting back to a regular index,
# the reset_index() method
countries_reviewed = countries_reviewed.reset_index()
# To get data in the order want it in we can sort it ourselves. The sort_values() method is handy for this.
countries_reviewed_ordered_by_len = countries_reviewed.sort_values(by='len')
# sort_values() defaults to an ascending sort, where the lowest values go first. However, most of the time we want a
# descending sort, where the higher numbers go first. That goes thusly:
countries_reviewed_ordered_by_len_descending = countries_reviewed.sort_values(by='len', ascending=False)
# To sort by index values, use the companion method sort_index(). This method has the same arguments and default order
countries_reviewed_ordered_by_len.sort_index()
# Finally, know that you can sort by more than one column at a time
countries_reviewed.sort_values(by=['country', 'len'])
