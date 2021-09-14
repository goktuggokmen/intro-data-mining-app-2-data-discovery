# -*- coding: utf-8 -*-
"""EEM 314 Veri Madenciliğine Giriş Uygulama 2 :  Veri Keşfi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sfTPGmOELxANv5HE9OMUUZkRAKZJWoz4

# **1.   Kütüphaneler**
"""

#kütüphaneleri import ediyoruz.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""# **2. Dataların Okunması**"""

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data") #datanın dosyadan okunması.

"""# **3. Kolonların Atanması**"""

cols = ['sepal length', 'sepal width','petal length', 'petal width', 'class'] #kolonların atanması.
data.columns = cols

"""# **4. Her Bir Niceliğin Özelliklerinin Tespit Edilmesi**

**4.1. Sepal Length**
"""

sepal_length = data['sepal length']
print("Ortalama :" , sepal_length.mean())
print("Standart Sapma :" , sepal_length.std())
print("Min. Değer :" , sepal_length.min())
print("Max. Değer :" , sepal_length.max())

"""4.2. Sepal Width"""

sepal_width = data['sepal width']
print("Ortalama :" , sepal_width.mean())
print("Standart Sapma :" , sepal_width.std())
print("Min. Değer :" , sepal_width.min())
print("Max. Değer :" , sepal_width.max())

"""4.3. Petal Length"""

petal_length = data['petal length']
print("Ortalama :" , petal_length.mean())
print("Standart Sapma :" , petal_length.std())
print("Min. Değer :" , petal_length.min())
print("Max. Değer :" , petal_length.max())

"""4.4. Petal Width"""

petal_width = data['petal width']
print("Ortalama :" , petal_width.mean())
print("Standart Sapma :" , petal_width.std())
print("Min. Değer :" , petal_width.min())
print("Max. Değer :" , petal_width.max())

"""# **5. Her Sınıftan Kaçar Örnek Olduğunun Belirlenmesi**"""

data['class'].value_counts()

"""# **6. Tüm Kolonların İstatistikleri**"""

data.describe(include='all')

"""# **7. Dataların Kovaryans Ve Kolerasyonlarının Hesaplanması**

**7.1. Kovaryans**

Kovaryans , iki rastgele değişkenin beklenen değerlerinden toplam varyasyonunu ölçer. Kovaryansı kullanarak, yalnızca ilişkinin yönünü ölçebiliriz (değişkenler birbiri ardına hareket etme eğilimi gösterme veya ters ilişki gösterme eğilimi). Ancak, ilişkinin gücünü veya değişkenler arasındaki bağımlılığı göstermez.

Pozitif kovaryans : İki değişkenin aynı yönde hareket etme eğiliminde olduğunu gösterir. 

Negatif kovaryans : İki değişkenin ters yönde hareket etme eğiliminde olduğunu ortaya çıkarır.
"""

data.cov()

"""**7.2. Korelasyon**

Korelasyon, iki veya daha fazla değişken arasında bir ilişki olup olmadığını, eğer ilişki varsa bu ilişkinin miktarını ve yönünü sayısal olarak belirlememizi sağlayan istatistiksel bir tekniktir. İki değişken arasındaki ilişkinin derecesine ise korelasyon katsayısı denir.

Hesaplanan korelasyon katsayısı -1 ile +1 arasında değer alır. -1’den küçük ve +1’den büyük olamaz. Korelasyonun pozitif (+) olması durumunda değişkenler aynı yönde değişmiş demektir. Korelasyon katsayısının + olması iki değişkenin aynı yönde bir ilişkide olduğunu, negatif (-) olması ise iki değişkenin arasında ters yönde bir ilişki olduğunu gösterir.  Eğer değişkenlerdeki artış veya azalış birbirine bağlı değilse korelasyon sıfır olur. Bu da değişkenler arasında ilişki yok anlamına gelir.
"""

data.corr()

"""# **8. Özniteliklerin Histogram Grafiklerinin Çizdirilmesi**"""

data.hist(bins = 8,color = '#ee104e',xlabelsize = 8,ylabelsize = 8)
plt.tight_layout(rect=(0,0,2,2))

"""# **9. Her Bir Sınıf İçin Özniteliklere Ait Box Plotların Çizdirilmesi**

**9.1. Sepal Length**
"""

plt.figure(figsize=(8,8))
sns.boxplot(x = 'class',y = 'sepal length',data = data)

"""**9.2. Sepal Width**"""

plt.figure(figsize=(8,8))
sns.boxplot(x = 'class',y = 'sepal width',data = data)

"""**9.3. Petal Length**"""

plt.figure(figsize=(8,8))
sns.boxplot(x = 'class',y = 'petal length',data = data)

"""**9.4. Petal Width**"""

plt.figure(figsize=(8,8))
sns.boxplot(x = 'class',y = 'petal width',data = data)

"""# **10. Her Öznitelik Çifti İçin Ortak Dağılımları Gösteren Scatter Plot Çizdirme**"""

oznitelikler = ['sepal length', 'sepal width','petal length', 'petal width']
pp = sns.pairplot(data[oznitelikler],height = 2,aspect = 2,plot_kws = dict(edgecolor="r",linewidth = 0.5),diag_kind = "kde",diag_kws = dict(shade=True))

"""# **11. Datayı Paralel Koordinatlar Şeklinde Çizdirme**"""

plt.figure(figsize = (8,8))
pd.plotting.parallel_coordinates(data[['class','sepal length', 'sepal width','petal length', 'petal width']],'class')
plt.show()

"""# **12. Kaynaklar**

1. http://www.kpsskonu.com/egitim-bilimleri/olcme-ve-degerlendirme/korelasyon-katsayisi/
2. https://tr.pharoskc.com/12-what-is-covariance
3. https://benalexkeen.com/parallel-coordinates-in-matplotlib/
4.
"""