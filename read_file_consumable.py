from f14 import Load
f = open(f"{Load.load}/consumable.csv","r")
raw_lines = f.readlines()
f.close()
lines =[(raw_lines.replace("\n", "")) for raw_lines in raw_lines]

def pengganti_split(kata, sep=';'):
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
    arr_cpy = array_of_data[:]
    for i in range (5):
        if (i==3):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def ganti_line_ke_data(line):
    raw_array_of_data = pengganti_split(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

# Merupakan Header
data_consumable1= []
header_data_consumable = lines.pop(0)
header_data_consumable = ganti_line_ke_data(header_data_consumable)

for line in lines:
    array_of_data = ganti_line_ke_data(line)
    data_real = ganti_data_ke_real(array_of_data)
    data_consumable1.append(data_real)

data_consumable = data_consumable1
