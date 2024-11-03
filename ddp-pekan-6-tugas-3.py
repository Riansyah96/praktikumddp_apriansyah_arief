# Meminta input dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris yang ingin dicetak: "))

# Menggunakan loop untuk mencetak bintang
for i in range(1, jumlah_baris + 1):
    print("* " * i)  # Mencetak bintang sebanyak i kali