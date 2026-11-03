def sapa ():
    print("Halo, data engineer")

sapa()

print("====================")

def sapa(nama):
    print("Halo ", nama )

sapa("Budi")
sapa("yanti")
print("===================")

def hitung_luas(panjang,  lebar):
    return panjang * lebar

hasil = hitung_luas(5, 6)
print(hasil)

print("====================")

def cek_harga(harga):
    if( harga >=  1000000):
        return "mahal"
    else:
        return "murah"
print (cek_harga(5000000))
print(cek_harga(400000))
print("======================")
transaksi = [
    {"produk": "Laptop", "harga": 8000000},
    {"produk": "Mouse", "harga": 250000},
    {"produk": "Keyboard", "harga": 500000},
    {"produk": "Monitor", "harga": 2500000},
]
def cek_diskon(harga):
    return harga - harga*0.1

for item in transaksi:
    print(item['produk'], ":" ,cek_diskon(item['harga']))
