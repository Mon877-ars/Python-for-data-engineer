
import csv
import json

import csv

data = [
    ["Laptop",8000000],
    ["Mouse",250000],
    ["Keyboard",500000],
    ["Monitor",2500000]
]

with open ("transaksi.cvs", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["produk", "harga"])


    for row in data:
        writer.writerow(row)

with open("/home/emon/data-engineering/transaksi.cvs", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        harga = int(row["harga"])
        #print(row["produk"], ":", harga)
        if harga > 1000000:
            print(row["produk"], ":", harga)   



data = [
    {"produk": "Laptop", "harga": 8000000},
    {"produk": "Mouse", "harga": 250000},
    {"produk": "Keyboard", "harga": 500000},
    {"produk": "Monitor", "harga": 2500000}
]
with open("apasih.json", "w") as file:
    json.dump(data, file, indent = 4)
with open("apasih.json", "r") as file :
    data =json.load(file)

print(data)




data = []

with open("transaksi.cvs", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row ["harga"] = int(row["harga"])
        data.append(row)

with open("transaksi.json", "w") as file:
    json.dump(data, file, indent=4)
