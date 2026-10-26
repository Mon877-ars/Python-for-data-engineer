#slsit
nama = ["Sita", "Juan", "Rasya", "Rachel", "Melly"]
print(nama)
nama[2] = "Sinta"
print(nama[2])
nama.append("Susan")
print(nama)

#dict

data = {
    "nama": "susan",
    "umur" : 13,
    "jurusan" : "Teknik perdagangan",
    "semester" : 14
}

print(data["nama"])
print(data["jurusan"])
print(data["semester"])

#dict to set
skills = [
    "Python",
    "SQL",
    "Python",
    "Java",
    "SQL",
    "Python",
    "Git"
]
value_set = set(skills.values())
print(value_set)

#mini case
mahasiswa = [
    {"nama": "Andi", "jurusan": "Informatika"},
    {"nama": "Budi", "jurusan": "Sistem Informasi"},
    {"nama": "Citra", "jurusan": "Informatika"},
]

list_nama = [mhs["nama"]for mhs in mahasiswa]
print (list_nama)

for mhs in mahasiswa:
    if mhs["jurusan"] == "Informatika":
        print(mhs["nama"])

mahasiswa = ["Sita", "Juan", "Rasya"]
mahasiswa[1] = "Johan"
mahasiswa.append("Rachel")
mahasiswa.insert(0, "Melly")
mahasiswa.remove("Rasya")
print(mahasiswa)

nama = ["Sita", "Juan", "Rasya", "Rachel", "Melly"]

nama_user = input("Masukkan nama anda: ")
if nama_user in nama:
    print(nama_user,"ditemukan")
else:
    print(nama_user,"tidak ditemukan")    

mahasiswa = [
    {"nama": "Sita", "jurusan": "Informatika"},
    {"nama": "Juan", "jurusan": "Sistem Informasi"},
    {"nama": "Rasya", "jurusan": "Informatika"},
    {"nama": "Rachel", "jurusan": "Teknik Komputer"},
    {"nama": "Melly", "jurusan": "Informatika"}
]

for mhs in mahasiswa:
    if mhs["jurusan"] == "Informatika":
        print(mhs["nama"])

nilai = {
    "Sita": 85,
    "Juan": 72,
    "Rasya": 90,
    "Rachel": 65,
    "Melly": 78
}

mahasiswa = [
    {"nama": "Sita", "jurusan": "Informatika", "nilai": 85},
    {"nama": "Juan", "jurusan": "Sistem Informasi", "nilai": 72},
    {"nama": "Rasya", "jurusan": "Informatika", "nilai": 90},
    {"nama": "Rachel", "jurusan": "Teknik Komputer", "nilai": 65},
    {"nama": "Melly", "jurusan": "Informatika", "nilai": 78}
]

for mhs in mahasiswa:
    if (mhs["jurusan"]=="Informatika"):
        print(mhs["nama"])

for mhs in mahasiswa:
    if (mhs["nilai"] >= 80):
        print(mhs["nama"]) 

for mhs in mahasiswa:
    if (mhs["jurusan"] == "Informatika"  and mhs["nilai"]>=80):
        print (mhs["nama"])       

jumlah = 0
for mhs in mahasiswa:
    if (mhs["nilai"]>=80):
        jumlah += 1

print(jumlah)