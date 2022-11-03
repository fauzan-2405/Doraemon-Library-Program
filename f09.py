from read_file_return_history import data_pengembalian_gadget
from read_file_borrow_history import data_peminjaman_gadget
from read_file_gadget import data_gadget

def modify_data_gadget(idx,value):
    # Fungsi ini digunakan untuk memodify data_gadget karena value jumlahnya berkurang
    data_gadget[idx][3] = value

def letak_gadget(id_pinjam):
    # Fungsi ini digunakan untuk mencari letak kolom dari gadget
    idx = 0
    for i in range (len(data_gadget)):
        if data_gadget[i][0] == id_pinjam :
            idx = i
    return idx

def sedang_dipinjam(id_user):
    #fungsi ini mengumpulkan data peminjaman gadget sesuai user
    on_hand = []
    for i in range (len(data_peminjaman_gadget)):
        if data_peminjaman_gadget[i][0] == id_user:
            on_hand.append(data_peminjaman_gadget[i])
    return on_hand

def kembali(id_user):
    dipinjam = sedang_dipinjam(id_user)
    #mencetak daftar gadget yang sedang dipinjam user
    for i in range (len(dipinjam)):
        gadget = letak_gadget(dipinjam[i][1])
        print('\n' + str(i+1) + ".", str(data_gadget[gadget][1]))
    mau_kembali = int(input('\n'+"Masukkan nomor peminjaman: ")) - 1
    #cek validitas input
    if mau_kembali > (len(dipinjam) - 1):
        while mau_kembali > (len(dipinjam) - 1):
          mau_kembali = int(input("Tolong masukkan nomor peminjaman dari daftar yang telah ditampilkan: ")) - 1
    tanggal_kembali = input("Tanggal pengembalian: ")
    indx_gad = letak_gadget(dipinjam[mau_kembali][2])
    print('\n' + "Item", str(data_gadget[indx_gad][1]), "(x" + str(dipinjam[mau_kembali][3]) + ") telah dikembalikan")
    id_pengembalian = len(data_pengembalian_gadget) + 1
    modify_data_gadget(indx_gad, (data_gadget[indx_gad][3] + dipinjam[mau_kembali][3]))
    entry_pengembalian = [id_pengembalian, dipinjam[mau_kembali][4], tanggal_kembali]
    data_pengembalian_gadget.append(entry_pengembalian)
    indx_peminjaman = dipinjam[mau_kembali][4] - 1
    data_peminjaman_gadget[indx_peminjaman][5] = True

#id_user nanti memakai data dari login saja saat di fungsi utama
#id_user = int(input("Masukkan ID user: "))
#kembali()