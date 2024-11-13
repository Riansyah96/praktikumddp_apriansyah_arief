# Tugas Mengecek Usia dan Status
usia = int(input("Masukkan usia: "))

if usia >= 18:
  print("Dewasa")
elif usia >= 13 and usia < 18:
  print("Remaja")
else:
  print("Anak-anak")