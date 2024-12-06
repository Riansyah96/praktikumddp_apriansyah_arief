import math

def luas_persegi(sisi):
    """Menghitung luas persegi."""
    hasil = sisi * sisi
    print("hasil Luas Persegi dari sisi",sisi,"=",hasil)


def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang."""
    hasil = panjang * lebar
    print("hasil Luas Persegi Panjang dari sisi",panjang,"sisi",lebar,"=",hasil)

def luas_segitiga(alas, tinggi):
    """Menghitung luas segitiga."""
    hasil = alas * tinggi
    print("hasil Luas Segitiga dari alas",alas,"tinggi",tinggi,"=",hasil)

def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran."""
    hasil = math.pi * (jari_jari ** 2)
    print("hasil Luas Persegi dari jari-jari",jari_jari,"=",hasil)

def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    """Menghitung luas trapesium."""
    hasil = 0.5 * (sisi_atas + sisi_bawah) * tinggi
    print("hasil Luas Trapesium dari sisi atas",sisi_atas,"sisi bawah",sisi_bawah,"tinggi",tinggi,"=",hasil)