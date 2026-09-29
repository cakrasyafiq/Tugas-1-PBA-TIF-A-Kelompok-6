"""
/*
 * 245150207111054 Raditya Ramadhan Eka Widhianto: 4.a — Bibliography Extraction
 * 245150200111056 Zaidan Alvi Zulfan Pramudya: 4.b — Tokenization & Case Folding
 * 245150200111062 Muhammad Azza Arsyada Roziqi: 4.b — Stopword & Frequency Analysis
 * 235150200111040 Putra Cakrawala Aulia Syafiq: 4.c — Subtitle Structure Cleaning
 * 245150207111084 Achmad Yusuf Hamdani Firmansyah: 4.c — Subtitle Text/Tag Cleaning
 */
"""

import os
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Mengunduh corpus stopwords NLTK secara otomatis jika belum tersedia
nltk.download('stopwords', quiet=True)

# 1. Path input dan output
input_path = os.path.join(os.path.dirname(__file__), '..', '2_CaseFoldingAndTokenization', 'output', 'output.txt')
output_local_path = os.path.join(os.path.dirname(__file__), 'output', 'output.txt')
output_final_path = os.path.join(os.path.dirname(__file__), '..', 'Final_Output', 'b_kataunik.txt')

# 2. Baca token hasil tahap sebelumnya (Anggota 2)
with open(input_path, 'r', encoding='utf-8') as f:
    tokens = [line.strip() for line in f if line.strip()]

# 3. Ambil daftar stopword Bahasa Indonesia dari library NLTK
stop_words = set(stopwords.words('indonesian'))

# 4. Filter token menggunakan Regex dan Stopword Removal
# Hanya mengambil token kata alfabet murni (panjang >= 2) dan bukan stopword
word_regex = re.compile(r'^[a-z]{2,}$')
clean_tokens = [t for t in tokens if word_regex.match(t) and t not in stop_words]

# 5. Hitung frekuensi kata dan urutkan secara descending
word_counts = Counter(clean_tokens)
sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

# 6. Ambil 30 kata unik teratas
top_30 = sorted_words[:30]

# 7. Format output sesuai ketentuan (kata\tFrekuensi)
output_lines = ['kata\tFrekuensi']
for word, freq in top_30:
    output_lines.append(f'{word}\t{freq}')

output_content = '\n'.join(output_lines) + '\n'

# 8. Simpan ke file output lokal
os.makedirs(os.path.dirname(output_local_path), exist_ok=True)
with open(output_local_path, 'w', encoding='utf-8') as f:
    f.write(output_content)

# 9. Simpan ke Final_Output (b_kataunik.txt)
os.makedirs(os.path.dirname(output_final_path), exist_ok=True)
with open(output_final_path, 'w', encoding='utf-8') as f:
    f.write(output_content)

print('Selesai! 30 kata unik berhasil disimpan ke output/output.txt dan Final_Output/b_kataunik.txt')