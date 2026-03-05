import pandas as pd
import numpy as np

#Veri Temizleme
df = pd.DataFrame({'Sütun A': [1, np.nan, 30, np.nan], 'Sütun B': [2, 8, 31, np.nan], 'Sütun C': [np.nan, 9, 32, 100], 'Sütun D': [5, 8, 34, 110]})
#dropna silcek nan içeren satırları 
#print(df.dropna())

# nan içeren sütınları silmek için axisi 1 yapabilirsin
#print(df.dropna(axis=1))

# how parametresi için any ve all değerleri var allda eğer hepsi nullsa anyde eğer bi null varsa siler
df2 = pd.DataFrame({'Sütun A': [1, np.nan, 30], 'Sütun B': [2, np.nan, 31], 'Sütun C': [np.nan, np.nan, 100]})
#print(df2)

#tüm değerleri nan olan satırları silelim
#print(df2.dropna(how="all"))

#null değerleri doldurma
s = pd.Series([1, 2, np.nan, 4, np.nan])
#print(s)

#fillna methoduyla null değerleri 0 ile dolduralım
#print(s.fillna(0))

#şimdi de null değerleri serinin ortalamasıyla dolduralım
#print(s.fillna(s.mean()))

#ffill null değeri bi önceki değerle, bfill bi sonraki değerle doldurur
print(s.ffill())
print()
print(s.bfill())