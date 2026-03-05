import numpy as np
import pandas as pd

# bir dataframe oluşturalım
pokemon = pd.DataFrame({'atak': [49, 52, 40, 65, 44], 'savunma': [56, 78, 65, 23, 99], 'hiz': [87,94, 95, 29, 47], 'tur': ['tas', 'ates', 'su', 'kaya', 'cicek']}, index=["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Onix"])
print(pokemon)
# dataframe sutunlarina yani atak savunma falan sutun baslıklarına .columns ile erişilir
print(pokemon.columns)
# Dataframe hakkindaki bilgilere .info() methodu ile ulasabilirsin
print(pokemon.info())
#toplam değer sayısına da .size ile bakabilirsin başlıkları falan saymıyo satır ve sutun baslıklarını 
print(pokemon.size)
# sekline de shape ile bakabilirsin
print(pokemon.shape)
# dataframein sayısal değerleri yani ortalama standart sapma gibi .describe() methoduyla bakabilirsin
print(pokemon.describe())

# indexleme secme ve dilimleme
#istediğin sutuna erismek icin
print(pokemon["hiz"])
#satıra indexle erismek icin .iloc kullanılır
print(pokemon.iloc[-1])
# satira normal indexle ersmek icin .loc kullanılır
print(pokemon.loc["Pikachu"])
#Dataframede dilimlemeyi iki boyutlu yapabiliriz
print(pokemon.loc["Charmander": "Squirtle", "atak": "savunma"])