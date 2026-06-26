# ===================================================
# Sorting (mengurutkan isi folder A-Z)
# ===================================================
def urutkan_isi(node_sekarang):
    if node_sekarang.isi:
        node_sekarang.isi.sort(key=lambda x: x.folder.lower())
        print(f"\n Isi folder '{node_sekarang.folder}' berhasil diurutkan A-Z.")
    else:
        print("\n Folder kosong, tidak ada yang bisa diurutkan.")
