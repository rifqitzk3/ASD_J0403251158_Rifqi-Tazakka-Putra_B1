#Buat fix path, jadi walau open folder dari folder general, tetep bisa nemuin file dari folder khusus yg ada di tempat file py ini berada
import os
os.chdir(os.path.dirname(__file__)) #Set current working directory ke folder tempat file py ini berada

#=========================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1: Membuat fungsi Load Data
#=========================================================

nama_file = "datamahasiswaa.txt"

def load_data(nama_file):
    data_dict={} 

    with open("datamahasiswaa.txt","r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")
            #Simpan data mahasiswa ke dictionary dengan key NIM
            data_dict[nim] = {
                "nama":nama,
                "nilai": int(nilai)
            }
    return data_dict

#Membuat fungsi baca
# baca = load_data(nama_file) #Menyimpan data dari dictionary ke variabel "baca"
# print(len(baca)) 


#=========================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2: Membuat fungsi menampilkan Data
#=========================================================

def tampilkan_data(data_dict):
    if len(data_dict)==0:
        print('Data Kosong')
        return
    
    #Membuat Header Tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM' :<10} | {'Nama' :<12} | {'Nilai' :>5}")
    print("-" * 32)
    #Membuat Isi Tabel
    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama:<12} | {nilai:>5}")

#Memanggil fungsi Menampilkan Data (Nampilin tabel yg tadi udah dibuat)
# tampilkan_data(baca)


#=========================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 3: Membuat fungsi mencari data
#=========================================================

def cari_data(data_dict):
    #Mencari Mahasiswa berdasarkan input NIM
    nim_cari = input("\nMasukkan NIM yang ingin dicari: ").strip()
    
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM    : {nim_cari}")
        print(f"Nama   : {nama}")
        print(f"Nilai  : {nilai}")
    else:
        print("Data tidak ditemukan!")

# cari_data(baca)


#=========================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 4: Membuat fungsi update nilai
#=========================================================

def update_nilai(data_dict):
    nim = input("\nMasukkan NIM Mahasiswa yang ingin di update: ").strip()
    
    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan Nilai Baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus direntang 0-100. Update dibatalkan")
    
    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru
    
    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(baca)


#============================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5: Membuat fungsi menyimpan perubahan data ke file
#============================================================

def simpan_data(nama_file, data_dict):
    # Membuka file dengan mode "w" (write/tulis ulang)
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in data_dict:
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            
            print(nim, nama, nilai, sep=",", file=file)
    
    print(f"\nData berhasil disimpan ke dalam {nama_file}")

# simpan_data("Pertemuan 1/datamahasiswa.txt", baca)


#============================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 6: Membuat Menu
#============================================================

def menu():
    #Load data pertama kali saat program dijalankan
    baca = load_data(nama_file)
    
    while True:
        print("\n" + "="*30)
        print(" MENU INFORMASI MAHASISWA ")
        print("="*30)
        print("1. Tampilkan Semua Data")
        print("2. Cari Mahasiswa (NIM)")
        print("3. Update Nilai Mahasiswa")
        print("4. Simpan Perubahan ke File")
        print("0. Keluar")
        print("="*30)
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == "1":
            tampilkan_data(baca)
        elif pilihan == "2":
            cari_data(baca)
        elif pilihan == "3":
            update_nilai(baca)
        elif pilihan == "4":
            simpan_data("datamahasiswaa.txt", baca)
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


#Manggil Fungsi Menu
menu()

