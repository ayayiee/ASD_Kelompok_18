import csv

#membuat class node

class Node:
    def __init__(self, folder, tipe):
        self.folder = folder    # Nama folder 
        self.tipe = tipe        #Isinya folder atau file
        self.isi = []           #List untuk menyimpan isi folder
        self.posisi = None      #Mengetahui folder ini ada di folder mana (fitur back)
        
    def tambah_isi(self, node_baru): #create
        node_baru.posisi = self 
        self.isi.append(node_baru)
        
    def lihat_isi (self):            #read
        print(f"\nIsi dari folder {self.folder}: ")
        if not self.isi:
            print("(Folder kosong)")
        else:
            for item in self.isi:
                ikon = "[F]" if item.tipe == "Folder" else "[t]"
                print(f"{ikon} {item.folder}")

    def ubah_nama(self, nama_lama, nama_baru): #update
        for item in self.isi:
            if item.folder.lower() == nama_lama.lower():
                item.folder = nama_baru
                print(f"[Sistem] Berhasil! Nama {nama_lama} telah diubah menjadi {nama_baru}.")
                return
        print(f"[Sistem] Gagal: {nama_lama} tidak ditemukan di folder ini.")  

    def hapus_isi(self, nama_dihapus): #delete   
        for item in self.isi:
            if item.folder.lower() == nama_dihapus.lower(): #lower membuat jadi huruf kecil agar tidak sensitif
                self.isi.remove(item)
                print(f"Berhasil menghapus {item.folder} !")
                return
        print(f"Gagal: {nama_dihapus} tidak ditemukan.")
                
awal = Node("Laptop_saya", "Folder")

dokumen = Node("Tugas", "Folder")
foto = Node("foto", "File")

awal.tambah_isi(dokumen)
awal.tambah_isi(foto)

awal.lihat_isi()

# === TUGAS ANGGOTA 2: DATA & LOGIC SPECIALIST ===

def simpan_ke_csv(node_root, nama_file="data_folder.csv"):
    """Menyimpan struktur folder ke CSV agar data permanen """
    with open(nama_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nama", "Tipe", "Parent"]) # Header
        _tulis_rekursif(node_root, writer)
    print(f"\n[Sistem] Data berhasil disimpan ke {nama_file}")

def _tulis_rekursif(node, writer):
    """Mencatat setiap folder dan file ke dalam baris CSV"""
    for item in node.isi:
        # Mencatat: Nama Item, Tipe, dan Nama Folder Induknya
        writer.writerow([item.folder, item.tipe, node.folder])
        if item.tipe == "Folder":
            _tulis_rekursif(item, writer)

def urutkan_isi(node_sekarang):
    """Fitur Sorting: Mengurutkan isi folder A-Z [cite: 16]"""
    if node_sekarang.isi:
        node_sekarang.isi.sort(key=lambda x: x.folder.lower())
        print(f"\n[Sistem] Isi folder '{node_sekarang.folder}' berhasil diurutkan A-Z.")
    else:
        print("\n[Sistem] Folder kosong, tidak ada yang bisa diurutkan.")

def cari_file_folder(node_root, nama_cari):
    """Fitur Searching: Mencari file/folder di seluruh sistem [cite: 17]"""
    hasil = []
    _cari_rekursif(node_root, nama_cari, hasil)
    
    if hasil:
        print(f"\n[Hasil Pencarian untuk '{nama_cari}']:")
        for path in hasil:
            print(f"-> {path}")
    else:
        print(f"\n[Sistem] '{nama_cari}' tidak ditemukan.")

def _cari_rekursif(node, nama_cari, hasil, path_sekarang=""):
    """Mencari ke dalam semua sub-folder secara mendalam"""
    path_baru = f"{path_sekarang}/{node.folder}"
    if nama_cari.lower() in node.folder.lower():
        hasil.append(path_baru)
    
    for item in node.isi:
        _cari_rekursif(item, nama_cari, hasil, path_baru)



# --- UJI COBA TUGAS ANGGOTA 2 ---
# 1. Coba urutkan
urutkan_isi(awal)
awal.lihat_isi()

# 2. Coba simpan ke CSV 
simpan_ke_csv(awal)

# 3. Coba cari file
cari_file_folder(awal, "foto")

#TUGAS ANGGOTA 3

while True:
    print("\n" + "="*35)
    print(f"📂 LOKASI SAAT INI: {awal.folder}") 
    print("="*35)
    print("1. Lihat isi folder (Read)")
    print("2. Tambah folder/file baru (Create)")
    print("3. Ubah nama (Update)")
    print("4. Hapus folder/file (Delete)")
    print("5. Keluar dari program")
    print("="*35)
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        print("\n--- MENAMPILKAN ISI ---")
        awal.lihat_isi()
        
    elif pilihan == "2":
        print("\n--- TAMBAH BARU ---")
        nama_baru = input("Masukkan nama: ")
        tipe_baru = input("Tipe (Folder/File): ").capitalize() 
        
        if tipe_baru in ["Folder", "File"]:
            node_baru = Node(nama_baru, tipe_baru) 
            awal.tambah_isi(node_baru)            
            print(f"[Sistem] Berhasil menambahkan {tipe_baru} '{nama_baru}'!")
        else:
            print("[Sistem] Gagal: Tipe hanya boleh diisi 'Folder' atau 'File'.")
            
    elif pilihan == "3":
        print("\n--- UBAH NAMA ---")
        nama_lama = input("Masukkan nama yang ingin diubah: ")
        nama_baru = input("Masukkan nama baru: ")
        awal.ubah_nama(nama_lama, nama_baru)
        
    elif pilihan == "4":
        print("\n--- HAPUS ITEM ---")
        nama_hapus = input("Masukkan nama yang ingin dihapus: ")
        awal.hapus_isi(nama_hapus)
        
    elif pilihan == "5":
        print("\n[Sistem] Menutup program direktori... Sampai jumpa!")
        break # Perintah untuk menghentikan 'while True'
        
    else:
        print("\n[Sistem] Pilihan salah! Harap ketik angka 1, 2, 3, 4, atau 5.")