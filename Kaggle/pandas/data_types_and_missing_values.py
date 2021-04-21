import pandas as pd

reviews = pd.read_csv("../data/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('max_rows', 5)

# Tipo de dato para una columna específica
type_price_review = reviews.price.dtype
# Lista de tipos de datos para todas las columnas de un dataframe
type_review = reviews.dtypes
# Convertir el tipo de dato de una columna
reviews.points.astype('float64')
# El index es un tipo entero
index_type = reviews.index.dtype
# Seleccionar filas con datos nullos para una columna
country_nan = reviews[pd.isnull(reviews.country)]
# Remplazar datos nulos de una columna o de todo el dataframe
reviews.region_2 = reviews.region_2.fillna("Unknown")
# Remplazar un dato por otro
reviews.taster_twitter_handle = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# EXERCISES

# What is the data type of the points column in the dataset?
type_points = reviews.points.dtype

# Cambiar a string el tipo de dato de la columna points
reviews.points = reviews.points.astype(str)

# Seleccionar los registros con precios nulos
price_null = len(reviews[pd.isnull(reviews.price)])
"""missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()"""

# Remplazar datos nullos de regiones y contar la cantidad de registros para cada una
reviews.region_1 = reviews.region_1.fillna("Unknown")
reviews_per_region = reviews.groupby(['region_1']).size().sort_values(ascending=False)

