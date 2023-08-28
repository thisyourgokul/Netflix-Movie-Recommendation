# -*- coding: utf-8 -*-
"""Eclat_Association_Rule_Learning_Netflix-Movie-Recommendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_zxtImmRdbiYc7XWQeXLUvcoAERSQMlo

# Eclat

## Importing libraries
"""

!pip install apyori

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing dataset"""

dataset = pd.read_csv('Movie Recommendation.csv', header = None)
transactions = []
for i in range(0, 7466):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

"""## Eclat Training on Dataset"""

from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

"""## Visualizing

### Raw Results
"""

results = list(rules)

results

"""### Proper Display"""

def inspect(results):
    movie_1         = [tuple(result[2][0][0])[0] for result in results]
    movie_2         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(movie_1, movie_2, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Movie 1', 'Movie 2', 'Support'])

resultsinDataFrame

resultsinDataFrame.nlargest(n = 10, columns = 'Support')