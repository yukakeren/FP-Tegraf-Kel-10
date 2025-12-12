# TUGAS PRAKTIKUM - THE KNIGHT'S TOUR

## Deskripsi Masalah

Jika sebuah bidak kuda diletakkan pada sebarang kotak untuk kemudian melakukan perjalanan (dengan cara pergerakan kuda) mengunjungi ke semua (8 × 8) kotak papan catur.

Jika diinginkan situasi bahwa kuda tsb dapat:
- **a. Mengakhiri perjalanan di sebarang kotak (open tour)**
- **b. Mengakhiri perjalanan pada attacking square (closed tour)**

## Algoritma

Program ini menggunakan **Backtracking** dengan **Warnsdorff's Heuristic**:
- **Backtracking**: Mencoba semua kemungkinan pergerakan secara sistematis dan mundur jika menemui jalan buntu
- **Warnsdorff's Heuristic**: Optimisasi dengan memilih kotak yang memiliki paling sedikit pilihan gerakan selanjutnya, mengurangi kemungkinan jalan buntu

## Fitur

- ✅ Open Tour: Kuda mengunjungi semua kotak tanpa harus kembali ke awal
- ✅ Closed Tour: Kuda mengunjungi semua kotak dan dapat kembali ke awal
- ✅ Visualisasi grafis dengan matplotlib
- ✅ Tracking waktu solusi
- ✅ Dapat memilih posisi awal arbitrary
- ✅ Support berbagai ukuran papan

## Cara Menggunakan

### 1. Menjalankan File Python

```bash
python knights.py
```

### 2. Menggunakan Jupyter Notebook

Buka file `knights_tour.ipynb` untuk versi interaktif dengan penjelasan lengkap.

## Struktur Kode

### Class `KnightsTour`

**Methods:**
- `__init__(board_size, closed_tour)`: Initialize solver
- `solve_tour(start_x, start_y)`: Mencari solusi Knight's Tour
- `visualize(save_fig, filename)`: Visualisasi solusi dengan matplotlib
- `print_board()`: Cetak solusi di console
- `get_path_coordinates()`: Dapatkan koordinat jalur

## Contoh Output

### Open Tour
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

### Visualisasi
Program akan menampilkan visualisasi grafis dengan:
- Papan catur dengan pola warna
- Nomor urutan setiap langkah
- Garis merah menunjukkan jalur
- Penanda hijau untuk posisi awal
- Penanda biru untuk posisi akhir
- Garis putus-putus untuk closed tour (kembali ke awal)

## Kompleksitas

- **Kompleksitas Waktu**: O(8^(n²)) dalam worst case, tetapi Warnsdorff's heuristic secara signifikan mengurangi waktu eksekusi
- **Kompleksitas Ruang**: O(n²) untuk menyimpan papan

## Requirements

```
matplotlib
numpy
```

Install dependencies:
```bash
pip install matplotlib numpy
```

## Catatan

- Closed tour lebih sulit ditemukan dibanding open tour karena constraint tambahan
- Posisi awal mempengaruhi waktu pencarian solusi
- Untuk papan berukuran kecil (< 5×5), solusi mungkin tidak ada

## Author

Tugas Praktikum Tegraf - Kelompok 10

## License

MIT License

