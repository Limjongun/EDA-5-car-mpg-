# ============================================================
# EDA MPG DATASET
# Exploratory Data Analysis pada Dataset Mobil
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 1. LOAD DATASET
# ============================================================

# Load dataset mpg dari seaborn.
# Dataset ini berisi informasi mobil seperti:
# mpg, cylinders, displacement, horsepower, weight,
# acceleration, model_year, origin, dan name.
df = sns.load_dataset('mpg')

# Menampilkan 5 data pertama
print("Head:")
print(df.head())

# Menampilkan 5 data terakhir
print("\nTail:")
print(df.tail())


# ============================================================
# 2. DATA OVERVIEW
# ============================================================

# Menampilkan nama-nama kolom
print("\nColumns:")
print(df.columns)

# Melihat jumlah baris dan kolom
print("\nShape:")
print(df.shape)

# Melihat informasi dataset:
# - tipe data
# - jumlah non-null
# - jumlah kolom
# - penggunaan memory
print("\nInfo:")
print(df.info())

# Melihat statistik deskriptif:
# count, mean, std, min, Q1, median, Q3, max
print("\nStatistik deskriptif:")
print(df.describe())

# Insight awal:
# Dataset mpg berisi data mobil dengan fitur numerik dan kategorikal.
# Fitur numerik utama:
# mpg, cylinders, displacement, horsepower, weight,
# acceleration, dan model_year.
#
# Fitur kategorikal:
# origin dan name.
#
# mpg menjadi variabel penting karena menunjukkan efisiensi bahan bakar.
# Semakin tinggi mpg, semakin hemat mobil tersebut.


# ============================================================
# 3. CEK MISSING VALUE
# ============================================================

print("\nMissing value:")
print(df.isnull().sum())

missing_percent = df.isnull().sum() / len(df) * 100

print("\nMissing value percentage:")
print(missing_percent)

# Insight:
# Dataset mpg memiliki missing value pada kolom horsepower.

#
# Pada EDA ini, missing value cukup dicatat dulu.
# Jika nanti masuk preprocessing/modeling, horsepower bisa diisi
# dengan median atau di-handle sesuai kebutuhan.


# ============================================================
# 4. CEK DATA DUPLIKAT
# ============================================================

print("\nJumlah data duplikat:")
print(df.duplicated().sum())

duplicated_row = df[df.duplicated()]

print("\nData duplikat:")
print(duplicated_row)

# Insight:
# Jika jumlah duplikat 0, berarti tidak ada baris yang sama persis.
# Jika ada, perlu dicek konteksnya sebelum dihapus.


# ============================================================
# 5. ANALISIS FITUR KATEGORIKAL
# ============================================================

# origin menunjukkan asal mobil:
# usa, japan, europe

categorical_column = ['origin']

for column in categorical_column:
    print(f"\nValue count untuk kolom {column}:")
    print(df[column].value_counts(dropna=False))

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=column)
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel("Jumlah")
    plt.show()

# Insight:
# Mobil dari USA adalah yang paling banyak dalam dataset.
# Jumlah mobil USA jauh lebih dominan dibanding Japan dan Europe.
# Ini penting karena pola keseluruhan dataset bisa sangat dipengaruhi
# oleh karakter mobil USA.


# ============================================================
# 6. ANALISIS FITUR NUMERIK
# ============================================================

numeric_column = [
    'mpg',
    'cylinders',
    'displacement',
    'horsepower',
    'weight',
    'acceleration',
    'model_year'
]

for column in numeric_column:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x=column, kde=True)
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# Insight:
# - mpg paling banyak berada di rentang rendah-menengah, sekitar 12 sampai 25.
# - cylinders didominasi oleh 4, 6, dan 8 silinder.
# - displacement cenderung berkumpul di nilai kecil-menengah,
#   lalu menurun ke sisi kanan.
# - horsepower juga cenderung lebih banyak di nilai rendah-menengah.
# - weight banyak berada di sekitar 2000 sampai 3500.
# - acceleration cukup terkonsentrasi di tengah.
# - model_year cukup tersebar, karena data berasal dari beberapa tahun produksi.


# ============================================================
# 7. ANALISIS MPG
# ============================================================

# mpg = miles per gallon
# Semakin tinggi mpg, semakin hemat konsumsi bahan bakar mobil.

print("\nStatistik MPG:")
print(df['mpg'].describe())

plt.figure(figsize=(6, 4))
sns.histplot(data=df, x='mpg', kde=True)
plt.title("Distribusi MPG")
plt.xlabel("MPG")
plt.ylabel("Frequency")
plt.show()

# Insight:
# MPG menunjukkan efisiensi bahan bakar.
# Mobil dengan mpg rendah berarti lebih boros.
# Mobil dengan mpg tinggi berarti lebih hemat.


# ============================================================
# 8. HUBUNGAN WEIGHT DAN MPG
# ============================================================

# Untuk melihat hubungan dua variabel numerik,
# scatterplot lebih tepat daripada histplot.
#
# Di sini kita ingin melihat apakah berat mobil memengaruhi efisiensi bahan bakar.

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='weight', y='mpg')
plt.title("Hubungan Weight dan MPG")
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()

# Insight:
# Terlihat pola menurun dari kiri ke kanan.
# Artinya, semakin berat mobil, mpg cenderung semakin rendah.
# Dengan kata lain, mobil yang lebih berat cenderung lebih boros bahan bakar.


# ============================================================
# 9. HUBUNGAN HORSEPOWER DAN MPG
# ============================================================

plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='horsepower', y='mpg')
plt.title("Hubungan Horsepower dan MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()

# Insight:
# Semakin tinggi horsepower, mpg cenderung semakin rendah.
# Artinya, mobil dengan tenaga besar cenderung lebih boros bahan bakar.
# Ini masuk akal karena tenaga besar biasanya membutuhkan konsumsi energi lebih besar.


# ============================================================
# 10. WEIGHT VS MPG BERDASARKAN ORIGIN
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='weight', y='mpg', hue='origin')
plt.title("Weight vs MPG Berdasarkan Origin")
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()

# Insight:
# Mobil USA banyak berkumpul di area weight tinggi dan mpg rendah.
# Artinya, mobil USA dalam dataset ini cenderung lebih berat dan lebih boros.
#
# Mobil Japan dan Europe lebih banyak berada di area weight rendah-menengah
# dan mpg lebih tinggi.
# Artinya, mobil Japan dan Europe cenderung lebih ringan dan lebih hemat.


# ============================================================
# 11. BOXPLOT MPG BERDASARKAN ORIGIN
# ============================================================

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='origin', y='mpg')
plt.title("Distribusi MPG Berdasarkan Origin")
plt.xlabel("Origin")
plt.ylabel("MPG")
plt.show()

# Cara baca boxplot:
# - Garis tengah box = median
# - Box = 50% data tengah
# - Whisker = rentang data normal
# - Titik di luar whisker = kandidat outlier
#
# Insight:
# Mobil Japan memiliki median mpg paling tinggi.
# Artinya, mobil Japan cenderung paling hemat bahan bakar.
#
# Mobil USA memiliki median mpg paling rendah.
# Artinya, mobil USA cenderung paling boros.
#
# Mobil Europe berada di tengah, lebih hemat daripada USA
# tetapi umumnya tidak setinggi Japan.


# ============================================================
# 12. BOXPLOT HORSEPOWER BERDASARKAN ORIGIN
# ============================================================

plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x='origin', y='horsepower')
plt.title("Distribusi Horsepower Berdasarkan Origin")
plt.xlabel("Origin")
plt.ylabel("Horsepower")
plt.show()

# Insight:
# Mobil USA memiliki horsepower yang cenderung lebih tinggi
# dibanding Japan dan Europe.
#
# Ini sejalan dengan pola sebelumnya:
# horsepower tinggi dan weight tinggi berkaitan dengan mpg yang lebih rendah.


# ============================================================
# 13. RATA-RATA BERDASARKAN ORIGIN
# ============================================================

print("\nRata-rata mpg berdasarkan origin:")
print(df.groupby('origin')['mpg'].mean().sort_values(ascending=False))

print("\nRata-rata weight berdasarkan origin:")
print(df.groupby('origin')['weight'].mean().sort_values(ascending=False))

print("\nRata-rata horsepower berdasarkan origin:")
print(df.groupby('origin')['horsepower'].mean().sort_values(ascending=False))

# Insight:
# Groupby membantu memperjelas angka dari visualisasi.
# Dari rata-rata ini, kita bisa membandingkan origin mana yang:
# - paling hemat berdasarkan mpg
# - paling berat berdasarkan weight
# - paling bertenaga berdasarkan horsepower


# ============================================================
# 14. CORRELATION HEATMAP
# ============================================================

# Mengambil kolom numerik saja
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# Menghitung korelasi antar fitur numerik
correlation = numeric_df.corr()

print("\nCorrelation matrix:")
print(correlation)

plt.figure(figsize=(9, 6))
sns.heatmap(correlation, annot=True, fmt=".2f")
plt.title("Correlation Heatmap MPG Dataset")
plt.show()

# Cara baca korelasi:
#  1.00  = hubungan positif sangat kuat
#  0.00  = hampir tidak ada hubungan linear
# -1.00  = hubungan negatif sangat kuat
#
# Insight:
# - mpg berkorelasi negatif kuat dengan weight, horsepower,
#   displacement, dan cylinders.
# - Artinya, semakin besar/berat/bertenaga mobil,
#   mpg cenderung semakin rendah.
#
# - cylinders dan displacement memiliki korelasi positif kuat.
#   Artinya, mobil dengan jumlah silinder lebih besar biasanya
#   memiliki displacement lebih besar.
#
# - weight dan displacement juga sangat berkaitan,
#   karena mobil bermesin besar biasanya lebih berat.
#
# - model_year biasanya berkorelasi positif dengan mpg.
#   Artinya, mobil keluaran tahun lebih baru cenderung lebih hemat.


# ============================================================
# 15. PAIRPLOT
# ============================================================

# Pairplot digunakan untuk melihat banyak hubungan antar fitur sekaligus.
# Diagonal menunjukkan distribusi masing-masing fitur.
# Bagian luar diagonal menunjukkan hubungan antar dua fitur.

sns.pairplot(
    df[['mpg', 'horsepower', 'weight', 'acceleration', 'origin']],
    hue='origin'
)

plt.show()

# Insight pairplot:
# - mpg vs weight menunjukkan pola negatif kuat.
#   Semakin berat mobil, mpg semakin rendah.
#
# - mpg vs horsepower juga menunjukkan pola negatif.
#   Semakin tinggi horsepower, mpg cenderung turun.
#
# - horsepower vs weight menunjukkan pola positif.
#   Mobil yang lebih berat cenderung memiliki horsepower lebih besar.
#
# - Mobil USA terlihat dominan pada area weight dan horsepower tinggi,
#   tetapi mpg rendah.
#
# - Mobil Japan dan Europe banyak muncul pada area weight lebih rendah
#   dan mpg lebih tinggi.
#
# - Pada diagonal, distribusi setiap fitur terlihat berbeda antar origin.
#   USA memiliki distribusi weight dan horsepower lebih tinggi,
#   sedangkan Japan dan Europe lebih terkonsentrasi pada mobil ringan.


# ============================================================
# 16. FINAL INSIGHT
# ============================================================

print("""
FINAL INSIGHT MPG DATASET:

1. Dataset mpg berisi data karakteristik mobil seperti mpg,
   cylinders, displacement, horsepower, weight, acceleration,
   model_year, origin, dan name.

2. Dataset memiliki missing value pada kolom horsepower.
   Missing value ini perlu ditangani jika nanti masuk preprocessing/modeling.

3. Mobil dari USA adalah yang paling banyak dalam dataset.
   Dataset cukup didominasi oleh mobil asal USA.

4. mpg adalah indikator efisiensi bahan bakar.
   Semakin tinggi mpg, semakin hemat mobil tersebut.

5. Weight memiliki hubungan negatif kuat dengan mpg.
   Semakin berat mobil, mpg cenderung semakin rendah.

6. Horsepower juga memiliki hubungan negatif dengan mpg.
   Mobil yang lebih bertenaga cenderung lebih boros bahan bakar.

7. Mobil USA cenderung lebih berat, memiliki horsepower lebih tinggi,
   dan mpg lebih rendah.

8. Mobil Japan dan Europe cenderung lebih ringan dan memiliki mpg lebih tinggi.

9. Heatmap menunjukkan bahwa cylinders, displacement, horsepower,
   dan weight saling berkaitan kuat.

10. Pairplot memperkuat insight bahwa ukuran dan tenaga mobil
    sangat berhubungan dengan efisiensi bahan bakar.

11. Dataset mpg cocok untuk latihan EDA karena memiliki:
    - data numerik
    - data kategorikal
    - missing value
    - korelasi kuat
    - pola scatterplot yang mudah dibaca
    - perbedaan karakteristik berdasarkan origin
""")