# Regex Explanation — Subtitle Number & Timestamp Cleaning

## Overview

Script `script.py` menggunakan 3 regex pattern untuk membersihkan file subtitle `.srt` dengan menghapus nomor subtitle, timestamp, dan baris kosong berlebih.

---

## Regex 1 — Menghapus Nomor Subtitle

```python
re.sub(r'^\d+\s*$', '', content, flags=re.MULTILINE)
```

### Penjelasan Pattern: `^\d+\s*$`

| Komponen | Penjelasan |
|----------|------------|
| `^`      | Mencocokkan **awal baris** (bukan awal string, karena flag `re.MULTILINE`) |
| `\d+`    | Mencocokkan **satu atau lebih digit angka** (0-9). `\d` = digit, `+` = satu atau lebih |
| `\s*`    | Mencocokkan **nol atau lebih whitespace** (spasi, tab, dll.). Ini menangani kemungkinan spasi trailing setelah angka |
| `$`      | Mencocokkan **akhir baris** (bukan akhir string, karena flag `re.MULTILINE`) |

### Flag: `re.MULTILINE`
- Membuat `^` dan `$` mencocokkan awal dan akhir **setiap baris**, bukan hanya awal dan akhir seluruh string.
- Tanpa flag ini, `^` hanya cocok di awal string dan `$` hanya di akhir string.

### Contoh

```
Input:                          Hasil:
2                      →       (baris dihapus, menjadi string kosong)
00:00:50,161 --> ...            00:00:50,161 --> ...
Giliranku.                      Giliranku.
```

Baris `2` hanya berisi digit, sehingga cocok dengan pattern dan dihapus. Baris teks seperti `Giliranku.` tidak cocok karena mengandung huruf.

> **Catatan:** Pattern ini juga aman terhadap teks subtitle yang mengandung angka di dalamnya (misal: `"0822 6454 4221"`) karena `^` dan `$` memastikan baris tersebut **hanya** berisi angka, tanpa karakter lain.

---

## Regex 2 — Menghapus Timestamp

```python
re.sub(r'^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*$', '', content, flags=re.MULTILINE)
```

### Penjelasan Pattern: `^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*$`

Pattern ini mencocokkan format timestamp SRT: `HH:MM:SS,mmm --> HH:MM:SS,mmm`

| Komponen | Penjelasan |
|----------|------------|
| `^`          | Awal baris |
| `\d{2}`      | **Tepat 2 digit** — mencocokkan bagian jam (`HH`) |
| `:`          | Karakter titik dua literal — pemisah antara jam, menit, dan detik |
| `\d{2}`      | **Tepat 2 digit** — mencocokkan bagian menit (`MM`) |
| `:`          | Titik dua literal |
| `\d{2}`      | **Tepat 2 digit** — mencocokkan bagian detik (`SS`) |
| `,`          | Karakter koma literal — pemisah antara detik dan milidetik |
| `\d{3}`      | **Tepat 3 digit** — mencocokkan bagian milidetik (`mmm`) |
| `\s*`        | Nol atau lebih whitespace |
| `-->`        | Tanda panah literal — pemisah antara waktu mulai dan waktu selesai |
| `\s*`        | Nol atau lebih whitespace |
| `\d{2}:\d{2}:\d{2},\d{3}` | Pola yang sama untuk **waktu selesai** |
| `\s*`        | Nol atau lebih whitespace trailing |
| `$`          | Akhir baris |

### Struktur Timestamp yang Dicocokkan

```
00:00:50,161 --> 00:00:52,861
│  │  │  │        │  │  │  │
│  │  │  │        │  │  │  └── \d{3}  (milidetik akhir: 861)
│  │  │  │        │  │  └───── \d{2}  (detik akhir: 52)
│  │  │  │        │  └──────── \d{2}  (menit akhir: 00)
│  │  │  │        └─────────── \d{2}  (jam akhir: 00)
│  │  │  └──────────────────── \d{3}  (milidetik awal: 161)
│  │  └─────────────────────── \d{2}  (detik awal: 50)
│  └────────────────────────── \d{2}  (menit awal: 00)
└───────────────────────────── \d{2}  (jam awal: 00)
```

### Contoh

```
Input:                                      Hasil:
00:00:50,161 --> 00:00:52,861      →       (baris dihapus)
Giliranku.                                  Giliranku.
```

---

## Regex 3 — Menghapus Baris Kosong Berlebih

```python
re.sub(r'\n{2,}', '\n', content)
```

### Penjelasan Pattern: `\n{2,}`

| Komponen | Penjelasan |
|----------|------------|
| `\n`     | Karakter **newline** (baris baru) |
| `{2,}`   | Quantifier — mencocokkan **2 atau lebih** kemunculan berturut-turut. `{2,}` berarti minimal 2, tanpa batas atas |

### Kenapa Diperlukan?
Setelah Regex 1 dan 2 menghapus nomor dan timestamp (menggantinya dengan string kosong `''`), baris-baris tersebut menjadi kosong dan menghasilkan newline berturut-turut. Pattern ini mengganti semua newline berlebih menjadi **satu newline** saja.

### Contoh

```
Input (setelah Regex 1 & 2):          Hasil:
                                       Giliranku.
                                       Aku dapat.
Giliranku.                →            Bisa kau buat...
Aku dapat.

                            
Bisa kau buat...
```

---

## Ringkasan

| No. | Pattern | Fungsi | Replacement |
|-----|---------|--------|-------------|
| 1   | `^\d+\s*$` | Menghapus nomor subtitle | `''` (kosong) |
| 2   | `^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*$` | Menghapus timestamp | `''` (kosong) |
| 3   | `\n{2,}` | Menghapus baris kosong berlebih | `\n` (satu newline) |
