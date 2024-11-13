#cara mengukur berat badan ideal pria
#Berat badan ideal laki-laki (kg) = [tinggi badan (cm) -100] - [(tinggi badan (cm) -100) x 10%] 
tinggi_badan = int(input('masukan tinggi badan; '))
berat_badan_ideal= (tinggi_badan-100)-(tinggi_badan-100)*1/10
print("berat badan ideal untuk tinggi",tinggi_badan, "cm adalah", berat_badan_ideal,"kg")