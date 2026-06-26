import csv
from node import Node

# === TUGAS ANGGOTA 2: ALYAA MARRDLATIL LAH ===
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
        writer.writerow([item.folder, item.tipe, node.folder])
        if item.tipe == "Folder":
            _tulis_rekursif(item, writer)