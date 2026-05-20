# 📂 Virtual File System - CLI Directory Management

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey.svg)

Proyek ini adalah aplikasi Sistem Manajemen Direktori Berkas (*Virtual File System*) berbasis *Command Line Interface* (CLI) yang dibangun menggunakan bahasa pemrograman Python. Proyek ini disusun untuk memenuhi Tugas Proyek Akhir mata kuliah **Algoritma & Struktur Data** pada program studi D4 Teknologi Rekayasa Perangkat Lunak, Sekolah Vokasi IPB University.

## 👥 Tim Pengembang (Kelompok 3)
- **Mouzia Syawalova** (Fokus: Core System, Struktur Data General Tree & Fungsi CRUD)
- **Alyaa Marrdlatillah** (Fokus: Processing System, Algoritma Rekursif Searching, Sorting A-Z & Database File Handling)
- **Gabriella Anggi** (Fokus: Project Manager, CLI UI/UX, Stack Riwayat Navigasi & Input Validation Protection)

## 💡 Konsep & Struktur Data
Aplikasi ini menerapkan dua kombinasi struktur data terintegrasi untuk menyimulasikan operasional sistem berkas lokal pada sistem operasi:
1. **General Tree:** Digunakan sebagai fondasi utama untuk memodelkan struktur direktori (Folder bertindak sebagai *Parent/Node*, File bertindak sebagai *Leaf*, yang saling terhubung secara non-linear melalui pointer dinamis).
2. **Stack (LIFO - Last In First Out):** Digunakan untuk mengelola riwayat penjelajahan jalur direktori (*backtracking*), sehingga ketika pengguna ingin kembali ke folder induk, sistem tahu jalur mundur secara kronologis.

## ✨ Fitur Utama
- **Antarmuka Responsif:** Tampilan terminal rapi yang dilengkapi dengan pelacak jalur aktif (*Real-time Path Tracker*) serta visualisasi warna (*pink ansi code*).
- **Manajemen Berkas Lengkap (CRUD):** Pengguna dapat membuat baru, melihat isi dengan filter tipe, mengubah nama (*rename*), hingga menghapus folder/file secara aman.
- **Navigasi Pintar (*Loop Input Validation*):** Dilengkapi proteksi salah ketik saat membuka folder. Sistem akan terus mengunci pengguna untuk mencoba lagi hingga ejaan benar atau dibatalkan secara sengaja.
- **Pencarian & Pengurutan Instan:** Memiliki fitur pencarian berkas global secara rekursif dari tingkat *Root* dan pengurutan isi direktori secara alfabetis (A-Z).
- **Sistem Pembatalan Universal:** Pengguna dapat membatalkan aksi manipulasi data kapan saja hanya dengan mengetikkan karakter `'x'` atau mengosongkan input, disertai transisi otomatis menggunakan `time.sleep()`.
- **Penyimpanan Permanen (*Auto-Save*):** Setiap perubahan data direktori otomatis disinkronisasikan dan disimpan ke dalam file eksternal `data_folder.csv`.

## 🛠️ Prasyarat & Instalasi
Aplikasi ini sepenuhnya menggunakan *built-in libraries* bawaan Python (seperti `csv` dan `time`), sehingga Anda tidak perlu menginstal pustaka pihak ketiga tambahan.

1. Clone *repository* ini:
   ```bash
   git clone https://github.com/gabriellaanggi/VirtualFileSystem.git
   cd ASD_Kelompok_18

2. Jalankan aplikasi langsung
   python Direktori-Folder-Laptop.py

## 📂 Struktur Direktori
VirtualFileSystem/
│
├── data_folder.csv              # Database utama penyimpanan Tree (format CSV)
├── Direktori-Folder-Laptop      # File eksekusi keseluruhan
└── README.md                    # Dokumentasi proyek

## 🔒 Catatan Penggunaan
Fitur Pembatalan: Saat Anda berada di menu Tambah (2), Ubah Nama (3), atau Hapus (4), Anda cukup mengetikkan huruf x (case-insensitive) atau langsung menekan Enter pada kolom input untuk kembali ke menu utama secara aman tanpa merusak struktur data yang ada.
Navigasi Mundur: Menu Kembali (8) hanya dapat digunakan jika Anda telah masuk ke dalam minimal satu sub-folder (Stack tidak kosong). Jika Anda berada di direktori tertinggi (Root), sistem akan memberikan notifikasi batasan navigasi.
