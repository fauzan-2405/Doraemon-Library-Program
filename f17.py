import sys
from f15 import save

def keluar():
    print("Apakah kamu yakin tidak ingin mengacak-acak kantong",end =" ")
    print("ajaib Doaremonangis lagi?")
    pil = input("(y/n) : ")
    while (pil != "Y") and (pil != "y") and (pil != "N") and (pil != "n"):
        print("Maaf, input kamu tidak valid, Silakan masukkan kembali")
        pil = input("(y/n) : ")
    
    if (pil == "Y") or (pil == "y"):
      # Disini bakal digantiin sama fungsi save yg bakal dibuat
        save()
        print("Sampai Jumpa!")
        sys.exit(0)
        
    else :
      # Disini bakal digantiin sama fungsi balik ke menu utama
        print("#Prosedure back to menu utama dijalankan...")
 
#keluar()
