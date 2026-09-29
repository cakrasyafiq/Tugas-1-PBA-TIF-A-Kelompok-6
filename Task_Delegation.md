# Guide Awal Pembagian Tugas

## Tugas 1 — Pemrosesan Bahasa Alami

> Dokumen ini digunakan sebagai **acuan awal pembagian tugas** dalam kelompok. Detail teknis pelaksanaan, integrasi kode, workflow, dan hal-hal lainnya akan didiskusikan bersama anggota kelompok setelah pembagian tugas disepakati.

---

# 1. Gambaran Umum Tugas

Tugas berfokus pada pemrosesan teks menggunakan **Regular Expression (Regex)**, termasuk:

* Pre-processing teks
* Tokenisasi tingkat kata
* Case folding
* Stopword removal
* Ekstraksi informasi menggunakan Regex
* Analisis frekuensi kata
* Cleaning subtitle

Terdapat tiga bagian utama:

| Soal    | Input       | Output           |
| ------- | ----------- | ---------------- |
| **4.a** | `doc-1.txt` | `a_judul.json`   |
| **4.b** | `doc-2.txt` | `b_kataunik.txt` |
| **4.c** | `doc_3.srt` | `c_subtitle.txt` |

Selain implementasi program, setiap pola Regex yang dirancang perlu dijelaskan dan penanggung jawabnya dicantumkan dalam laporan.

---

# 2. Pembagian Tugas Tim

Pembagian dilakukan menjadi **5 bagian technical**, sehingga setiap anggota memiliki kontribusi langsung terhadap implementasi.

| Anggota       | Tugas                                   | Fokus                                                      |
| ------------- | --------------------------------------- | ---------------------------------------------------------- |
| **Anggota 1** | **4.a — Bibliography Extraction**       | Ekstraksi `authors`, `year`, dan `title` menggunakan Regex |
| **Anggota 2** | **4.b — Tokenization & Case Folding**   | Case folding dan tokenisasi teks                           |
| **Anggota 3** | **4.b — Stopword & Frequency Analysis** | Stopword removal dan analisis frekuensi kata               |
| **Anggota 4** | **4.c — Subtitle Structure Cleaning**   | Cleaning nomor subtitle, timestamp, dan newline            |
| **Anggota 5** | **4.c — Subtitle Text/Tag Cleaning**    | Cleaning HTML/style tags pada subtitle                     |

---

# 3. Anggota 1 — Bibliography Extraction

### Fokus

**Soal 4.a — Ekstraksi Bibliografi**

### Input

```text
doc-1.txt
```

### Output

```text
a_judul.json
```

### Tanggung Jawab

Membuat program menggunakan Regex untuk mengekstrak informasi:

* `authors`
* `year`
* `title`

Hasil ekstraksi disimpan dalam struktur `dictionary`, kemudian disimpan dalam format JSON.

### Alur

```text
doc-1.txt
    ↓
Regex
    ↓
Extract:
    ├── authors
    ├── year
    └── title
    ↓
Dictionary
    ↓
a_judul.json
```

### Contoh Struktur

```python
{
    "authors": "Goldberg, Yoav",
    "year": "2016",
    "title": "A Primer on Neural Network Models for Natural Language Processing"
}
```

Jika tahun tidak ditemukan, atribut `year` tidak perlu disertakan.

### Fokus Pembahasan

* Pola Regex bibliografi
* Ekstraksi nama penulis
* Ekstraksi tahun
* Ekstraksi judul
* Pembentukan dictionary
* Penyimpanan hasil dalam JSON

---

# 4. Anggota 2 — Tokenization & Case Folding

### Fokus

**Bagian preprocessing untuk Soal 4.b**

### Input

```text
doc-2.txt
```

### Tanggung Jawab

Mengerjakan tahap awal pemrosesan teks sebelum analisis frekuensi.

Tahapan utama:

```text
doc-2.txt
    ↓
Case Folding
    ↓
Tokenization
    ↓
Tokens
```

### Case Folding

Memastikan pencarian kata dilakukan secara **case-insensitive**.

Contoh:

```text
Language
LANGUAGE
language
```

dianggap sebagai kata yang sama:

```text
language
```

### Tokenisasi

Melakukan tokenisasi pada tingkat kata.

Contoh:

```text
Natural Language Processing
```

menjadi:

```python
["natural", "language", "processing"]
```

### Fokus Pembahasan

* Case folding
* Tokenisasi tingkat kata
* Regex yang digunakan untuk tokenisasi jika diperlukan
* Bentuk data hasil tokenisasi

---

# 5. Anggota 3 — Stopword & Frequency Analysis

### Fokus

**Bagian lanjutan Soal 4.b**

### Input

Token hasil preprocessing.

### Output

```text
b_kataunik.txt
```

### Alur

```text
Tokens
    ↓
Stopword Removal
    ↓
Frequency Counting
    ↓
Sorting Descending
    ↓
30 Kata Unik
    ↓
b_kataunik.txt
```

### Tanggung Jawab

#### Stopword Removal

Menghapus kata yang termasuk stopword sehingga tidak ikut dalam perhitungan frekuensi.

#### Frequency Counting

Menghitung jumlah kemunculan setiap kata.

Contoh:

```text
language → 25
model    → 18
text     → 15
```

#### Sorting

Mengurutkan kata berdasarkan frekuensi secara **descending**.

#### Top 30

Mengambil **30 kata unik** sesuai ketentuan soal.

### Format Output

```text
kata    Frekuensi
language    25
model       18
text        15
```

### Fokus Pembahasan

* Stopword removal
* Frequency counting
* Sorting
* Pemilihan 30 kata unik
* Format output

---

# 6. Anggota 4 — Subtitle Structure Cleaning

### Fokus

**Bagian struktur Soal 4.c**

### Input

```text
doc_3.srt
```

### Tanggung Jawab

Membuat Regex untuk membersihkan elemen struktural pada file subtitle.

Elemen yang menjadi fokus:

1. Nomor subtitle
2. Timestamp
3. Newline atau baris kosong yang tidak diperlukan

### Contoh

Input:

```text
1
00:00:00,010 --> 00:00:40,010
Giliranku.

2
00:00:41,000 --> 00:00:43,000
Aku dapat.
```

Setelah struktur dibersihkan:

```text
Giliranku.

Aku dapat.
```

### Fokus Pembahasan

* Regex untuk nomor subtitle
* Regex untuk timestamp
* Penanganan newline
* Penanganan baris kosong
* Struktur file `.srt`

---

# 7. Anggota 5 — HTML/Style Tag Cleaning

### Fokus

**Bagian text cleaning Soal 4.c**

### Input

```text
doc_3.srt
```

atau hasil preprocessing dari bagian struktur subtitle.

### Tanggung Jawab

Membuat Regex untuk menghapus **HTML/style tags** yang terdapat pada subtitle.

### Contoh

Input:

```text
<i>Giliranku.</i>
```

Menjadi:

```text
Giliranku.
```

Contoh lain:

```text
<font color="red">Aku dapat.</font>
```

Menjadi:

```text
Aku dapat.
```

### Fokus Pembahasan

* Deteksi HTML/style tags menggunakan Regex
* Opening tags
* Closing tags
* Tag dengan atribut
* Penghapusan tag tanpa menghilangkan isi teks

### Output

Hasil akhirnya akan menjadi bagian dari:

```text
c_subtitle.txt
```

---

# 8. Ringkasan Pembagian

|   No. | Anggota | Bagian  | Kontribusi Technical                           |
| ----: | ------- | ------- | ---------------------------------------------- |
| **1** | Nama 1  | **4.a** | Bibliography Extraction menggunakan Regex      |
| **2** | Nama 2  | **4.b** | Case Folding + Tokenization                    |
| **3** | Nama 3  | **4.b** | Stopword Removal + Frequency Analysis          |
| **4** | Nama 4  | **4.c** | Subtitle Number + Timestamp + Newline Cleaning |
| **5** | Nama 5  | **4.c** | HTML/Style Tag Cleaning                        |

---

## Catatan

Pembagian di atas merupakan **pembagian awal berdasarkan bagian technical dari soal**.

Hal-hal seperti:

* pembagian file,
* struktur program,
* cara menggabungkan kode,
* penggunaan Git/GitHub,
* format laporan,
* pembagian dokumentasi,
* dan teknis pengerjaan lainnya

**belum ditentukan dalam dokumen ini** dan akan dibahas bersama anggota kelompok setelah pembagian tugas disepakati.
