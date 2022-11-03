from datetime import datetime
from read_file_user import data_user
from read_file_gadget import data_gadget
from read_file_borrow_history import data_peminjaman_gadget
                
def print_riwayatpinjam(i,date_list):
    # Fungsi ini digunakan untuk menampilkan data riwayat peminjaman gadget ke user
    print("ID peminjaman: ", date_list[i][4] )
    print("ID gadget:", date_list[i][1])
    print("Nama gadget:", cari_gadget(date_list[i][1]))
    print("ID peminjam:", date_list[i][0])
    print("Nama pengambil:", cari_nama(date_list[i][0]))
    print("Tanggal peminjaman:", date_list[i][2])
    print("Jumlah:", date_list[i][3])
    print("\n")

def urutkan_tanggal ():
    raw_date_list=""
    # Fungsi ini digunakan untuk menciptakan list baru dengan elemen dari list
    # data_peminjaman_gadget yang sudah di sort berdasarkan tanggal
    raw_date_list = []
    for i in range (len(data_peminjaman_gadget)):
        raw_date_list.append(data_peminjaman_gadget[i])
    raw_date_list.sort(key=lambda date : datetime.strptime(date[2], "%d/%m/%Y"), reverse = True)
    return raw_date_list        

def cari_nama(id_peminjam):
    nama_usr=""
    # Fungsi ini digunakan untuk mencari nama dari id peminjam
    for i in range (len(data_user)):
        if id_peminjam == data_user[i][0]:
            nama_usr = data_user[i][2]
    return nama_usr

def cari_gadget(id_gadget):
    nama_gdgt=""
    # Fungsi ini digunakan untuk mencari nama gadget dari id gadget
    for i in range (len(data_gadget)):
        if id_gadget == data_gadget[i][0]:
            nama_gdgt = data_gadget[i][1]
    return nama_gdgt
            
def riwayatpinjam():
    # Fungsi ini digunakan untuk menampilkan fungsi print_riwayatpinjam
    date_list = urutkan_tanggal()
    if len(date_list) > 5 : # Jika banyak data > 5 maka ditampilkan 5 data terlebih dahulu
        a = 0
        b = 5
        for i in range (a,b):
            print_riwayatpinjam(i,date_list)
        pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
        # Jika input tidak valid maka dikeluarkan pesan kesalahan
        while (pil != "Y") and (pil != "y") and (pil != "N") and (pil != "n"):
            print("Maaf, input kamu tidak valid, Silakan masukkan kembali")
            pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
        # Input valid
        while (pil == "Y" or pil == "y"):
            a += 5
            b += 5
            if (b>len(date_list)):
                c = len(date_list) % 5 
                b -= 5
                for i in range (a,b+c):
                    print_riwayatpinjam(i,date_list)
                print("Entry data telah habis")
                break 
            else :
                for i in range (a,b):
                    print_riwayatpinjam(i,date_list)
            pil = input("Tampilkan entry data selanjutnya? (y/n) : ")

    elif len(date_list) == 0 : # Jika jumlah datanya 0 maka dikeluarkan tidak ada data
        print("Tidak ada data")
        
    else : # Jika jumlah data < 5 maka tampilkan semuanya
        for i in range (len(date_list)):
            print_riwayatpinjam(i,date_list)

#riwayatpinjam()
