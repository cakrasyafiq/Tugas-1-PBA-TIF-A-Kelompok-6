# Achmad Yusuf Hamdani Firmansyah
# 2451050207111084

# Import library
import re
import os

# Path input dan output
# Input mengambil dari hasil tahap sebelumnya (Anggota 4)
input_path = os.path.join(os.path.dirname(__file__), '..', '4_SubtitleNumberAndTimestampAndNewlineCleaning', 'output', 'output.txt')

# Path output folder 5_HTMLStyleTagCleaning
output_local_path = os.path.join(os.path.dirname(__file__), '..', '5_HTMLStyleTagCleaning', 'output', 'output.txt')
# Path output folder Final_Output
output_final_path = os.path.join(os.path.dirname(__file__), '..', 'Final_Output', 'c_subtitle.txt')

# Read file SRT
with open(input_path, 'r', encoding='utf-8') as file:
    teks_subtitle = file.read()

# Regex pattern untuk menghapus tag seperti <i>, </i>, atau <fontcolor=#FFF000>
text_subtitle = re.sub(r'<.*?>', '', teks_subtitle)

# Simpan hasil file output
# folder 5_HTMLStyleTagCleaning
os.makedirs(os.path.dirname(output_local_path), exist_ok=True)

with open(output_local_path, 'w', encoding='utf-8') as file:
    file.write(text_subtitle)

# Path output folder Final_Output
os.makedirs(os.path.dirname(output_final_path), exist_ok=True)

with open(output_final_path, 'w', encoding='utf-8') as file:
    file.write(text_subtitle)

print("Pembersihan Tag HTML selesai! File tersimpan")