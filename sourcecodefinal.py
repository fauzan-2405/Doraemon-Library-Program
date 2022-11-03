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
import f15
import f16
import f17
# Login dan register
print("=========================================")
print("SELAMAT DATANG DI KANTONG DORAEMONANGIS")
id_user,role_user= f02.run()
if role_user=="admin":
    while True:
        command = input("Silahkan masukkan command. Ketik help untuk melihat command yang dapat digunakan. \n ")
        if command == "raritySearch":
            f03_f04.RaritySearch()
        elif command == "register":
            f01.run()
        elif command == "yearSearch":
            f03_f04.YearSearch()
        elif command == "help":
            f16.help()
        elif command == "tambahItem":
            f05.tambah_item()
        elif command == "hapusItem":
            f06.hapus_item()
        elif command == "ubahJml":
            f07.ubah_item()
        elif command == "riwayatpinjam":
            f11.riwayatpinjam()
        elif command == "riwayatkembali":
            f12.riwayatpengembalian()
        elif command == "riwayatambil":
            f13.riwayatambil()
        elif command=="save":
            f15.save()
        elif command=="exit":
            f17.keluar()
        else :
            print("Command Salah. ")
else:
    while True:
        command = input("Silahkan masukkan command. Ketik help untuk melihat command yang dapat digunakan. \n ")
        if command == "raritySearch":
            f03_f04.RaritySearch()
        elif command == "register":
            f01.run()
        elif command == "yearSearch":
            f03_f04.YearSearch()
        elif command == "help":
            f16.help()
        elif command == "meminjam":
            f08.pinjam(id_user)
        elif command == "mengembalikan":
            f09.kembali(id_user)
        elif command == "meminta":
            f10.minta(id_user)
        elif command=="save":
            f15.save()
        elif command=="exit":
            f17.keluar()
        else:
            print("Command salah. ")



