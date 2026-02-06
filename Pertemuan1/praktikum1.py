#=====================================================
#Praktikum Pertemuan 1 : Konsep ADT dan File Handling
#=====================================================

#===========================================
#Latihan Dasar 1 : Membaca seluruh isi file
#===========================================

#Membuka file dengan mode read ("r")
with open("Pertemuan 1/datamahasiswaa.txt", "r", encoding='utf-8') as file:
    isi_file = file.read() #Membaca keseluruhan isi file dalam satu string

print(isi_file)

print("\n=== Hasil Read ===\n")
print("Tipe Data:", type(isi_file)) #Fungsi melihat tipe data
print("Jumlah Karakter", len(isi_file)) #Fungsi menghitung panjang (length) karakter dari string (dalam kasus ini itu datamahasiswaa.txt)
print("jumlah baris", isi_file.count("\n")+1) #Method yang menjumlahkan berdasarkan parameter, dalam kasus ini itu \n atau baris baru

#Membuka file perbaris
print("===Membaca File per Baris===")
jumlah_baris = 0
with open("Pertemuan 1/datamahasiswaa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1 #Ini bakal ngebuat nilai dari variabel jumlah baris bertambah 1 setiap iterasi loop for 
        baris = baris.strip() #Menghilangkan baris yang kosong
        print("Baris ke-", jumlah_baris) 
        print ("Isinya", baris)

#====================================================
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#====================================================

with open("Pertemuan 1/datamahasiswaa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() 
        nim, nama, nilai = baris.split(",") #Memisahkan variabel nim, nama, nilai dengan parameter koma, jadi dia misahin dengan 
        print("NIM : ", nim, "| NAMA : ", nama, "| NILAI: ", nilai)

#========================================================
#Latihan Dasar 3 : Membaca file dan menyimpannya ke List
#========================================================

data_list = []
with open("Pertemuan 1/datamahasiswaa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        
        data_list.append([nim,nama,int(nilai)])

print("\n=== Data Mahasiswa dalam List ===")
print(data_list)

print("\n=== Jumlah Record dalam List ===")
print("Jumlah Record", len(data_list))

print("\n=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama: ", data_list[0])

#============================================================
#Latihan Dasar 4 : Baca file dan menyimpannya ke Dictionary
#============================================================

data_dict = {} #buat variabel untuk dictionary
with open("Pertemuan 1/datamahasiswaa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #Simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {
            "nama":nama,
            "nilai": int(nilai)
        }
print("\n==== Data Mahasiswa dalam Dictionary ===")
print(data_dict)