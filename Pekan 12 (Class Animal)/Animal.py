class Animal :
    #Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    #method informasi
    def informasi_animal(self):
        print("Nama Hewan \t\t: ",self.nama,"\nMakanan\t\t\t: ",self.makanan,"\nHidup\t\t\t: ",self.hidup,"\nBerkembang Biak\t\t: ",self.berkembang_biak,)

# #Membuat objek
# kucing = Animal("Kucing", "Daging", "10 Tahun", "Melahirkan")
# #Mengakses atribut
# kucing.informasi_animal()