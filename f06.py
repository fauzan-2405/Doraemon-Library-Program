from read_file_gadget import data_gadget
from read_file_consumable import data_consumable
def hapus_item():
    global data_gadget,data_consumable
    id=input("Masukan ID item: ")
    gadget_id=[i[0] for i in data_gadget]
    gadget_name=[i[1] for i in data_gadget]
    consumable_name=[i[1] for i in data_consumable]
    consumable_id=[i[0] for i in data_consumable]
    pil='K'
    if id in gadget_id:
        temp=gadget_id.index(id)
        pil=input("Anda yakin ingin menghapus "+gadget_name[temp]+" (Y/N) ?")
        if pil=='Y':
            print("Item telah berhasil dihapus dari database")
            data_gadget.pop(temp)
        
    elif id in consumable_id:
        temp=consumable_id.index(id)
        pil=input("Anda yakin ingin menghapus "+consumable_name[temp]+"(Y/N) ?")
        if pil=='Y':
            print("Item telah berhasil dihapus dari database")
            data_consumable.pop(temp)
    else:
        print("Tidak ada item dengan ID tersebut.")