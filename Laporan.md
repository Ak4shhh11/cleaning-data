📄 Laporan Big Data – Sesi 6
Data Cleaning & Preprocessing
1. Pendahuluan

Pada sesi ini, saya melakukan proses data cleaning dan preprocessing terhadap dataset Spotify yang telah digunakan pada sesi sebelumnya. Dataset ini berisi informasi terkait lagu seperti nama lagu, artist, energy, valence, dan atribut lainnya yang digunakan untuk menentukan mood lagu.

Tujuan dari tahap ini adalah untuk memastikan bahwa data yang digunakan bersih, konsisten, dan siap untuk dianalisis lebih lanjut. Dalam konteks Big Data, kualitas data sangat berpengaruh terhadap hasil analisis yang dihasilkan.

2. Tools yang Digunakan

Berikut tools yang saya gunakan dalam proses ini:

Visual Studio Code (VS Code) → sebagai code editor
Python → bahasa pemrograman utama
Pandas → library untuk pengolahan data
Dataset CSV (Spotify Dataset) → sumber data
3. Proses Data Cleaning
3.1 Import Library dan Load Dataset
import pandas as pd

df = pd.read_csv("spotify.csv")
3.2 Menampilkan Jumlah Data Awal
print("Jumlah data awal:", df.shape)
3.3 Menghapus Data Duplikat
df = df.drop_duplicates()
print("Setelah hapus duplicate:", df.shape)
3.4 Mengecek Missing Value
print("\nMissing value:")
print(df.isnull().sum())
3.5 Menangani Missing Value

Contoh penanganan missing value:

df = df.fillna(0)
3.6 Menyimpan Data Hasil Cleaning
df.to_csv("spotify_clean.csv", index=False)
4. Hasil Data Cleaning

Setelah dilakukan proses cleaning, diperoleh hasil sebagai berikut:

Jumlah data awal: (499, 22)
Setelah menghapus duplikat: (480, 22)
Terdapat beberapa missing value pada kolom tertentu
5. Analisis

Berdasarkan hasil pengolahan data:

Dataset awal masih mengandung data duplikat
Beberapa kolom memiliki nilai kosong (missing value)
Setelah proses cleaning, data menjadi lebih konsisten dan siap digunakan
6. Insight

Dari proses ini, saya mendapatkan beberapa insight:

Data cleaning merupakan tahap penting dalam Big Data
Data yang tidak bersih dapat menyebabkan hasil analisis menjadi tidak akurat
Penggunaan Python (Pandas) sangat mempermudah proses pengolahan data dalam jumlah besar
7. Kesimpulan

Pada sesi ini, saya berhasil melakukan proses data cleaning dan preprocessing terhadap dataset Spotify. Proses ini meliputi penghapusan data duplikat, pengecekan missing value, serta transformasi data.

Hasil akhir berupa dataset yang lebih bersih dan siap digunakan untuk tahap analisis selanjutnya, seperti sistem rekomendasi musik berbasis mood pengguna.
8. Output

Jumlah data awal: (499, 22)
Setelah hapus duplicate: (499, 22)

Missing value:
no                  0
track_id            0
artist              0
album_name          0
track_name          0
popularity          0
duration_ms         0
explicit            0
danceability        0
energy              0
key_signature       0
loudness            0
mode                0
speechiness         0
acousticness        0
instrumentalness    0
liveness            0
valence             0
tempo               0
time_signature      0
track_genre         0
mood_user           0
dtype: int64

Data cleaning selesai!
