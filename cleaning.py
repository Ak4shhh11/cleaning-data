import pandas as pd

# Load data
df = pd.read_csv("spotify.csv")

# Tampilkan jumlah awal
print("Jumlah data awal:", df.shape)

# Hapus duplikat
df = df.drop_duplicates()

# Tampilkan setelah hapus
print("Setelah hapus duplicate:", df.shape)

# Cek missing value
print("\nMissing value:")
print(df.isnull().sum())

# Simpan hasil
df.to_csv("spotify_clean.csv", index=False)

print("\nData cleaning selesai!")