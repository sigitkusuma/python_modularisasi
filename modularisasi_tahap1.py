"""
Progam menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
print('Menghitung luas segitiga tanpa fungsi')
alas = 10
tinggi = 6
luas_segitiga = (alas * tinggi) / 2
print(f'Segitiga luas adalah {luas_segitiga,type(luas_segitiga)}')

alas = 20
tinggi = 6
luas_segitiga = (alas * tinggi) / 2
print(f'Segitiga luas adalah {luas_segitiga,type(luas_segitiga)}')

#mendefinisikan fungsi menggunakan : def
print('Menghitung luas segitiga dengan fungsi')
def menghitungLuasSegitiga(alas, tinggi):
    luasSegitiga = (alas * tinggi) / 2
    return luasSegitiga

alas = float(input('Masukan Alas : '))
tinggi = float(input('Masukan Tinggi : '))
print(f'Menghitung luas segitiga dengan fungsi, hasilnya : {menghitungLuasSegitiga(alas, tinggi), type(menghitungLuasSegitiga(alas, tinggi))}')

