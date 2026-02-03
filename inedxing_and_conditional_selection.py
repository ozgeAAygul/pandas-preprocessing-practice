import pandas as pd
import numpy as np

series = pd.Series({'Bulbasaur': 49, 'Charmander': 43, 'Pikachu': 40}, name='Pokemon Savunma Güçleri')
# bir index değerini keyine göre olma
print(series['Pikachu'])
# bir index değerini indexe göre alma
print(series.iloc[0])
# birden fazla indexi seri olarak döndürme
print(series[['Pikachu', 'Bulbasaur']]) # iki köşeli parantez var dikkat et
print(series.iloc[[0,1]]) 
# slicingle döndürme burada son değer de eklenir
print(series['Bulbasaur': 'Pikachu'])
# koşullu seçim
print(series > 45) # true false olarak döndürür
print(series[series > 45]) # conditionu sağlayanları serie olarak döndürür
# bazı fonksiyonları var
print(series.mean())
# series[(condition) &/|gibi şeyler (condititon)]
# seride bi indexin değerini değiştirmek istedik
# pikachu güçlendi yuhuuu
series['Pikachu'] = 70 # istersen şey de yaparsın picachu yerine condition yazarsın hepsini bi değere eşitlersin
