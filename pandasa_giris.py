import pandas as pd
import numpy as np

# seri oluşturma
g3_pop = pd.Series([1.558, 4.504, 5.908])
print(g3_pop)

# name atama
g3_pop.name = "Population"
print(g3_pop)

# data typeına bakma
print(g3_pop.dtype)

# valuesa bakma 
print(g3_pop.values)

# typeına bakma
print(type(g3_pop))

# belli indexlere erişme
print(g3_pop[0])

# indexlere bakma
print(g3_pop.index)

# index değiştirme
g3_pop.index = ['Hatay', 'Izmir', 'Ankara']
print(g3_pop)

'''
bak şu şekilde de oluşturabilirdin aynı serieyi
pd.Series([1.558, 4.504, 5.908], index= ['Hatay', 'Izmir', 'Ankara'], name='Population')
ya da 
pd.Series({'Hatay': 1.558, 'Izmir': 4.504, 'Ankara': 5.908}, name='Population')
'''