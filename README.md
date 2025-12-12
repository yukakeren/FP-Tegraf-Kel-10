# Tugas Praktikum - The Knight's Tour Problem

## Deskripsi Masalah

Sebuah bidak kuda diletakkan pada sebarang kotak di papan catur berukuran 8 × 8. Kuda tersebut harus melakukan perjalanan dengan aturan pergerakan kuda dalam catur (berbentuk L) untuk mengunjungi semua kotak pada papan.

Terdapat dua situasi yang harus diselesaikan:

a. **Open Tour** - Kuda mengakhiri perjalanan di sebarang kotak (tidak harus kembali ke posisi awal)

b. **Closed Tour** - Kuda mengakhiri perjalanan pada attacking square, yaitu kotak yang memungkinkan kuda kembali ke posisi awal dengan satu gerakan

## Solusi yang Diimplementasikan

### Algoritma

Program ini mengimplementasikan algoritma **Backtracking** yang dikombinasikan dengan **Warnsdorff's Heuristic** untuk menemukan solusi Knight's Tour secara efisien.

#### Backtracking
Algoritma backtracking akan mencoba semua kemungkinan pergerakan kuda secara sistematis. Jika menemui jalan buntu (dead end), algoritma akan mundur dan mencoba jalur alternatif lainnya.

#### Warnsdorff's Heuristic
Sebagai optimisasi, digunakan Warnsdorff's heuristic yang memprioritaskan perpindahan ke kotak yang memiliki lebih sedikit pilihan gerakan selanjutnya. Strategi greedy ini terbukti efektif mengurangi kemungkinan jalan buntu dan mempercepat pencarian solusi.

### Implementasi

Program terdiri dari class `KnightsTour` dengan method-method berikut:

- `__init__(board_size, closed_tour)` - Inisialisasi solver dengan ukuran papan dan tipe tour
- `solve_tour(start_x, start_y)` - Mencari solusi dengan posisi awal tertentu
- `visualize(save_fig, filename)` - Membuat visualisasi grafis dari solusi
- `print_board()` - Menampilkan solusi dalam bentuk matriks di console
- `get_path_coordinates()` - Mendapatkan koordinat jalur yang dilalui

### Fitur Program

- Solusi untuk Open Tour dan Closed Tour
- Visualisasi jalur pergerakan kuda pada papan catur
- Tracking waktu komputasi untuk menemukan solusi
- Fleksibilitas memilih posisi awal
- Mendukung berbagai ukuran papan (tidak hanya 8x8)

## Cara Menggunakan

### Menjalankan Program Python

Jalankan file utama dengan perintah:
```bash
python knights.py
```

Program akan secara otomatis menyelesaikan kedua situasi (open tour dan closed tour) dan menampilkan visualisasinya.

### Menggunakan Jupyter Notebook

Untuk eksplorasi lebih interaktif dengan penjelasan detail, buka file:
```
knights_tour.ipynb
```

Notebook ini berisi penjelasan algoritma, implementasi bertahap, dan berbagai eksperimen dengan ukuran papan yang berbeda.

## Contoh Output

Program akan menghasilkan output berupa matriks yang menunjukkan urutan kunjungan kuda:

```
OPEN TOUR - Knight's Tour Solution:
=================================
  0  59  38  33  30  17   8  63
 37  34  31  60  55  62  29  16
 58   1  56  39  32  27  18   7
 35  36  41  54  61  56  15  28
 42  57  52  47  40  23   6  19
 51  46  43  50  53  20  25  14
 48  43  50  45  24  11   4  21
 45  50  47  44  49  22  13  10
=================================
Solution time: 0.0023 seconds
```

Selain itu, program juga akan menampilkan visualisasi grafis yang menunjukkan:
- Papan catur dengan warna alternatif
- Nomor urutan di setiap kotak yang dikunjungi
- Garis merah yang menggambarkan jalur pergerakan
- Marker hijau untuk posisi awal
- Marker biru untuk posisi akhir
- Untuk closed tour, garis putus-putus dari posisi akhir kembali ke awal

## Analisis Kompleksitas

**Kompleksitas Waktu:** 
Dalam worst case, kompleksitas adalah O(8^(n²)) karena setiap kotak memiliki maksimal 8 pilihan gerakan. Namun dengan Warnsdorff's heuristic, waktu eksekusi praktis jauh lebih cepat.

**Kompleksitas Ruang:** 
O(n²) untuk menyimpan state papan dan rekursi.

## Dependencies

Library yang dibutuhkan:
```
matplotlib >= 3.5.0
numpy >= 1.21.0
```

Instalasi:
```bash
pip install -r requirements.txt
```

atau manual:
```bash
pip install matplotlib numpy
```

## Catatan Pengembangan

Beberapa hal yang perlu diperhatikan:

1. Closed tour memiliki constraint yang lebih ketat sehingga waktu pencarian bisa lebih lama dibanding open tour

2. Posisi awal berpengaruh terhadap waktu pencarian - posisi di sudut atau tepi cenderung lebih cepat

3. Untuk papan dengan ukuran kecil (di bawah 5x5), kemungkinan tidak ada solusi yang valid

4. Algoritma ini deterministik untuk input yang sama akan menghasilkan solusi yang sama

## Kelompok 10

Tugas Praktikum Teknik Grafika

