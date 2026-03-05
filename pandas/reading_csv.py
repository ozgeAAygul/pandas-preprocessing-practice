# CSV "Comma Separated Values"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#veriyi okuyalım
df = pd.read_csv('btc-market-price.csv', header=None)
#sütun isimleri olmadığından ilk satır öyle algılandı. Düzeltelim :üste header= None yazmam gerekiyor
# sütun isimlerini kendimiz verelim
df.columns = ["time", "value"]
#zaman değerini string olarak değil de datetime methodu ile zaman objesine çevirelim
df["time"] = pd.to_datetime(df["time"])
#zaman değerlerini yazdıralım
print(df["time"].head())
#dataframe indexini zaman değerleri yapalım
df.set_index("time", inplace=True)
#verinin ilk beş satırını yazdıralım
print(df.head(), "\n")
#istediğimiz zamandaki değeri .loc methodu ile bulabiliriz
print(df.loc["2017-04-04"])

# Veriyi Görselleştirme
#grafiği x ve y eksenlerindeki değerleri verek çizdirelim
df.plot()
plt.plot(df.index, df["value"])
plt.show() #bak bu sayede figür açıldı
