import f14
import f01
import f02
import f03_f04
import f05
import f06
import f07
import f08
import f09
import f10
import f11
import f12
import f13
import f14
import f15
import f16
import f17
import math
import time
import datetime

# Mengimport file utility
from read_file_user import data_user
from read_file_gadget import data_gadget
from read_file_consumable import data_consumable
from read_file_borrow_history import data_peminjaman_gadget
from read_file_return_history import data_pengembalian_gadget

# Login dan register
print("=========================================")
print("SELAMAT DATANG DI KANTONG DORAEMONANGIS")
id_user = ""

while True:
    masuk = int(
        input(
            "Silahkan Masukkan angka (1) untuk Login dan Jika belum terdaftar masukkan angka (2) untuk register dan (3) untuk help \n "
        ))
    if masuk == 1:
        id_user = f02.run()
        print()
        break
    elif masuk == 2:
        f01.run()
    elif masuk == 3:
        f16.help()
    else:
        print("Angka yang anda pilih salah")

# Mencari gadget
while True:
    command = input(
        "Silahkan mencari gadget yang anda inginkan ketik (carirarity) untuk mencari gadget berdasarkan rarity,(caritahun) untuk mencari gadget berdasarkan tahun,atau next untuk pilihan lainnya. \n "
    )
    if command == "carirarity":
        f03_f04.RaritySearch()
    elif command == "caritahun":
        f03_f04.YearSearch()
    elif command == "next":
        break
    else:
        print("Input yang anda masukkan salah")

# Menambah, Menghapus, dan Mengubah jumlah Gadget
while True:
    command = input(
        "Anda disini dapat menambah, menghapus, dan mengubah jumlah gadget. \n "
    )
    if command == "menambah":
        f05.tambah_item()
    elif command == "menghapus":
        f06.hapus_item()
    elif command == "mengubah":
        f07.ubah_item()
    elif command == "next":
        break
    else:
        print("Input yang anda masukkan salah")

# Meminjam dan Mengambalikan Gadget
while True:
    command = input(
        "Setelah mencari gadget, Anda juga bisa meminjam Gadget atau Mengembalikannya. \n "
    )
    if command == "meminjam":
        f08.pinjam(id_user)
    elif command == "mengembalikan":
        f09.kembali(id_user)
    elif command == "next":
        break
    else:
        print("Input yang anda masukkan salah")

# Meminta consumable
while True:
    command = input(
        "Anda juga dapat meminta consumable dengan cara mengetik meminta")
    if command == "meminta":
        f10.minta(id_user)
    elif command == "next":
        break
    else:
        print("Input yang anda masukkan salah")

# Melihat riwayat peminjaman dan pengembalian gadget
while True:
    command = input(
        "Untuk melihat riwayat peminjaman dan pengembalian gadget,ketik riwayat pinjam atau riwayat kembali \n "
    )
    if command == "riwayat pinjam":
        f11.riwayatpinjam()
    elif command == "riwayat kembali":
        f12.riwayatpengembalian()
    elif command == "next":
        break
    else:
        print("Input yang anda masukkan salah")

#Sebelum keluar file di save dulu
while True :
    command = input("Sebelum keluar file di save dulu \n ")
  if command == "save":
      f15.saveFile()
  else:
      print("Input yang anda masukkan salah")

# Setelah semuanya selesai bisa keluar
while True:
    command = input("Setelah semuanya selesai anda bisa keluar \n ")
    if command == "keluar":
        f17.keluar()
    else:
        print("Input yang anda masukkan salah")
