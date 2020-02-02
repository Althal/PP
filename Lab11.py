#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("Zadanie 1")
from sklearn.datasets import load_boston
boston_dataset = load_boston()
print(boston_dataset.keys())
pdObj = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
pdObj['MEDV'] = pd.Series(boston_dataset.target)
print(pdObj.head(10))
print(pdObj.tail(10))

print("Zadanie 2")
print(pdObj.info())

print("Zadanie 3")
print(pdObj.describe())

print("Zadanie 4")
sns.distplot(pdObj['MEDV'])
plt.show()

print("Zadanie 5")
correlations= pdObj.corr()
print(correlations)
sns.heatmap(correlations)
plt.show()

