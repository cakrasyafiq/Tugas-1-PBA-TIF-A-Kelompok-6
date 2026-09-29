# [T1] [PBA] Tugas 1 - Pemrosesan Bahasa Alami

> *"STUDY HARD. DO GOOD AND THE GOOD LIFE WILL FOLLOW."*

---

## A. ATURAN PENGERJAAN & PENGUMPULAN

### Ketentuan Pengerjaan:
1. **Berkelompok:** Dikerjakan berkelompok maksimal 4–5 orang (1 orang tidak dianggap berkelompok). Apabila jumlah mahasiswa ganjil, terpaksa ada 1–2 kelompok yang berjumlah 5 anggota. Mayoritas kelompok beranggotakan 4 orang, bukan 5 orang.
2. **Platform & Tenggat:** Batas waktu dan pengumpulan dilakukan melalui **BRONE**.
3. **Identitas Anggota:** Nama anggota wajib dituliskan di bagian atas kode program dalam bentuk komentar:
   ```python
   /*
    * NIM_1 NAMA_1: peran_mahasiswa_1
    * NIM_2 NAMA_2: peran_mahasiswa_2
    * dst.
    */
   ```
4. **Integritas Akademik:** Dilarang menjiplak/menyontek dengan alasan, cara, atau sesedikit apapun. 
   - Kode program akan dicek menggunakan program pendeteksi plagiarisme.
   - Pengubahan nama variabel, tata letak kode, dll. tidak berpengaruh dan tetap dianggap plagiarisme.
   - Plagiarisme (bahkan hanya satu baris) tidak akan ditolerir dan berisiko mendapatkan nilai **E**.
5. Baca dan pahami soal dengan cermat agar tidak ada poin penilaian yang terlewat. Jika ada hal yang belum dimengerti, segera tanyakan kepada dosen pengampu.

---

### Ketentuan Pengumpulan:
* Perhatikan batas waktu server di BRONE.
* Unggah *soft copy* ke BRONE berupa satu berkas arsip terkompres (`.ZIP` atau `.RAR`) dengan format penamaan:
  ```text
  [TX] [PBA-PRODI-KELAS] NamaMahasiswa.ZIP
  ```
  * **TX**: Kode tugas (misal: `T1` untuk Tugas 1, `TP` untuk Tugas/Proyek Akhir).
  * **PBA**: Kode mata kuliah Pemrosesan Bahasa Alami.
  * **PRODI**: Inisial program studi (`TIF` untuk Teknik Informatika, `TKOM` untuk Teknik Komputer, `SI` untuk Sistem Informasi).
  * **KELAS**: Kode kelas (misal: `A`, `B`, `C`, dst.).
  * **NamaMahasiswa**: Nama ketua kelompok / penanggung jawab unggahan saja (tidak perlu mencantumkan semua nama anggota).
  * *Contoh:* `[T1] [PBA-TIF-B] Elon Gates.ZIP`

#### Isi di Dalam Berkas `.ZIP`:
1. **Berkas `.DOCX` / `.PDF`:** Berisi *source code*, tangkapan layar (*screenshot*) keluaran program, dan penjelasan kode (seluruh jawaban digabung menjadi satu dokumen). Gunakan templat yang disediakan di BRONE pada menu *"Informasi Dosen, Kontrak Kuliah, Nilai Keaktifan, Ketua Kelas, Template"*.
2. **Berkas `.py`:** Format penamaan `T1_NoSoal_NamaMahasiswa.py` (menggunakan garis bawah/*underscore*).
3. Berkas pendukung lainnya yang diperlukan.

---

## B. TUJUAN TUGAS
Pada tugas ini mahasiswa diharapkan:
* Mengetahui dan memahami cara melakukan pemrosesan teks.
* Menguasai pemrosesan teks dasar menggunakan **Regular Expression (Regex)**.
* Mampu melakukan pencarian *string* dan ekstraksi informasi sederhana berbasis Regex.
* Memahami teknik pembuatan pola pencarian Regex serta pemilihan struktur data yang tepat guna mempermudah pengolahan data teks pada ranah pemrosesan bahasa alami.

---

## C. DESKRIPSI TUGAS
Tugas ini menitikberatkan pada pemrosesan teks di tingkat kata untuk kasus sederhana, khususnya pada tahapan pra-pemrosesan (*pre-processing*)—seperti tokenisasi, *case folding*, dan *stopword removal*—serta ekstraksi informasi dari dokumen yang telah disediakan.

---

## D. SOAL DASAR PEMROSESAN TEKS (REGULAR EXPRESSION)

1. Buat program menggunakan **Python (3.x)** untuk memproses dokumen yang tersedia (program ditulis untuk menjawab soal nomor 4).
2. Lakukan *pre-processing* apabila diperlukan (misalnya pembersihan tanda baca). **Perhatian:** Cermati soal terlebih dahulu sebelum menghapus tanda baca, karena beberapa tanda baca masih dibutuhkan untuk ekstraksi pola.
3. Lakukan proses **tokenisasi tingkat kata**. Metode tokenisasi dibebaskan; cara termudah adalah menggunakan Regex berbasis pemisah spasi/*whitespace*.
4. Dari berkas dokumen yang diberikan, ekstraklah informasi berikut:

### Soal 4.a: Ekstraksi Bibliografi (`doc-1.txt`)
Berkas `doc-1.txt` berisi daftar sitasi/referensi, contohnya:
```text
Goldberg, Yoav (2016). "A Primer on Neural Network Models for Natural Language Processing". Journal of Artificial Intelligence Research. 57: 345-420. arXiv:1807.10854.

Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron (2016). Deep Learning. MIT Press.

Jozefowicz, Rafal; Vinyals, Oriol; Schuster, Mike; Shazeer, Noam; Wu, Yonghui (2016). Exploring the Limits of Language Modeling. arXiv:1602.02410.
```

* **Instruksi:** Gunakan Regex untuk mengekstrak informasi ke dalam struktur data dictionary/`dict()` dengan kunci:
  * `authors` : Nama-nama penulis
  * `year` : Tahun penerbitan (jika tahun tidak ditemukan, atribut ini tidak perlu disertakan)
  * `title` : Judul publikasi
* **Format Keluaran:** Simpan ke dalam berkas `a_judul.json` menggunakan modul `json` Python (`import json`).
* **Contoh Format JSON:**
  ```json
  [
    {
      "authors": "Goldberg, Yoav",
      "year": "2016",
      "title": "A Primer on Neural Network Models for Natural Language Processing"
    },
    {
      "authors": "Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron",
      "year": "2016",
      "title": "Deep Learning"
    },
    {
      "authors": "Jozefowicz, Rafal; Vinyals, Oriol; Schuster, Mike; Shazeer, Noam; Wu, Yonghui",
      "year": "2016",
      "title": "Exploring the Limits of Language Modeling"
    },
    {
      "authors": "Choe, Do Kook; Charniak, Eugene",
      "title": "Parsing as Language Modeling"
    }
  ]
  ```

---

### Soal 4.b: Analisis Frekuensi Kata Unik (`doc-2.txt`)
* **Instruksi:** 
  * Temukan **30 kata unik** (di luar *stopword*) beserta frekuensi kemunculannya dari dokumen `doc-2.txt`.
  * Terapkan *case-folding* (*case-insensitive*).
  * Urutkan data secara menurun (*descending*) berdasarkan jumlah frekuensi.
* **Format Keluaran:** Simpan dalam berkas `b_kataunik.txt` dengan pemisah tabulasi (`\t`):
  ```text
  kata	Frekuensi
  ```
  *Contoh:*
  ```text
  yang	100
  di	75
  ```

---

### Soal 4.c: Pembersihan Teks Subtitle Film (`doc_3.srt`)
Berkas `doc_3.srt` merupakan fail takarir (*subtitle*) dengan format:
| Komponen | Penjelasan |
| :--- | :--- |
| `1` | Nomor baris |
| `00:00:00,010 --> 00:00:40,010` | Penanda waktu (*timestamp*) |
| `Teks` | Isi percakapan (dapat terdiri atas lebih dari 1 baris) |
| `<ENTER/NEWLINE>` | Baris kosong pemisah antar percakapan |

* **Instruksi:** Bersihkan (*data cleaning*) berkas tersebut menggunakan **Regex** (tidak boleh sekadar memakai `str.replace()`). Hapus elemen-elemen berikut:
  * Nomor baris
  * Penanda waktu (format `00:00:00,000 --> 00:00:00,000`)
  * Tag HTML/gaya format (misal: `<i>`, `</i>`, `<font>`, dll.)
  * *Newline* atau baris kosong yang tidak diperlukan
* **Format Keluaran:** Simpan hasil teks bersih ke dalam fail `c_subtitle.txt`.
* **Contoh Hasil Pembersihan:**
  ```text
  Giliranku.
  Aku dapat.
  Bisa kau buat...
  ...sedikit lebih menantang?
  Baik. Dengar.
  ```

---

### Soal 5: Dokumentasi Pola Regex
Untuk setiap pola Regex yang dirancang, sertakan penjelasannya secara mendalam di dalam berkas dokumen `.DOCX` serta sebutkan nama anggota yang bertanggung jawab menyusun pola tersebut.

---

## E. REKAPITULASI PENGUMPULAN
Pastikan berkas `.ZIP` atau `.RAR` memuat:
1. **Source Code Python:** Berkas `.py` atau Jupyter Notebook (`.ipynb`).
2. **Dokumen Laporan (`.DOCX`):** Penjelasan detail solusi nomor 4, tangkapan layar, dan keterangan kontribusi/penanggung jawab tiap nomor (anggota yang tidak berkontribusi tidak akan mendapatkan nilai).
3. **Berkas Hasil Eksekusi Program:**
   * `a_judul.json`
   * `b_kataunik.txt`
   * `c_subtitle.txt`
4. Seluruh fail masukan (*input*) dan data pendukung.

> *Selamat mengerjakan sebaik-baiknya. Practice makes perfect.*