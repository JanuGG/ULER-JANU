#Soal 1 : Perbedaan data structure
#LIST : List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya. Untuk mengakses nilai dalam list python, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut.
#TUPLE : Tupel adalah urutan, seperti daftar. Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. Tupel menggunakan tanda kurung, sedangkan List Python menggunakan tanda kurung siku. Untuk mengakses nilai dalam tupel, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut
#SET : Tipe data set dalah salah satu tipe data python yang tidak berurut (unordered). Misalkan ada dua anggota yang sama dalam nilai set maka secara otomatisa salah satu diantaranya akan menghilang, artinya tidak ditampilkan. cara ngeprint nya tinggal panggil var nya
#ICTIONARY : Karena setiap urutanya berisi key dan value. Setiap key dipisahkan dari value-nya oleh titik dua (:), item dipisahkan oleh koma, dan semuanya tertutup dalam kurung kurawal.Untuk mengakses elemen Dictionary, Anda dapat menggunakan tanda kurung siku yang sudah dikenal bersama dengan key untuk mendapatkan nilainya.

#Soal 2 : Akses List
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print (a[1:5])

#Soal 3 : Akses nested list
a = [[5, 9, 8], [0, 0, 6]]
print(a[1][1:3])

#Soal 4 : List manipulation
a = [[5, 9, 8], [0, 0, 6], [5, 9, 10], [11, 0, 6]]
print(a[2:4])

#Soal 5 : Delete element list
areas = ['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.0, 'bedroom', 10.75, 'bathroom', 10.50, 'poolhouse', 24.5, 'garage', 15.45]
areas.pop(9)
areas.pop(8)
print(areas)

#Soal 6 : List comprehension
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
T = [x for x in S if x %2 == 0]
print(T)

#Soal 7 : Menambahkan key-value baru ke Dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
europe["itali"] = "roma"
print(europe)

#Soal 8 : Boolean Comparison
print((50 > 40)) and ((5 < 6))
print((10 == 10)) or ((10 == 12))
print(not(9 == 8))

#Soal 9 : If-Else Statement
a = 60000 
if a > 100000:
    print("high")
elif a > 5000:
    print("medium")
elif a < 5000:
    print("low")










