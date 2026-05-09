

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
