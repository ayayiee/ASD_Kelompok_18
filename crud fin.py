import csv

#membuat class node

class Node:
    def __init__(self, folder, tipe):
        self.folder = folder    # Nama folder / file
        self.tipe = tipe        #Isinya folder atau file
        self.isi = []           #List untuk menyimpan isi folder
        self.posisi = None      #Mengetahui folder ini ada di folder mana (fitur back)
    
    #=========================================
    # CREATE
    #=========================================
    
    def tambah_isi(self, node_baru): 
        if self.tipe == "File":
            print("[Error] Tidak bisa menambahkan item ke dalam File!")
            return False

        # Kondisi ketika nama boleh sama asal beda TIPE
        for item in self.isi:
            if item.folder.lower() == node_baru.folder.lower() and item.tipe == node_baru.tipe:
                print(f"[Error] {node_baru.tipe} '{node_baru.folder}' sudah ada di lokasi ini!")
                return False

        node_baru.posisi = self 
        self.isi.append(node_baru)
        return True

    #=========================================
    # READ
    #=========================================
    
    def lihat_isi (self, filter_tipe=None):            
        items = self.isi
        if filter_tipe:
            items = [i for i in self.isi if i.tipe == filter_tipe]
            print(f"  (Menampilkan hanya: {filter_tipe})")

        if not items:
            print("  (Folder Kosong - Gunakan menu 'Tambah' untuk mengisi folder ini)")
        else:
            for item in items:
                ikon = "📁" if item.tipe == "Folder" else "📄"
                print(f"  {ikon} {item.folder}")

    #=========================================
    # UPDATE
    #=========================================
    
    def ubah_nama(self, nama_lama, nama_baru): 
        for item in self.isi:
            if item.folder.lower() == nama_lama.lower():
                
                # Cek apakah nama baru bentrok dengan tipe yang sama
                for cek in self.isi:
                    if cek.folder.lower() == nama_baru.lower() and cek.tipe == item.tipe:
                        print(f"[Error] Nama '{nama_baru}' sudah digunakan oleh {item.tipe} lain!")
                        return False
                        
                item.folder = nama_baru
                print(f"[Sukses] {item.tipe} '{nama_lama}' telah diubah menjadi {nama_baru}.")
                return True
        print(f"[Error] Gagal! {nama_lama} tidak ditemukan di folder ini.")
        return False

    #=========================================
    # DELETE
    #=========================================
    
    def hapus_isi(self, nama_dihapus): #delete   
        for item in self.isi:
            if item.folder.lower() == nama_dihapus.lower(): #lower membuat jadi huruf kecil agar tidak sensitif
                self.isi.remove(item)
                print(f"Berhasil menghapus {item.tipe} '{item.folder}'! !")
                return True
        print(f"Gagal, {nama_dihapus} tidak ditemukan.")
        return False
                
awal = Node("Laptop_saya", "Folder")

dokumen = Node("Tugas", "Folder")
foto = Node("foto", "File")

awal.tambah_isi(dokumen)
awal.tambah_isi(foto)

awal.lihat_isi()

# === TUGAS ANGGOTA 2: DATA & LOGIC SPECIALIST ===

# ================================================
# Menyimpan struktur folder ke CSV
# ================================================
def simpan_ke_csv(node_root, nama_file="data_folder.csv"):
    try:
        with open(nama_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Nama", "Tipe", "Parent"]) # Header
            writer.writerow([node_root.folder, node_root.tipe, "Root"])
            _tulis_rekursif(node_root, writer)
    except Exception as e:
        print(f"[Error CSV] {e}")

# ===================================================
# Mencatat setiap folder dan file ke dalam baris CSV
# ===================================================
def _tulis_rekursif(node, writer):
    """Mencatat setiap folder dan file ke dalam baris CSV"""
    for item in node.isi:
        # Mencatat: Nama Item, Tipe, dan Nama Folder Induknya
        writer.writerow([item.folder, item.tipe, node.folder])
        if item.tipe == "Folder":
            _tulis_rekursif(item, writer)

# ===================================================
# Sorting (mengurutkan isi folder A-Z)
# ===================================================
def urutkan_isi(node_sekarang):
    if node_sekarang.isi:
        node_sekarang.isi.sort(key=lambda x: x.folder.lower())
        print(f"\n[Sistem] Isi folder '{node_sekarang.folder}' berhasil diurutkan A-Z.")
    else:
        print("\n[Sistem] Folder kosong, tidak ada yang bisa diurutkan.")

# ===================================================
# Searching (mencari file/folder di seluruh sistem)
# ===================================================
def cari_file_folder(node_root, nama_cari):
    hasil = []
    _cari_rekursif(node_root, nama_cari, hasil)
    
    if hasil:
        print(f"\n[Hasil Pencarian untuk '{nama_cari}']:")
        for path in hasil:
            print(f"-> {path}")
    else:
        print(f"\n[Sistem] '{nama_cari}' tidak ditemukan.")

# ===================================================
# Searching (mencari ke dalam semua sub-folder)
# ===================================================
def _cari_rekursif(node, nama_cari, hasil, path_sekarang=""):
    path_baru = f"{path_sekarang}/{node.folder}" if path_sekarang else node.folder
    if nama_cari.lower() in node.folder.lower():
        hasil.append(f"[{node.tipe}] {path_baru}")
    
    for item in node.isi:
        _cari_rekursif(item, nama_cari, hasil, path_baru)

#TUGAS ANGGOTA 3
root = Node("Laptop_saya", "Folder")

try:
    nodes = {}
    with open("data_folder.csv",mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for baris in reader:
            nama, tipe, parent = baris
            baru = Node(nama, tipe)
            nodes[nama] = baru
            if parent == "Root":
                root = baru
            else:
                if parent in nodes:
                    nodes[parent].tambah_isi(baru)
except:
    print("[Sistem] File CSV tidak ditemukan. Memulai dengan folder kosong.")

node_sekarang = root
stack_riwayat = []

while True:
    path_saatini = " / ".join([n.folder for n in stack_riwayat] + [node_sekarang.folder])
    print("\n" + "="*35)
    print(f"📂 LOKASI SAAT INI: {path_saatini}") 
    print("="*35)
    print("1. Lihat isi folder")
    print("2. Tambah folder/file baru")
    print("3. Ubah nama")
    print("4. Hapus folder/file")
    print("5. Buka (Folder)")
    print("6. Urutkan (A-Z)")
    print("7. Cari nama")
    print("8. Kembali")
    print("0. Keluar dari program")
    print("="*35)
    
    pilihan = input("Pilih menu (0-8): ").strip()
    
    if pilihan == "1":
        f = input("Tampilkan hanya (1: Folder, 2: File, 3: Semua): ")
        tipe_f = "Folder" if f=="1" else "File" if f=="2" else None
        print("\n--- HASIL FILTER ---")
        node_sekarang.lihat_isi(tipe_f)
        input("\nTekan Enter untuk kembali ke menu...")
        
    elif pilihan == "2":
        print("\n--- TAMBAH BARU ---")
        nama_baru = input("Masukkan nama: ").strip()
        tipe_baru = "Folder" if input("Tipe (1. Folder, 2. File): ") == "1" else "File" 
        
        if node_sekarang.tambah_isi(Node(nama_baru, tipe_baru)):
            print(f"[Sukses] Berhasil menambahkan {tipe_baru} ke '{node_sekarang.folder}'")
            simpan_ke_csv(root)
            
    elif pilihan == "3":
        print("\n--- UBAH NAMA ---")
        nama_lama = input("Masukkan nama yang ingin diubah: ")
        nama_baru = input("Masukkan nama baru: ")
        if node_sekarang.ubah_nama(nama_lama, nama_baru):
            simpan_ke_csv(root)
        
    elif pilihan == "4":
        print("\n--- HAPUS ITEM ---")
        nama_hapus = input("Masukkan nama yang ingin dihapus: ")
        if node_sekarang.hapus_isi(nama_hapus):
            simpan_ke_csv(root)
        
    elif pilihan == "5":
        target = input("Masukkan nama folder untuk dibuka: ").strip()
        found = False
        for item in node_sekarang.isi:
            if item.folder.lower() == target.lower():
                if item.tipe == "Folder":
                    stack_riwayat.append(node_sekarang)
                    node_sekarang = item
                    print(f"[Sistem] Berhasil masuk ke folder '{node_sekarang.folder}'")
                else:
                    print("Folder tidak ditemukan")
                    input("\nTekan Enter untuk kembali ke menu...")
                found = True; break
        if not found: print("[Error] Tidak ditemukan.")

    elif pilihan == "6":
         print("\n--- URUTKAN A-Z ---")
         urutkan_isi(node_sekarang)

    elif pilihan == "7":
         print("\n--- CARI ---")
         cari_file_folder(root, input("Cari nama: "))

    elif pilihan == "8":
        if stack_riwayat:
            node_sekarang = stack_riwayat.pop()
        else:
            print("[Sistem] Anda sudah berada di lokasi paling awal (Root).")
            
    elif pilihan == "0":
        simpan_ke_csv(root)
        print("Program ditutup.")
    
    else:
        print("\n[Sistem] Pilihan salah! Harap ketik angka 1, 2, 3, 4, 5, 6, 7, 8, atau 0.")
