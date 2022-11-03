import os
from read_file_user import data_user,header_data_user
from read_file_gadget import data_gadget,header_data_gadget
from read_file_consumable_history import data_pengambilan_consumable,header_data_pengambilan_consumable
from read_file_consumable import data_consumable,header_data_consumable
from read_file_return_history import data_pengembalian_gadget,header_data_pengembalian_gadget
from read_file_borrow_history import data_peminjaman_gadget,header_data_peminjaman_gadget

def convert_datas_to_string(header,datas):
    string_data = ";".join(header) + "\n"
    for arr_data in datas:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def saveFile(filename,datas_as_string):
    f=open(filename,"w")
    f.write(datas_as_string)
    f.close()

def save():
    directory = input("Masukkan nama folder tempat penyimpanan: ")
    global data_user,data_gadget,data_consumable,data_peminjaman_gadget,data_pengambilan_consumable,data_pengembalian_gadget
    global header_data_consumable,header_data_user,header_data_gadget,header_data_peminjaman_gadget,header_data_pengambilan_consumable,header_data_pengembalian_gadget
    listdata=[data_user,data_gadget,data_consumable,data_peminjaman_gadget,data_pengambilan_consumable,data_pengembalian_gadget]
    listheader=[header_data_user, header_data_gadget, header_data_consumable, header_data_peminjaman_gadget, header_data_pengambilan_consumable, header_data_pengembalian_gadget]
    listfile=["User.csv","gadget.csv","consumable.csv","gadget_borrow_history.csv","consumable_history.csv","gadget_return_history.csv"]
    cwd=os.getcwd()
    if directory not in os.listdir(cwd) :
        os.mkdir(directory)
    for i in range (6):
        saveFile(cwd+"/"+directory+"/"+listfile[i],convert_datas_to_string(listheader[i],listdata[i]))
    print("Berhasil menyimpan data. ")