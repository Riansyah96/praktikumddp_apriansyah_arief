# tugas Pembelian Diskon
# Harga_Minyak = 25000
# Harga_Indomie = 5000
# Harga_Beras = 75000

# total_Minyak_dibeli = int(input("Minyak "))
# total_Indomie_dibeli = int(input("Indomie "))
# total_Beras_dibeli = int(input("Beras "))

# total_seluruh_barang_dibeli = ((total_Beras_dibeli)+(total_Indomie_dibeli)+(total_Minyak_dibeli))
# total_seluruh_harga = ((Harga_Beras*total_Beras_dibeli)+(Harga_Indomie*total_Indomie_dibeli)+(Harga_Minyak*total_Minyak_dibeli))

# if total_seluruh_barang_dibeli >= 100:
#      print("Selamat! Anda mendapatkan diskon 10%, harga menjadi."(total_seluruh_harga*0.1))
# else:
#      print(total_seluruh_harga)


# #daftar harga barang satuan
# harga_barang = {
#     "minyak":25000,
#     "indomie":5000,
#     "beras":75000,
#     "gula":25000,
#     "kopi":20000,
#     "teh":10000
# }

# # meminta pengguna memasukan jumlah pembelian untuk setiap barang
# jumlah_minyak=int(input("masukan jumlah minyak yang dibeli: "))
# jumlah_indomie=int(input("masukan jumlah indomie yang dibeli: "))
# jumlah_beras=int(input("masukan jumlah beras yang dibeli: "))
# jumlah_gula=int(input("masukan jumlah gula yang dibeli: "))
# jumlah_kopi=int(input("masukan jumlah kopi yang dibeli: "))
# jumlah_teh=int(input("masukan jumlah teh yang dibeli: "))

# # menghitung total harga
# total_harga=(
#     jumlah_minyak*harga_barang["minyak"]+
#     jumlah_indomie*harga_barang["indomie"]+
#     jumlah_beras*harga_barang["beras"]+
#     jumlah_gula*harga_barang["gula"]+
#     jumlah_kopi*harga_barang["kopi"]+
#     jumlah_teh*harga_barang["teh"]
# )

# #menghitung total harga debgan atau diskon menggunakan shorthand if
# total_harga_setelah_diskon = total_harga*0.1 if total_harga > 100000 else total_harga

# #mencetak hasil harga setelah diskon (jika ada) atau tanpa diskon
# print(f"Total harga yang harus dibayar : {total_harga_setelah_diskon}")

#  Soal 5: Pembelian Diskon
minyak = 25000
indomie = 5000
beras = 75000
gula = 25000
kopi = 20000
teh = 10000

Jminyak = int(input('berapa minyak yang di beli?'))
Jindomie = int(input('berapa indomie yang di beli?'))
Jberas = int(input('berapa beras yang di beli?'))
Jgula = int(input('berapa gula yang di beli?'))
Jkopi = int(input('berapa kopi yang di beli?'))
Jteh = int(input('berapa teh yang di beli?'))

TH = Jminyak+Jindomie+Jberas+Jgula+Jkopi+Jteh

Hm = Jminyak*minyak
Hi = Jindomie*indomie
Hb = Jberas*beras
Hg = Jgula*gula
Hk = Jkopi*kopi
Ht = Jteh*teh

jumlah = Hm+Hi+Hb+Hg+Hk+Ht

if  TH > 100 :
    jumlah_akhir = jumlah-(jumlah * 0.1)
    print('anda dapt diskon 10%, sehingga total belanja anda adalah Rp', int(jumlah_akhir))
else:
    print('total belanja anda adalah Rp', jumlah)