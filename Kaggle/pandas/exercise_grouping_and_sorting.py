import pandas as pd

reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)

# Conteo de revisiones de vinos
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()
"""reviews_written = reviews.groupby('taster_twitter_handle').size()"""

# Lista del mejor vino para cada precio
best_rating_per_price = reviews.groupby('price').points.max()

# Lista del vino más caro y más barato para cada precio
price_extremes = reviews.groupby('variety').price.agg([min, max])

# Lista del vino más caro y más barato para cada precio ordenado descendentemente
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Lista de promedio de puntuación para todos los testers de vinos
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Análisis de lista de promedios puntuación testers
reviewer_mean_ratings.describe()

# Conteo de vinos por país y variedad y ordenamiento descendente
reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)

