import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as st

import matplotlib.pyplot as plt

dataset = pd.read_csv("temperature.csv", sep=";", encoding='ISO-8859-1')

print (dataset.head())

milanoData = dataset['Milan']
moyenne = np.mean(milanoData)

# la fonction round est juste pour arrondir a deux nombre apres virgule
print ("La Moyenne de degree a milan est : ", round(moyenne, 2))

mediane = np.median(milanoData)
print ("La mediane de degree a milan est : ", round(mediane, 2))


variance = np.var(milanoData)
print ("La variance de degree a milan est : ", round(variance, 2))


ecartType = np.std(milanoData)
print ("Le ecart type de degree a milan est : ", round(ecartType, 2))

# On calcule le quantile 0,5 qui n'est rien d'autre que la mediane
print("Le Quantile 0,5 vaut : " , np.percentile(milanoData, 50))

# On calcule le quantile 0,25 qui est le quartile Q1
Q1 = round(np.percentile(milanoData, 25))
print("Quartile Q1 vaut : ", Q1)

# On calcule le quantile 0,75 qui est le quartile Q3
Q3 = round(np.percentile(milanoData, 75))
print("Quartile Q3 vaut : ", round(np.percentile(milanoData, 75)))

# L ecart interquartile est Q3 - Q1
print("L ecart interquartile vaut : ", Q3 - Q1)