# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Rifqi Tazakka Putra
# NIM   : J0403251158
# Kelas : TPL-B1
# ========================================================== 

# ---------------------------------------------------------------------
# Set current working directory ke folder tempat file py ini berada
# ---------------------------------------------------------------------
import os
os.chdir(os.path.dirname(__file__)) # ini nge set current working directory ke folder tempat file py ini berada
                                    # biar bisa baca file txt nya dengan mudah
# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 


# --------------------------------
# Fungsi: Membaca data dari file 
# --------------------------------
def baca_stok(nama_file): 
    stok_dict = {} 
    with open(nama_file,"r", encoding="utf-8") as file:
        
        # ngebaca tiap baris file txt nya dengan perulangan for
        for baris in file:
            baris = baris.strip()
            KodeBarang, NamaBarang, Stok = baris.split(",") # misahin tiap string berdasarkan tanda baca koma dan masing-masing bakal disimpen ke variabel yang berurutan
            
            # simpan data stok barang ke dictionary dengan key KodeBarang 
            stok_dict[KodeBarang] = {
                "nama_barang":NamaBarang,
                "stok" : int(Stok)
            }
    return stok_dict 

# intinya fungsi diatas bakal baca tiap baris file txt nya terus konversi ke dictionary 


# --------------------------------
# Fungsi: Menyimpan data ke file 
# --------------------------------
def simpan_stok(nama_file, stok_dict): 
    with open(nama_file, "w", encoding="utf-8") as f: # mode 'w' disini akan nge-write semua perubahan yang dilakukan oleh program menu ini
        for KodeBarang in stok_dict:                  # jadi kalo ga pake fungsi simpan, gabakal berubah file txt nya
            NamaBarang = stok_dict[KodeBarang]["nama_barang"]
            Stok = stok_dict[KodeBarang]["stok"]
            
            print(KodeBarang, NamaBarang, Stok, sep=",", file=f)
            
    print(f"\nStok Barang berhasil disimpan ke dalam {nama_file}")
    
# jadi intinya itu dia bakal nimpa dictionary saat ini ke file txt yang dituju (stok_barang.txt)

# --------------------------------
# Fungsi: Menampilkan semua data 
# --------------------------------
def tampilkan_semua(stok_dict): 
    if len(stok_dict)==0:
        print("Stok Kosong")
        return
    
    print("\n=== Daftar Stok Barang ===\n")
    print(f"{'Kode':^10} | {'Nama':^20} | {'Stok':^10}") # ini semacam kayak format gitu, '^' artinya rata tengah
    print("-"*45)                                        # angka disampingnya itu ukuran karakter yang bakal memuat di kolom tersebut
    
    for KodeBarang in sorted(stok_dict.keys()):
        NamaBarang = stok_dict[KodeBarang]["nama_barang"]
        Stok = stok_dict[KodeBarang]["stok"]
        print(f"{KodeBarang:^10} | {NamaBarang:^20} | {Stok:^10}")
    

# ----------------------------------------
# Fungsi: Cari barang berdasarkan kode 
# ----------------------------------------
def cari_barang(stok_dict): 
    # mencari barang berdasarkan input Kode Barang
    kode = input("Masukkan kode barang: ").strip()
    
    # validasi kalo kode ada di dictionary, tampilin stok barangnya
    if kode in stok_dict:
        NamaBarang=stok_dict[kode]["nama_barang"]
        Stok=stok_dict[kode]["stok"]
        
        print("\n=== Stok Barang Ditemukan ===\n")
        print(f"Kode : {kode}")
        print(f"Nama : {NamaBarang}")
        print(f"Kode : {Stok}")
    else:
        print("Barang tidak ditemukan.")


# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 
def tambah_barang(stok_dict): 

    kode = input("Masukkan kode barang baru: ").strip() 
    nama = input("Masukkan nama barang: ").strip() 
    
    if kode in stok_dict:
        print("Kode sudah digunakan!")
        return
    
    stok_awal = int(input("Masukkan jumlah stok: "))
    print("Barang baru berhasil ditambahkan!")
    
    stok_dict[kode] = {
        "nama_barang":nama,
        "stok":int(stok_awal)
    }

# intinya fungsi diatas bakal masukin inputan kita ke dictionary, tpi sebelum itu dicek dlu apakah kode udh digunain atau belum untuk menghindari duplikasi primary key (dimana ini tuh harus unik dan beda semua buat memudahkan pencarian)

# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 
def update_stok(stok_dict): 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    if kode not in stok_dict:
        print("Stok Barang tidak ditemukan.")
        return
  
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
 
    pilihan = input("Masukkan pilihan (1/2): ").strip() 
    
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except:
        print("Stok harus angka!")
        return
    
    stok_lama = stok_dict[kode]["stok"]
    
    if pilihan == "1":
           stok_baru = stok_lama + jumlah
    elif pilihan == "2":
           stok_baru = stok_lama - jumlah
    else:
        print("Pilihan tidak valid!")
        return
    
    if stok_baru < 0:
        print("Stok tidak boleh negatif!")
        return
    
    stok_dict[kode]["stok"] = stok_baru
    print(f"Stok berhasil diupdate. Nilai {kode} berubah dari {stok_lama} menjadi {stok_baru}")

# intinya fungsi ini bakal ngeupdate data dictionary berdasarkan kode barang dan juga ada 2 pilihan update antara menambahkan stok dan mengurangi stok, dan juga stok tidak boleh negatif
 
# ------------------------------- 
# Program Utama 
# ------------------------------- 
def main(): 
    
    # membaca data dari file saat program mulai (biar bisa di proses/ubah selama program berjalan)
    stok = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===\n") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("\nPilih menu: ").strip() 

        # pemanggilan semua fungsi yang udah dibuat jadi pilihan
        
        if pilihan == "1": 
            tampilkan_semua(stok) 
 
        elif pilihan == "2": 
            cari_barang(stok) 
 
        elif pilihan == "3": 
            tambah_barang(stok) 
 
        elif pilihan == "4": 
            update_stok(stok) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok) 
            print("\nData berhasil disimpan.") 
 
        elif pilihan == "0": 
            print("Program selesai.") 
            break
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 

# menjalankan program utama jika hanya jika file ini dijalankan langsung, bukan saat diimport sebagai module di file lain
if __name__ == "__main__": 
    main()
