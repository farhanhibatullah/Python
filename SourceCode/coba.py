"""
    
def jumlah(a, b):
    return a+b

def kurang(a, b):
    return a-b

def kali(a, b):
    return a*b

def bagi(a, b):
    return a/b


print("kalkulator")
print("-----------")

print("1. Jumlah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")

jawab = int(input("Masukkan pilihan anda = "))

if jawab in (1,2,3,4) :
    angka1 = float(input("Input angka 1 = "))
    angka2 = float(input("Input angka 2 = "))
    print("-------------------")
    
if jawab == 1:
    print("nilainya adalah = ", jumlah(angka1,angka2))
    
if jawab == 2:
    print("nilainya adalah = ", kurang(angka1,angka2))
    
if jawab == 3:
    print("nilainya adalah = ", kali(angka1,angka2))

if jawab == 4:
    print("nilainya adalah = ", bagi(angka1,angka2))

"""

nama = ["Ruspel", "Dewi", "Farhan", "Ifa", "Faiz", "Fadly"]
nama_urutan_awal = nama.copy()
nama_urutan_awal.sort()
print("Ini sebelum diubah")
print(nama)
print(nama[1])
print("Ini sesudah diubah")
print(nama_urutan_awal)
nama_urutan_awal.reverse()
print("Ini kalo dari belakang")
print(nama_urutan_awal)
print(nama_urutan_awal[1:4])
print(nama_urutan_awal.index("Faiz"))
nama.insert(1,"Ini ibuku ->")
print(nama)

