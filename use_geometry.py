from Geometri.persegiPanjang import hitungPersegiPanjang
from Geometri.segitiga import info, menghitungLuasSegitiga as hitungSegitiga

alas = float(input('Masukan alas : '))
tinggi = float(input('Masukan Tinggi : '))
print(info())
print(hitungSegitiga(alas, tinggi))

panjang = float(input('Masukan Panjang : '))
tinggi = float(input('Masukan tinggi : '))
print(hitungPersegiPanjang(panjang, tinggi))