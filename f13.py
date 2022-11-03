from datetime import datetime
from read_file_user import data_user
from read_file_consumable import data_consumable
from read_file_consumable_history import data_pengambilan_consumable


def print_riwayatambil(i, date_list):
    # Fungsi ini digunakan untuk menampilkan data riwayat pengambilan item ke user
    print("ID pengambilan: ", date_list[i][0])
    print("ID consumable:", date_list[i][2])
    print("Nama item:", cari_consumable(date_list[i][2]))
    print("Nama pengambil:", cari_nama(date_list[i][1]))
    print("Tanggal pengambilan:", date_list[i][3])
    print("Jumlah:", date_list[i][4])
    print("\n")


def urutkan_tanggal():
    # Fungsi ini digunakan untuk menciptakan list baru dengan elemen dari list
    # data_pengambilan_consumable yang sudah di sort berdasarkan tanggal
    raw_date_list = []
    for i in range(len(data_pengambilan_consumable)):
        raw_date_list.append(data_pengambilan_consumable[i])
    raw_date_list.sort(key=lambda date: datetime.strptime(date[3], "%d/%m/%Y"), reverse=True)
    return raw_date_list


def cari_nama(id_pengambil):
    nama_usr=""
    # Fungsi ini digunakan untuk mencari nama dari id pengambil
    for i in range(len(data_user)):
        if id_pengambil == data_user[i][0]:
            nama_usr = data_user[i][2]
    return nama_usr


def cari_consumable(id_consumable):
    nama_cnsmble=""
    # Fungsi ini digungadgeakan untuk mencari nama gadget dari id gadget
    for i in range(len(data_consumable)):
        if id_consumable == data_consumable[i][0]:
            nama_cnsmble = data_consumable[i][1]
    return nama_cnsmble


def riwayatambil():
    # Fungsi ini digunakan untuk menampilkan fungsi print_riwayatpinjam
    date_list = urutkan_tanggal()
    if len(date_list) > 5:  # Jika banyak data > 5 maka ditampilkan 5 data terlebih dahulu
        a = 0
        b = 5
        for i in range(a, b):
            print_riwayatambil(i, date_list)
        pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
        # Jika input tidak valid maka dikeluarkan pesan kesalahan
        while (pil != "Y") and (pil != "y") and (pil != "N") and (pil != "n"):
            print("Maaf, input kamu tidak valid, Silakan masukkan kembali")
            pil = input("Tampilkan entry data selanjutnya? (y/n) : ")
        # Input valid
        while (pil == "Y" or pil == "y"):
            a += 5
            b += 5
            if (b > len(date_list)):
                c = len(date_list) % 5
                b -= 5
                for i in range(a, b + c):
                    print_riwayatambil(i, date_list)
                print("Entry data telah habis")
                break
            else:
                for i in range(a, b):
                    print_riwayatambil(i, date_list)
            pil = input("Tampilkan entry data selanjutnya? (y/n) : ")

    elif len(date_list) == 0:  # Jika jumlah datanya 0 maka dikeluarkan tidak ada data
        print("Tidak ada data")

    else:  # Jika jumlah data < 5 maka tampilkan semuanya
        for i in range(len(date_list)):
            print_riwayatambil(i, date_list)


#riwayatambil()
