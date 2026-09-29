# Putra Cakrawala Aulia Syafiq
# 235150200111040

# Lanjutin kode masing masing

import re
import os

# Path input dan output
input_path = os.path.join(os.path.dirname(__file__), '..', 'Raw_data', 'doc_3.srt')
output_path = os.path.join(os.path.dirname(__file__), 'output', 'output.txt')

# Read file SRT
with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex pattern untuk menghapus nomor subtitle dan timestamp
# 1. Hapus baris yang hanya berisi angka (nomor subtitle)
content = re.sub(r'^\d+\s*$', '', content, flags=re.MULTILINE)

# 2. Hapus baris timestamp (format: HH:MM:SS,mmm --> HH:MM:SS,mmm)
content = re.sub(r'^\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3}\s*$', '', content, flags=re.MULTILINE)

# 3. Hapus baris kosong berlebih (ganti 2+ newline berturut-turut menjadi 1 newline)
content = re.sub(r'\n{2,}', '\n', content)

# 4. Hapus newline di awal dan akhir
content = content.strip()

# Simpan hasil ke file output
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)