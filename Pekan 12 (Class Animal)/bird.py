from Animal import Animal

class Bird(Animal):
    #Konstruksi Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        super().informasi_animal()
        print("Warna \t\t\t: ",self.warna,"\nParuh\t\t\t: ",self.paruh)

#objek
print()
Elang = Bird("Elang", "Daging", "70 tahun", "bertelur","coklat","bengkok dan lancip")
print("### Informasi Manuk ###")
Elang.info_bird()
Beo = Bird("Beo", "Biji-bijian", "10 tahun", "bertelur","Merah, Kuning, Hijau, dan Putih","Pendek dan Bengkok")
print("### Informasi Manuk ###")
Beo.info_bird()
Bangau = Bird("Bangau", "Daging", "15 tahun", "bertelur","Merah Muda","Panjang dan lancip")
print("### Informasi Manuk ###")
Bangau.info_bird()