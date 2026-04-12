<<<<<<< HEAD
# Pengelolaan Folder & File (Tree)
import csv

def simpan_ke_csv(node_root, nama_file="data_folder.csv"):
    with open(nama_file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nama", "Tipe", "Parent"])
        _tulis_rekursif(node_root, writer)
    print(f"\n[Sistem] Data berhasil disimpan ke {nama_file}")

def _tulis_rekursif(node, writer):
    for item in node.isi:
        writer.writerow([item.folder, item.tipe, node.folder])
        if item.tipe == "Folder":
            _tulis_rekursif(item, writer)

def urutkan_isi(node_sekarang):
    if node_sekarang.isi:
        node_sekarang.isi.sort(key=lambda x: x.folder.lower())
        print(f"\n[Sistem] Isi folder '{node_sekarang.folder}' berhasil diurutkan A-Z.")
    else:
        print("\n[Sistem] Folder kosong, tidak ada yang bisa diurutkan.")

def cari_file_folder(node_root, nama_cari):
    hasil = []
    _cari_rekursif(node_root, nama_cari, hasil)
    
    if hasil:
        print(f"\n[Hasil Pencarian untuk '{nama_cari}']:")
        for path in hasil:
            print(f"-> {path}")
    else:
        print(f"\n[Sistem] '{nama_cari}' tidak ditemukan.")

def _cari_rekursif(node, nama_cari, hasil, path_sekarang=""):
    path_baru = f"{path_sekarang}/{node.folder}"
    if nama_cari.lower() in node.folder.lower():
        hasil.append(path_baru)
    
    for item in node.isi:
        _cari_rekursif(item, nama_cari, hasil, path_baru)

urutkan_isi(awal)
awal.lihat_isi()
simpan_ke_csv(awal)
cari_file_folder(awal, "foto")
=======
#membuat class node

class Node:
    def __init__(self, folder, tipe):
        self.folder = folder    # Nama folder 
        self.tipe = tipe        #Isinya folder atau file
        self.isi = []           #List untuk menyimpan isi folder
        self.posisi = None      #Mengetahui folder ini ada di folder mana (fitur back)
        
    def tambah_isi(self, node_baru):
        node_baru.posisi = self 
        self.isi.append(node_baru)
        
    def lihat_isi (self):
        print(f"\nIsi dari folder {self.folder}: ")
        if not self.isi:
            print("(Folder kosong)")
        else:
            for item in self.isi:
                ikon = "[F]" if item.tipe == "Folder" else "[t]"
                print(f"{ikon} {item.folder}")
                
awal = Node("Laptop_saya", "Folder")

dokumen = Node("Tugas", "Folder")
foto = Node("foto", "File")

awal.tambah_isi(dokumen)
awal.tambah_isi(foto)

awal.lihat_isi()
>>>>>>> eae56fc715b924bfbc8d90a0dc100b7561078dad
