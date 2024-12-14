from Animal import Animal

class Fish(Animal):
    #Konstruksi Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat

    def info_fish(self):
        super().informasi_animal()
        print("Bernapas \t\t: ",self.bernapas,"\nHabitat\t\t\t: ",self.habitat)

#objek
print()
Hiu = Fish("Hiu", "Daging", "20 tahun", "ovipar","insang","laut")
print("### Informasi Iwak ###")
Hiu.info_fish()
print()
Paus = Fish("Paus", "Plankton", "60 tahun", "vivipar","Paru-Paru","laut")
print("### Informasi Iwak ###")
Paus.info_fish()
print()
Lumba_lumba = Fish("Lumba-lumba", "Daging", "30 tahun", "vivipar","Paru-paru","laut")
print("### Informasi Iwak ###")
Hiu.info_fish()