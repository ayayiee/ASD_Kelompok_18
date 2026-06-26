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
        print(f"\n'{nama_cari}' tidak ditemukan.")

# ===================================================
# Searching (mencari ke dalam semua sub-folder)
# ===================================================
def _cari_rekursif(node, nama_cari, hasil, path_sekarang=""):
    path_baru = f"{path_sekarang}/{node.folder}" if path_sekarang else node.folder
    if nama_cari.lower() in node.folder.lower():
        hasil.append(f"[{node.tipe}] {path_baru}")
    
    for item in node.isi:
        _cari_rekursif(item, nama_cari, hasil, path_baru)
