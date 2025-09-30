#1
#List adalah struktur data yang digunakan untuk menyimpan sekumpulan data dalam satu variabel. List dapat menyimpan berbagai jenis data, seperti angka, string, dan objek lainnya. List bersifat mutable, artinya kita dapat menambah, mengubah dan menghapus elemen di dalamnya.

data_banyak = list(range(1, 201))
print(data_banyak)

akses_data = data_banyak[0:100]
print(akses_data)

#2
angka = [90, 4, 5, 6, 7, 20]

#3
angka.append(60)

#4
angka.insert(2, 25)

#5
angka[4] = 35

#6
angka.remove(20)

#7
jumlah = sum(angka)

#8
terbesar = max(angka)

#9
urut = angka.sort(reverse=True)

#10
angka_baru = [35, 40]

#11
rata_rata = sum(angka) / len(angka)

print(angka)
print(jumlah)
print(angka_baru)
print(rata_rata)

#KELOMPOK 9
#Muhammad Raihan (241111075)
#Muhammad Ihsan (241111046)