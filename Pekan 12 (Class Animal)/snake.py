from Animal import Animal

class Snake(Animal):
    #Konstruksi Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, motif, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.motif = motif
        self.habitat = habitat

    def info_snake(self):
        super().informasi_animal()
        print("Motif \t\t\t: ",self.motif,"\nHabitat\t\t\t: ",self.habitat)

#objek
print()
King_Kobra = Snake("King Kobra", "Daging", "20 tahun", "bertelur","Hijau Zaitun","Hutan")
print("### Informasi Ula ###")
King_Kobra.info_snake()
print()
Sanca = Snake("Sanca", "Daging", "15 tahun", "bertelur","Beberapa jenis Gelap dan Beberapa jenis Terang","Hutan")
print("### Informasi Ula ###")
Sanca.info_snake()
Boa = Snake("Boa", "Daging", "55 tahun", "bertelur","Biru,Hitam,Putih","Laut")
print("### Informasi Ula ###")
Boa.info_snake()