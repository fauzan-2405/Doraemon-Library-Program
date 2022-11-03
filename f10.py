# Silahkan download/copy dulu read_file_riwayat_peminjaman_gadget yang udah kusediain
from read_file_consumable import data_consumable
from read_file_consumable_history import data_pengambilan_consumable

# !!!! TOLONG DIBACA !!!!
# Ini cuma jadi id_user dan nama sementara, karena nanti di sc utama bakal digantikan sama
# fungsi login yang udah nge provide id_user dan nama user
#id_user = int(input("Masukkan id: "))
#nama = input("Masukkan nama: ")


def modify_data_consumable(idx, col, value):
    # Fungsi ini digunakan untuk memodify data_gadget karena value jumlahnya berkurang
    data_consumable[idx][col] = value


def is_idminta_valid(id_minta):
    # Fungsi ini digunakan untuk mengecek apakah id item sudah terdaftar atau tidak
    # Jika tidak, valid = False dsb.
    valid = False
    for i in range(len(data_consumable)):
        if data_consumable[i][0] == id_minta:
            valid = True
    return valid


def is_jumlahminta_valid(z, jumlah_minta):
    # Fungsi ini digunakan untuk mengecek apakah jumlah yang diminta melebihi stok atau bukan
    # jika lebih dari stok, valid = False dsb.
    valid = False
    for i in range(len(data_consumable)):
        if jumlah_minta <= data_consumable[z][3]:
            valid = True
    return valid


def letak_item(id_minta):
    # Fungsi ini digunakan untuk mencari letak kolom dari item
    for i in range(len(data_consumable)):
        if data_consumable[i][0] == id_minta:
            idx = i
    return idx


def minta(id_user):
    # Fungsi ini digunakan untuk menjalankan prosedur meminta item dari Doraemonangis oleh user
    id_minta = input("Masukkan ID item: ")
    while is_idminta_valid(id_minta) == False:
        print("ID item tidak ditemukan, silahkan masukkan ulang")
        id_minta = input("Masukkan ID item: ")
    z = letak_item(id_minta)  # Letak item yang akan dipinjam
    print("Stok item", data_consumable[z][1] + ":", data_consumable[z][3])  # Menampilkan stok item yang bersangkutan
    tanggal_minta = input("Tanggal permintaan: ")  # Input selalu valid
    jumlah_minta = int(input("Jumlah permintaan: "))
    while is_jumlahminta_valid(z, jumlah_minta) == False:
        print("Jumlah item yang diminta tidak mencukupi, silahkan masukkan ulang")
        jumlah_minta = int(input("Jumlah permintaan: "))
    print("Item", data_consumable[z][1] + "(x" + str(jumlah_minta) + ")", "berhasil diambil!")

    modify_data_consumable(z, 3, (
                data_consumable[z][3] - jumlah_minta))  # Memodify data_gadget karena jumlah gadget ybs berkurang
    new_data_for_rwyt_permintaan = [len(data_pengambilan_consumable) + 1, id_user, id_minta, tanggal_minta,
                                    jumlah_minta]  # data baru utk ditambahkan ke riwayat
    # Data ini berupa [id, id user, id item, tanggal minta, jumlah minta]
    data_pengambilan_consumable.append(new_data_for_rwyt_permintaan)


#minta()