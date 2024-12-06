class Gempa:
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        
#method menetukan dampak skala gempa       
    def dampak(self):
    #statement / Logika
        if self.skala <2 :
            print ("Dampak tidak Berasa")
        elif self.skala >= 2 and self.skala <=4:
            print ("dampak gempa bangunan retak-retak")
        elif self.skala >4 and self.skala <=6:
            print ("dampak gempa bangunan roboh")
        elif self.skala >6:
            print ("dampak gempa bangunan roboh dan berpotensi tsunami")
    
        #menampilkan lokasi dan skala
        print(f'Lokasi Gempa : {self.lokasi}')
        print(f'Skala Gempa : {self.skala}')
