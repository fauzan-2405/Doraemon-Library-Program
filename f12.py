# Silahkan download/copy dulu read_file_riwayat_pengembalian_gadget yang udah kusediain
from datetime import datetime
from read_file_return_history import data_pengembalian_gadget
from read_file_borrow_history import data_peminjaman_gadget
from read_file_user import data_user
from read_file_gadget import data_gadget

def print_riwayatpengembalian(i,date_list, user, gadget):
    # Fungsi ini digunakan untuk menampilkan data riwayat pengembalian gadget ke user
    print("ID pengembalian:", date_list[i][0])
    print("Nama pengambil:", user[i])
    print("Nama gadget:", gadget[i])
    print("Tanggal peminjaman:", date_list[i][2])
    print("\n")

def letak_gadget(id_pinjam):
    # Fungsi ini digunakan untuk mencari letak kolom dari gadget
    idx = 0
    for i in range (len(data_gadget)):
        if data_gadget[i][0] == id_pinjam :
            idx = i
    return idx

def idx_user(user_id):
    #fungsi mencari letak/index baris data user 
    for i in range (len(data_user)):
        if data_user[i][0] == user_id:
            idx = i
    return idx

def list_user(date_list):
    #fungsi ini mengumpulkan nama-nama user yang telah melakukan pengembalian
    users = []
    for i in range (len(date_list)):
        for j in range (len(data_peminjaman_gadget)):
            if date_list[i][1] == data_peminjaman_gadget[j][4]:
                user = data_user[idx_user(data_peminjaman_gadget[j][0])][2]
                users.append(user)
    return users

def list_gadget(date_list):
    #fungsi ini mengumpulkan nama-nama gadet yang telah dikembalikan
    gadgets = []
    for i in range (len(date_list)):
        for j in range (len(data_peminjaman_gadget)):
            if date_list[i][1] == data_peminjaman_gadget[j][4]:
                gadget = data_gadget[letak_gadget(data_peminjaman_gadget[j][1])][1]
                gadgets.append(gadget)
    return gadgets

def urutkan_tanggal ():
    # Fungsi ini digunakan untuk menciptakan list baru dengan elemen dari list
    # data_pengembalian_gadget yang sudah di sort berdasarkan tanggal
    raw_date_list = []
    for i in range (len(data_pengembalian_gadget)):
        raw_date_list.append(data_pengembalian_gadget[i])
    raw_date_list.sort(key=lambda date : datetime.strptime(date[2], "%d/%m/%Y"), reverse = True)
    return raw_date_list        
    
def riwayatpengembalian():
    # Fungsi ini digunakan untuk menampilkan fungsi print_riwayatpinjam
    date_list = urutkan_tanggal()
    user_list = list_user(date_list)
    gadget_list = list_gadget(date_list)
    if len(date_list) > 5 : # Jika banyak data > 5 maka ditampilkan 5 data terlebih dahulu
        a = 0
        b = 5
        for i in range (a,b):
            print_riwayatpengembalian(i,date_list, user_list, gadget_list)
        pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
        # Jika input tidak valid maka dikeluarkan pesan kesalahan
        while (pil != "Y") and (pil != "y") and (pil != "N") and (pil != "n"):
            print("Maaf, input kamu tidak valid, Silakan masukkan kembali")
            pil = input(("Tampilkan entry data selanjutnya? (y/n) : "))
        #  Input valid
        while (pil == "Y" or pil == "y"):
            a += 5
            b += 5
            if (b>len(date_list)):
                c = len(date_list) % 5 
                b -= 5
                for i in range (a,b+c):
                    print_riwayatpengembalian(i,date_list, gadget_list)
                print("Entry data telah habis")
                break 
            else :
                for i in range (a,b):
                    print_riwayatpengembalian(i,date_list, user_list, gadget_list)
            pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
            
    elif len(date_list) == 0 : # Jika jumlah datanya 0 maka dikeluarkan tidak ada data
        print("Tidak ada data")
        
    else : # Jika jumlah data < 5 maka tampilkan semuanya
        for i in range (len(date_list)):
            print_riwayatpengembalian(i,date_list, user_list, gadget_list)

#riwayatpengembalian()