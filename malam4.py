#try and except
#task 1
try:
    angka = int("abc")
    print (angka)    

except (ValueError):
    print("Angka merupakan String bukan integer")

#task 2
try :
    angka = int("100")
    print(angka)
except:
    print("Angka error")
else:
    print("Yeay berhasil")        



#task 3

def pembagian(a, b):
    return a / b

try :
    hasil = pembagian(10, 0)

    print(hasil)
except:
    print("Tidak bisa dibagi dengan angka nol")    



#task 4
data = [
    {"produk": "Laptop", "harga": "8000000"},
    {"produk": "Mouse", "harga": "250000"},
    {"produk": "Keyboard", "harga": "abc"},
    {"produk": "Monitor", "harga": "2500000"},
]

for item in data:
    try:
        harga = int(item["harga"])
        print(item["produk"], ":",harga )

    except ValueError:
        print(item["produk"], ":", "tidiak memiliki harga valid")    

print("==================================================================")

#bonys task

data = [
    {"produk": "Laptop", "harga": "8000000"},
    {"produk": "Mouse", "harga": "250000"},
    {"produk": "Keyboard", "harga": "abc"},
    {"produk": "Monitor", "harga": "2500000"},
    {"produk": "Headset", "harga": None},
]

for i in data:
    try:
        print(i["produk"],":", i["harga"])
    except: 
        print ("data error")   

print("============================================================================")
#bonus task tambahan
data = [
    {"produk": "Laptop", "harga": "8000000"},
    {"produk": "Mouse", "harga": "250000"},
    {"produk": "Keyboard", "harga": "abc"},
    {"produk": "Monitor", "harga": "2500000"},
    {"produk": "Headset", "harga": None},
]

for i in data:
    try:
    
        harga = int(i["harga"])
        print(i["produk"], ";", harga)

    except (ValueError, TypeError):
        print(i["produk"], "harga tidak valid")