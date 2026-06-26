import csv
import time
from node import Node
from file_handler import simpan_ke_csv
from sorting import urutkan_isi
from searching import cari_file_folder

pink = '\033[95m'
reset = '\033[0m'

# === TUGAS ANGGOTA 3: GABRIELLA ANGGI ===
root = Node("Laptop_saya", "Folder")

print(f"{pink}" + "="*70 + f"{reset}")
print("Selamat Datang di Direktori Folder Laptop Saya!")
print("Sistem siap mengelola file dan folder Anda.")
print(f"{pink}" + "="*70 + f"{reset}")
input("Tekan Enter untuk masuk ke program...")

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
    print("File CSV tidak ditemukan. Memulai dengan folder kosong.")

node_sekarang = root
stack_riwayat = []

while True:
    path_saatini = " / ".join([n.folder for n in stack_riwayat] + [node_sekarang.folder])
    print("\n" + "="*70)
    print(f"📂 LOKASI SAAT INI: {path_saatini}") 
    print("="*70)
    print("1. Lihat isi folder")
    print("2. Tambah folder/file baru")
    print("3. Ubah nama")
    print("4. Hapus folder/file")
    print("5. Buka (Folder)")
    print("6. Urutkan (A-Z)")
    print("7. Cari nama")
    print("8. Kembali")
    print("0. Keluar dari program")
    print("="*70)
    
    pilihan = input("Pilih menu (0-8): ").strip()
    
    if pilihan == "1":
        f = input("Tampilkan hanya (1: Folder, 2: File, 3: Semua): ")
        if f in ["1", "2", "3"]:
            tipe_f = "Folder" if f=="1" else "File" if f=="2" else None
            print("\n--- HASIL FILTER ---")
            node_sekarang.lihat_isi(tipe_f)
        else: 
            print("\nPilihan tidak tersedia!")
        input("\nTekan Enter untuk kembali ke menu...")
        
    elif pilihan == "2":
        print("\n--- TAMBAH BARU ---")
        print("Kosongkan untuk membatalkan.")
        
        nama_baru = input("Masukkan nama: ").strip()
        if not nama_baru:
            print("\n>>> Penambahan item dibatalkan. Kembali ke menu utama...")
            time.sleep(3)
            continue
        
        tipe_input = input("Tipe (1. Folder, 2. File): ").strip()
        if not tipe_input:
            print("\n>>> Penambahan item dibatalkan. Kembali ke menu utama...")
            time.sleep(3)
            continue
        
        tipe_baru = "Folder" if tipe_input == "1" else "File" 
        if node_sekarang.tambah_isi(Node(nama_baru, tipe_baru)):
            print(f"[Sukses] Berhasil menambahkan {tipe_baru} ke '{node_sekarang.folder}'")
            simpan_ke_csv(root)
            input("\nTekan Enter untuk kembali ke menu...")
            
    elif pilihan == "3":
        print("\n--- UBAH NAMA ---")
        
        if not node_sekarang.isi:
            print("  (Folder kosong, tidak ada item yang bisa diubah namanya)")
            input("\nTekan Enter untuk kembali ke menu...")
            continue
        
        print("Item yang tersedia di lokasi ini:")
        for item in node_sekarang.isi:
            ikon = "📁" if item.tipe == "Folder" else "📄"
            print(f"  {ikon} {item.folder} ({item.tipe})")
        print("-" * 70)
        print("(Kosongkan untuk membatalkan)")
        
        nama_lama = input("Masukkan nama yang ingin diubah: ")
        if not nama_lama:
            print("\n>>> Perubahan nama dibatalkan. Kembali ke menu utama...")
            time.sleep(3)
            continue
        
        nama_ketemu = False
        for item in node_sekarang.isi:
            if item.folder.lower() == nama_lama.lower():
                nama_ketemu = True
                break
        if not nama_ketemu:
            print(f"\nGagal! '{nama_lama}' tidak ditemukan di folder ini.")
            input("\nTekan Enter untuk kembali ke menu...")
            continue
        
        nama_baru = input("Masukkan nama baru: ")
        if not nama_baru:
            print("\n>>> Proses penghapusan dibatalkan. Kembali ke menu utama...")
            time.sleep(3)
            continue
        
        if node_sekarang.ubah_nama(nama_lama, nama_baru):
            simpan_ke_csv(root)
            input("\nTekan Enter untuk kembali ke menu...")
        
    elif pilihan == "4":
        print("\n--- HAPUS ITEM ---")
        if not node_sekarang.isi:
            print("\nFolder kosong, tidak ada file atau folder yang bisa dihapus.")
            input("Tekan Enter untuk kembali ke menu. . .")
            continue
        
        print("Item yang tersedia di lokasi ini: ")
        for item in node_sekarang.isi:
            ikon = "📁" if item.tipe == "Folder" else "📄"
            print(f"  {ikon} {item.folder} ({item.tipe})")
        print("=" * 70)
        print("Kosongkan untuk membatalkan")
        
        nama_hapus = input("Masukkan nama yang ingin dihapus: ").strip()
        
        if not nama_hapus:
            print("\n>>> Proses penghapusan dibatalkan. Kembali ke menu utama...")
            time.sleep(3)
            continue
        
        if node_sekarang.hapus_isi(nama_hapus):
            simpan_ke_csv(root)
        input("\nTekan Enter untuk kembali ke menu...")
        
    elif pilihan == "5":
        print("\n--- BUKA FOLDER ---")
        daftar_folder = [item for item in node_sekarang.isi if item.tipe == "Folder"]
        
        if not daftar_folder:
            print("Tidak ada folder yang bisa dibuka di lokasi ini.")
            input("Tekan Enter untuk kembali ke menu. . .")
            continue
        
        else:
            print("\nFolder yang tersedia : ")
            for folder_aktif in daftar_folder:
                print(f"📁 {folder_aktif.folder}")
            print("="*70)
            
        while True:
            print("\nKosongkan untuk membatalkan")
            target = input("Masukkan nama folder untuk dibuka: ").strip()
            
            if not target:
                print("\n>>> Proses membuka folder dibatalkan. Kembali ke menu utama...")
                time.sleep(2)
                break
            
            found = False
            for item in node_sekarang.isi:
                if item.folder.lower() == target.lower():
                    found = True
                    if item.tipe == "Folder":
                        stack_riwayat.append(node_sekarang)
                        node_sekarang = item
                        print(f"[Sistem] Berhasil masuk ke folder '{node_sekarang.folder}'")
                        time.sleep(2)
                    else:
                        print("Item tersebut adalah File, bukan Folder!")
                        found = False; break
            if found:
                break 
            elif target.lower() != 'x':
                print("Folder tidak ditemukan. Silakan periksa ejaan dan coba lagi.")
                print("="*70)

    elif pilihan == "6":
        print("\n--- URUTKAN A-Z ---")
        urutkan_isi(node_sekarang)
         
        if node_sekarang.isi:
            print("\nIsi folder setelah diurutkan:")
            node_sekarang.lihat_isi()
            
            input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "7":
        print("\n--- CARI FILE/FOLDER ---")
        print("Kosongkan untuk membatalkan")
        cari_file_folder(root, input("Cari nama: "))
        input("\nTekan Enter untuk kembali ke menu...")

    elif pilihan == "8":
        if stack_riwayat:
            print("\n>>> Kembali ke folder sebelumnya...")
            time.sleep(2)
            node_sekarang = stack_riwayat.pop()
        else:
            print("\nAnda sudah berada di lokasi paling awal (Root).")
            print("Kembali ke menu utama dalam 2 detik ... ")
            time.sleep(2)
            
    elif pilihan == "0":
        simpan_ke_csv(root)
        print(f"\n{pink}" + "="*70 + f"{reset}")
        print("Program ditutup.")
        print("Terimakasih telah menggunakan Direktori Folder Laptop!")
        print(f"{pink}" + "="*70 + f"{reset}")
        break 
    
    else:
        print("\nPilihan salah! Harap ketik angka 0-8!")
