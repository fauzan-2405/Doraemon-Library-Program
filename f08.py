# Silahkan download/copy dulu read_file_riwayat_peminjaman_gadget yang udah kusediain
from read_file_gadget import data_gadget
from read_file_borrow_history import data_peminjaman_gadget


# !!!! TOLONG DIBACA !!!!
# Ini cuma jadi id_user dan nama sementara, karena nanti di sc utama bakal digantikan sama
# fungsi login yang udah nge provide id_user dan nama user
# aku pake disini biar nanti pas kita nge modify datanya kita udah punya id sama nama usernya (liat line 58)
# jadi 2 line dibawah ini nanti dihapus klo udah mau ke sc utama
# id_user = int(input("Masukkan id: "))
# nama = input("Masukkan nama: ")

def modify_data_gadget(idx, col, value):
    # Fungsi ini digunakan untuk memodify data_gadget karena value jumlahnya berkurang
    data_gadget[idx][col] = value


def is_idpinjam_valid(id_pinjam):
    # Fungsi ini digunakan untuk mengecek apakah id gadget sudah terdaftar atau tidak
    # Jika tidak, valid = False dsb.
    valid = False
    for i in range(len(data_gadget)):
        if data_gadget[i][0] == id_pinjam:
            valid = True
    return valid


def is_jumlahpinjam_valid(z, jumlah_pinjam):
    # Fungsi ini digunakan untuk mengecek apakah jumlah yang dipinjam melebihi stok atau bukan
    # jika lebih dari stok, valid = False dsb.
    valid = False
    for i in range(len(data_gadget)):
        if jumlah_pinjam <= data_gadget[z][3]:
            valid = True
    return valid


def letak_gadget(id_pinjam):
    # Fungsi ini digunakan untuk mencari letak kolom dari gadget
    for i in range(len(data_gadget)):
        if data_gadget[i][0] == id_pinjam:
            idx = i
    return idx


def pinjam(id_user):
    # Fungsi ini digunakan untuk menjalankan prosedur meminjam barang dari Doraemonangis oleh user
    id_pinjam = input("Masukkan ID gadget: ")
    while is_idpinjam_valid(id_pinjam) == False:
        print("ID gadget tidak ditemukan, silahkan masukkan ulang")
        id_pinjam = input("Masukkan ID gadget: ")
    z = letak_gadget(id_pinjam)  # Letak gadget yang akan dipinjam
    print("Stok item", data_gadget[z][1] + ":", data_gadget[z][3])  # Menampilkan stok item gadget yang bersangkutan
    tanggal_pinjam = input("Tanggal peminjaman: ")  # Input selalu valid
    jumlah_pinjam = int(input("Jumlah peminjaman: "))
    while is_jumlahpinjam_valid(z, jumlah_pinjam) == False:
        print("Jumlah gadget yang dipinjam tidak mencukupi, silahkan masukkan ulang")
        jumlah_pinjam = int(input("Jumlah peminjaman: "))
    print("Item", data_gadget[z][1] + "(x" + str(jumlah_pinjam) + ")", "berhasil dipinjam!")

    modify_data_gadget(z, 3,
                       (data_gadget[z][3] - jumlah_pinjam))  # Memodify data_gadget karena jumlah gadget ybs berkurang
    new_data_for_rwyt_peminjaman = [id_user, id_pinjam, tanggal_pinjam, jumlah_pinjam,
                                    (len(data_peminjaman_gadget) + 1),
                                    "FALSE"]  # data baru utk ditambahkan ke riwayat peminjaman
    data_peminjaman_gadget.append(new_data_for_rwyt_peminjaman)