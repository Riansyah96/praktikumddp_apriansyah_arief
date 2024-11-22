print()
print('## Nomor 1 ##')
def celsius_ke_fahrenheit(celsius):
    konversi=(celsius*9/5)+32
    return konversi
print(celsius_ke_fahrenheit(0)) #32
print(celsius_ke_fahrenheit(100)) #212

print()
print('## Nomor 2 ##')
def ganjil_genap(bilangan):
    penentuan = bilangan % 2 == 0
    return penentuan
print(ganjil_genap(4)) #true
print(ganjil_genap(7)) #false

print()
print('## Nomor 3 ##')
def keterangan(nilai):
    if nilai >= 80:
        print("lulus")
    elif nilai <= 60:
        print("Gagal")
    else :
        print("tidak valid")

keterangan(80)
keterangan(60)

print()
print('## Nomor 4 ##')
def bilangan_ganjil(range_akhir):
    return [i for i in range(1,range_akhir,2)]
print(bilangan_ganjil(20))