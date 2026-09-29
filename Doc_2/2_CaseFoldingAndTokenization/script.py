# Zaidan Alvi Zulfan Pramudya
# 245150200111056

import re

# Baca File
with open("../Raw_Data/doc_2.txt", encoding="utf-8", errors="replace") as f:
  teks = f.read()

# Case Folding
teks_kecil = teks.lower()

# Tokenisasi
token = re.split(r'\W+', teks_kecil)
hasil = []  
for t in token:
    if t:   # buang string kosong ''
        hasil.append(t)  

print(len(hasil))
print(hasil[:30])

# Simpan ke output.txt
with open("output/output.txt", "w", encoding="utf-8") as f:
    for t in hasil:
        f.write(t + "\n")