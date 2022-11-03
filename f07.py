from read_file_gadget import data_gadget
from read_file_consumable import data_consumable
def ubah_item():
    global data_gadget,data_consumable
    id=input("Masukan ID: ")
    jumlah_tambah=int(input("Masukan Jumlah: "))
    gadget_id=[i[0] for i in data_gadget]
    consumable_id=[i[0]for i in data_consumable]
    if id in gadget_id:
        data_gadget[gadget_id.index(id)][3]=jumlah_tambah
        print(str(jumlah_tambah), data_gadget[gadget_id.index(id)][1],"berhasil diubah. Stok sekarang:", str(data_gadget[gadget_id.index(id)][3]))
    elif id in consumable_id:
        data_consumable[consumable_id.index(id)][3]=jumlah_tambah
        print(str(jumlah_tambah), data_consumable[consumable_id.index(id)][1], "berhasil diubah. Stok sekarang:", str(data_consumable[consumable_id.index(id)][3]))
    else:
        print("Tidak ada item dengan ID tersebut!")
