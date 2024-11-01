kendaraan = ['Beat','motor',125,'hitam',2]
print(kendaraan)

kendaraan.append('18 Juta')  
kendaraan.append('matic') 
print(kendaraan)

kendaraan.insert(2,'honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))



hitung_luas= int(input("""pilih salah satu
1. Hitung Luas Persegi
2. Hitung Luas Lingkaran                   
3. Hitung Luas Segitiga
nomor berapa yang kamu pilih?                    
"""))

match hitung_luas:
    case 1:
        print('menghitung luas persegi')
        sisi=int(input('masukan nilai sisi: '))
        hitung_luas_persegi = sisi**2
        print(f'jadi luas persegi dengan sisi {sisi} cm, adalah {hitung_luas_persegi}cm^2')
    case 2:
        print('menghitung luas lingkaran')
        jari_jari=int(input('masukan nilai jari-jari: '))
        hitung_luas_lingkaran = 22/7*jari_jari**2
        print(f'jadi luas lingkaran dengan jari-jari {jari_jari} cm, adalah {hitung_luas_lingkaran}cm^2')
    case 3:
        print('menghitung luas segitiga')
        alas=int(input('masukan nilai alas: '))
        tinggi=int(input('masukan nilai tinggi: '))
        hitung_luas_segitiga = 1/2*alas*tinggi
        print(f'jadi luas lingkaran dengan alas {alas} cm dan tinggi {tinggi} cm, adalah {hitung_luas_segitiga}cm^2')
    case _:
        print('pilihan tidak valid')