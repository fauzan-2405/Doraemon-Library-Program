# FILE INI DIPAKE BUAT NGE READ FILE GADGET
# JADINYA NANTI KITA NGE IMPORT data_gadget DARI FILE INI
# KLO DIBUAT SATU SATU RIWEH EUY
from f14 import Load
f = open(f"{Load.load}/gadget.csv","r")
raw_lines = f.readlines()
f.close()
lines =[(raw_lines.replace("\n", "")) for raw_lines in raw_lines]

def pengganti_split(kata, sep=';'):
# Fungsi ini digunakan untuk men-split line(kata) dari chr ";"
# dengan memanfaatkan fungsi rekursif
    kata = kata.lstrip(sep)
    if sep in kata:
        pos = kata.index(sep)
        found = kata[:pos]
        remainder = pengganti_split(kata[pos+1:])
        remainder.insert(0, found)
        return remainder
    else:
        return [kata]

def ganti_data_ke_real(array_of_data):
# Fungsi ini digunakan untuk mengganti nilai data ke nilai real(asli) nya
    arr_cpy = array_of_data[:]
    for i in range (6):
    # Dalam file gadget terdapat 6 kolom
        if (i==3) or (i==5):
            # Kolom dgn index (3) dan (5), yaitu "jumlah" dan "tahun_ditemukan"
            # sehingga akan diubah nilainya dari str menjadi int
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def ganti_line_ke_data(line):
# Fungsi ini digunakan untuk mengganti line menjadi data sekaligus membersihkan
# jika ada spasi yang berlebih
    raw_array_of_data = pengganti_split(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

# Merupakan Header
data_gadget1= []
header_data_gadget = lines.pop(0)
header_data_gadget = ganti_line_ke_data(header_data_gadget)

for line in lines:
    array_of_data = ganti_line_ke_data(line)
    data_real = ganti_data_ke_real(array_of_data)
    data_gadget1.append(data_real)

data_gadget = data_gadget1

