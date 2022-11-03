from read_file_gadget import data_gadget
from read_file_consumable import data_consumable
def cek_id(dicari):
    global data_gadget,data_consumable
    temp1=[i[0] for i in data_gadget]
    temp2=[i[0] for i in data_consumable]
    return dicari in temp1 or dicari in temp2
def tambah_item():
    global data_gadget,data_consumable
    id=input("Masukkan ID: ")
    huruf_awal=id[0]
    if huruf_awal=='G' and not cek_id(id):
        nama=input("Masukan nama: ")
        desc=input("Masukan Deskripsi: ")
        jumlah=int(input("Masukkan jumlah: "))
        rarity_scale=["S","A","B","C"]
        rarity=input("Masukkan rarity: ")
        if rarity not in rarity_scale:
            print("Rarity tidak valid!!!")
            return
        tahun=input("Masukan tahun ditemukan: ")
        print("Item telah berhasil ditambahkan ke database.")
        data_gadget.append([id,nama,desc,jumlah,rarity,tahun])
    elif huruf_awal =='C' and not cek_id(id):
        nama=input("Masukan nama: ")
        desc=input("Masukan Deskripsi: ")
        jumlah=int(input("Masukkan jumlah: "))
        rarity=input("Masukkan rarity: ")
        print("Item telah berhasil ditambahkan ke database.")
        data_consumable.append([id,nama,desc,jumlah,rarity])
    elif cek_id(id):
        print("Gagal menambahkan karena ID sudah ada")
    else:
        print("Gagal menambahkan item karena ID tidak valid.")

