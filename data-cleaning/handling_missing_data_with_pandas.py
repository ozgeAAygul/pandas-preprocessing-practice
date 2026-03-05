import pandas as pd
import numpy as np

#değer null mu kontrolü
value = np.nan #pd.isna da kullanabilirdin
print(pd.isnull(value))
print(pd.notnull(value))
#serilerde kontrol edersek fonksiyon da seri döndürür
print(pd.isnull(pd.Series([None, 2, np.nan, ""])))
#DataFrame kullanırsak
print(pd.isnull(pd.DataFrame({'Sütun A': [1, np.nan, 7], 'Sütun B': [np.nan, 2, np.nan] })))

print()

#Pandas ile NaN Değerlerde Işlem Yapma
#NaNı görmezden geldi
print(pd.Series([1, 2,np.nan]).sum())
#boş değerleri filtreleme
s = pd.Series([1, 2, np.nan, 4, np.nan])
print(s[pd.notnull(s)])
# boş verileri silme
print(s.dropna())

