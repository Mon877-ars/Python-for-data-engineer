#for
angka = [10, 20, 30, 40, 50]
for i in angka:
    print(i)

#range
for i in range(1, 11):
    print(i)    

#range dengan selisih 2
for i in range(2,22,2):
    print(i)

#while
n = 5
while n >0:
    print(n)
    n -=1

#mini case
transaksi = [
    {"produk": "Laptop", "harga": 8000000},
    {"produk": "Mouse", "harga": 250000},
    {"produk": "Keyboard", "harga": 500000},
    {"produk": "Monitor", "harga": 2500000},
]

for items in transaksi:
    print(items["produk"])
    print(items["harga"])
print ("================")
for items in transaksi:
    if (items["harga"] >=1000000):
        print(items["produk"])