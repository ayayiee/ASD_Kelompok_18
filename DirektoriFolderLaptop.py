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