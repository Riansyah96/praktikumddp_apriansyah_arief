#memamggil file gempa dan Import semua Method/fungsi
from Gempa import *

#Membuat Objek Gempa dengan Argumen
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

#Informasi Gempa
print ('## Info Gempa Maseh ##')
print()
gempa1.dampak()
gempa2.dampak()
gempa3.dampak()
gempa4.dampak()
gempa5.dampak()