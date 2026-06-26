import time

pink = '\033[95m'
reset = '\033[0m'

# === TUGAS ANGGOTA 1: MOUZIA SYAWALOVA ===
class Node:
    def __init__(self, folder, tipe):
        self.folder = folder    
        self.tipe = tipe        
        self.isi = []           
        self.posisi = None      
    
    #=========================================
    # CREATE
    #=========================================
    def tambah_isi(self, node_baru): 
        if self.tipe == "File":
            print("Tidak bisa menambahkan item ke dalam File!")
            return False
        for item in self.isi:
            if item.folder.lower() == node_baru.folder.lower() and item.tipe == node_baru.tipe:
                print(f"{node_baru.tipe} '{node_baru.folder}' sudah ada di lokasi ini!")
                time.sleep(3)
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
            print("Folder Kosong - Gunakan menu 'Tambah' untuk mengisi folder ini.")
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
                
                for cek in self.isi:
                    if cek.folder.lower() == nama_baru.lower() and cek.tipe == item.tipe:
                        print(f"Nama '{nama_baru}' sudah digunakan oleh {item.tipe} lain!")
                        time.sleep(2)
                        return False
                        
                item.folder = nama_baru
                print(f"[Sukses] {item.tipe} '{nama_lama}' telah diubah menjadi {nama_baru}.")
                return True
        print(f"Gagal! {nama_lama} tidak ditemukan di folder ini.")
        return False

    #=========================================
    # DELETE
    #=========================================
    def hapus_isi(self, nama_dihapus):   
        for item in self.isi:
            if item.folder.lower() == nama_dihapus.lower(): #lower membuat jadi huruf kecil agar tidak sensitif
                self.isi.remove(item)
                print(f"Berhasil menghapus {item.tipe} '{item.folder}'! !")
                return True
        print(f"Gagal, {nama_dihapus} tidak ditemukan.")
        return False