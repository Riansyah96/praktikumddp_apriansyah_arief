import math

def luas_kubus(sisi):
    """Menghitung luas permukaan kubus."""
    hasil = 6 * (sisi ** 2)
    print("hasil Luas kubus dari sisi",sisi,"=",hasil)

def luas_balok(panjang, lebar, tinggi):
    """Menghitung luas permukaan balok."""
    hasil = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    print("hasil Luas balok dari panjang",panjang,",lebar",lebar,",tinggi",tinggi,"=",hasil)

def luas_tabung(jari_jari, tinggi):
    """Menghitung luas permukaan tabung."""
    hasil = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    print("hasil Luas tabung dari jari-jari",jari_jari,",tinggi",tinggi,"=",hasil)

def luas_kerucut(jari_jari, tinggi):
    """Menghitung luas permukaan kerucut."""
    sisi_miring = math.sqrt(jari_jari ** 2 + tinggi ** 2)
    hasil = math.pi * jari_jari * (jari_jari + sisi_miring)
    print("hasil Luas kerucut dari jari-jari",jari_jari,",tinggi",tinggi,"=",hasil)

def luas_bola(jari_jari):
    """Menghitung luas permukaan bola."""
    hasil = 4 * math.pi * (jari_jari ** 2)
    print("hasil Luas bola dari jari-jari",jari_jari,"=",hasil)