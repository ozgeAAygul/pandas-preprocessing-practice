import numpy as np
import pandas as pd

#dataframe oluşturalım
pokemon = pd.DataFrame({'atak': [49, 52, 40, 65, 44], 'savunma': [56, 78, 65, 23, 99], 'hiz': [87,94, 95, 29, 47], 'tur': ['tas', 'ates', 'su', 'kaya', 'cicek']}, index=["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Onix"])

#koşullu seçim yapalım
print(pokemon["hiz"] > 60)
#şimdi bunu dataframe üzerinden seçelim
print(pokemon.loc[pokemon["hiz"] > 60])
# sadece istediğimiz sutünu da seçebiliriz
print(pokemon.loc[pokemon["hiz"] > 60, "hiz"])
#veri silme yaparız
print(pokemon.drop("Bulbasaur"))
#birden çok da silersin
print(pokemon.drop(["Pikachu", "Onix"]))
#sutün da silebilirsin
print(pokemon.drop(["hiz", "tur"], axis=1))

#Operasyonlar
#birden fazla sutüna aynı anda işlem yapabiliriz
print(pokemon[["atak", "savunma"]] / 10)
#bak iki sutünu seçip ayrı şeyler ekleyebilirsin
print(pokemon[["atak", "savunma"]] + [10, 5])

# Dataframeleri değiştirme düzenleme 
#yrni sutün ekleyebilirsin
boylar = pd.Series([0.7, 0.6, 0.5, 0.4, 8.8], index=pokemon.index)
pokemon["boy"] = boylar
print(pokemon)
#bir sutündaki tüm değerleri değiştirme
pokemon["boy"] = 1
print(pokemon)
#yeniden adlandırma
pokemon = pokemon.rename(
  columns={
    "atak": "attack",
    "savunma": "defense",
    "tur": "type",
    "hiz": "speed",
    "boy": "height"
  }
)
print(pokemon)