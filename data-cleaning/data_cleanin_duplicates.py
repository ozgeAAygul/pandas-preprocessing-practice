import pandas as pd
import numpy as np

#Tekrarlanan Değerler
elciler = pd.Series([
  'France',
  'United Kingdom',
  'United Kingdom',
  'Italy',
  'Germany',
  'Germany',
  'Germany',
], index=[
  'Gérard Araud',
  'Kim Darroch',
  'Peter Westmacott',
  'Armando Varricchio',
  'Peter Wittig',
  'Peter Ammon',
  'Klaus Scharioth'
])
print(elciler)
#duplicated methodu bize tekrarlanan değerleri verir üstten aşağı doğru bakar keep="last" eklersek aşağıdan üste doğru bakar
print(elciler.duplicated())
print()
print(elciler.duplicated(keep="last"))
#keepe False verirsek tekrarlanan tüm değerleri verir
print(elciler.duplicated(keep=False))
#drop_duplicates methoduyla tekrarlanan değerleri silebiliriz aynı zamanda keep ile değer atayabiliriz
print(elciler.drop_duplicates(keep=False))
print(elciler.drop_duplicates(keep="first"))

#Metin İşleme
#Sütunlara Ayırma
df = pd.DataFrame({
    'Veri': [
        '1987_E_ABD _1',
        '1990?_E_ING_1',
        '1992_K_ABD_2',
        '1970?_E_ IT_1',
        '1985_K_I T_2'
]})
#pandas str arayüzü ile string methodlarını kullanmamızı sağlar
print(df["Veri"].str.split("_"))
#expand parametresini True yaparak parçalanan verileri sütunlara ayırabiliriz
print(df["Veri"].str.split("_", expand=True))
#sütunları ayıralım
df = df["Veri"].str.split("_", expand=True)
#sütun isimlerini değiştirelim
df.columns = ["Yil", "Cinsiyet", "Ulke", "Cocuk Sayisi"]
print(df)
#veride herhangi bir metin ya daa karakter bulunuyor mu diye kontrol etmek için contains methodu kullanılır
print(df["Yil"].str.contains("\?"))
#replace methodu kullanabiliriz
df["Yil"] = df["Yil"].str.replace("?", "")
print(df)
#ülke ismindeki boşlukları silebiliriz
df["Ulke"] = df["Ulke"].str.replace(" ", "")
print(df)