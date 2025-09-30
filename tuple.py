#1
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

#2
hari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
print(hari)

#3
angka = (10, 20, 30, 40)
print(angka[1:3]) 
# (20, 30) hasilnya

#4
data = ('apel', 'jeruk', 'pisang', 'anggur')
print(data[2])  # Mengakses elemen ketiga

#5
nilai = (80, 85, 90, 75, 95)
jumlah = len(nilai)
print("Jumlah elemen dalam tuple:", jumlah)

#6
# tuple tidak dapat diubah setelah dibuat karena bersifat imutable
tuple_mut = (9, 8, 7, 6)
# tuple_mut[1] = 10  # Mengubah elemen kedua
# print(tuple_mut)  # TypeError: 'tuple' object does not support item assignment

#7
def elemen_sama(t1, t2):
    hasil = tuple(set(t1) & set(t2))
    return hasil

t1 = ('kucing', 'anjing', 'burung', 'ikan')
t2 = ('ikan', 'kuda', 'burung')

print(elemen_sama(t1, t2))


#9 
tuple_bersarang = ((1, 2), (3, 4), (5, 6))
jumlah_bersarang = len(tuple_bersarang)
print("Jumlah elemen dalam tuple bersarang:", jumlah_bersarang)

#KELOMPOK 9
#Muhammad Raihan (241111075)
#Muhammad Ihsan (241111046)