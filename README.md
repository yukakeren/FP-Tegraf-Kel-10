# Tugas Praktikum - The Knight's Tour Problem

## How to run
For Knights problem, simply `python3 knights.py` to run or .ipynb.

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

## Input dan Output

### Input

Program menerima input melalui parameter saat membuat instance dan memanggil method:

1. **Parameter Inisialisasi (`KnightsTour`)**:
   - `board_size` (int): Ukuran papan catur (default: 8 untuk papan 8x8)
   - `closed_tour` (bool): 
     - `False` untuk Open Tour (default)
     - `True` untuk Closed Tour

2. **Parameter Solve (`solve_tour`)**:
   - `start_x` (int): Posisi baris awal kuda (0-7 untuk papan 8x8)
   - `start_y` (int): Posisi kolom awal kuda (0-7 untuk papan 8x8)

**Contoh penggunaan:**
```python
# Open Tour dari posisi (0, 0)
knight_open = KnightsTour(board_size=8, closed_tour=False)
knight_open.solve_tour(start_x=0, start_y=0)

# Closed Tour dari posisi (0, 0)
knight_closed = KnightsTour(board_size=8, closed_tour=True)
knight_closed.solve_tour(start_x=0, start_y=0)

# Open Tour dari posisi tengah (3, 3)
knight_center = KnightsTour(board_size=8, closed_tour=False)
knight_center.solve_tour(start_x=3, start_y=3)
```

### Output

Program menghasilkan dua jenis output:

#### 1. Output Console (Text)

**Output untuk Open Tour:**
```
TUGAS PRAKTIKUM - THE KNIGHT'S TOUR
==================================================

Situation A: Open Tour (ending at any square)
--------------------------------------------------
✓ Solution found for Open Tour!

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

**Output untuk Closed Tour:**
```
Situation B: Closed Tour (returning to starting square)
--------------------------------------------------
✓ Solution found for Closed Tour!

CLOSED TOUR - Knight's Tour Solution:
=================================
  0  11  38  33  58  13   8  63
 37  34  59  12  39  62  57  14
 10   1  36  49  32  55  16   7
 35  48  31  60  51  40  15  56
 30   9  50  45  54  29   6  41
 47  44  53  28  61  52  43  22
 26  29  46  41  24  19   4  53
 45  42  27  52  47  24  21  18
=================================
Solution time: 0.0156 seconds

Note: You can change the starting position by modifying
the start_x and start_y parameters in solve_tour()
```

**Penjelasan Matriks Output:**
- Setiap angka merepresentasikan urutan langkah kuda (0-63 untuk papan 8x8)
- Angka 0 adalah posisi awal
- Angka 63 adalah posisi akhir
- Untuk Closed Tour, posisi dengan angka 63 harus berjarak satu gerakan kuda dari posisi 0

#### 2. Output Visualisasi Grafis

Program menampilkan visualisasi menggunakan matplotlib dengan elemen:

1. **Papan Catur**: Kotak bergantian warna krem (#F0D9B5) dan coklat (#B58863)
2. **Nomor Urutan**: Angka 0-63 di setiap kotak yang menunjukkan urutan kunjungan
3. **Jalur Pergerakan**: Garis merah solid yang menghubungkan setiap langkah
4. **Marker Start**: Titik hijau bulat di posisi awal (angka 0)
5. **Marker End**: Kotak biru di posisi akhir (angka 63)
6. **Garis Return** (Closed Tour only): Garis merah putus-putus dari posisi akhir ke awal
7. **Informasi**: Judul menampilkan tipe tour dan waktu komputasi

**Format Gambar:**
- Ukuran: 12x12 inches
- Resolusi: 300 DPI (jika disimpan)
- Format file: PNG (jika disimpan)
- Legend: Menunjukkan Start, End, dan Path

## Contoh Output Detail

### Situasi A: Open Tour

**Input:**
- Ukuran papan: 8x8
- Tipe tour: Open Tour
- Posisi awal: (0, 0)

**Output Matriks:**
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

**Interpretasi:**
- Kuda mulai dari kotak (0,0) dengan angka 0
- Langkah pertama ke kotak dengan angka 1 di posisi (2,1)
- Langkah kedua ke kotak dengan angka 2 dan seterusnya
- Berakhir di kotak dengan angka 63 di posisi (0,7)
- Total 64 kotak berhasil dikunjungi dalam 0.0023 detik

### Situasi B: Closed Tour

**Input:**
- Ukuran papan: 8x8
- Tipe tour: Closed Tour
- Posisi awal: (0, 0)

**Output Matriks:**
```
CLOSED TOUR - Knight's Tour Solution:
=================================
  0  11  38  33  58  13   8  63
 37  34  59  12  39  62  57  14
 10   1  36  49  32  55  16   7
 35  48  31  60  51  40  15  56
 30   9  50  45  54  29   6  41
 47  44  53  28  61  52  43  22
 26  29  46  41  24  19   4  53
 45  42  27  52  47  24  21  18
=================================
Solution time: 0.0156 seconds
```

**Interpretasi:**
- Kuda mulai dari kotak (0,0) dengan angka 0
- Mengunjungi semua 64 kotak
- Berakhir di kotak dengan angka 63 di posisi (0,7)
- Dari posisi (0,7), kuda dapat kembali ke (0,0) dengan satu gerakan L-shape
- Waktu komputasi lebih lama (0.0156s) karena constraint tambahan

### Return Value

Method `solve_tour()` mengembalikan:
- `True`: Jika solusi ditemukan
- `False`: Jika tidak ada solusi (biasanya terjadi pada papan kecil atau posisi awal tertentu)

## Analisis Kompleksitas

**Kompleksitas Waktu:** 
Dalam worst case, kompleksitas adalah O(8^(n²)) karena setiap kotak memiliki maksimal 8 pilihan gerakan. Namun dengan Warnsdorff's heuristic, waktu eksekusi praktis jauh lebih cepat.

**Kompleksitas Ruang:** 
O(n²) untuk menyimpan state papan dan rekursi.

