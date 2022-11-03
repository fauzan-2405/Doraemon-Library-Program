#mengimport data gadget yang sudah jadi
from read_file_gadget import data_gadget

def print_gad_det (gadget):
 #Prosedur untuk mencetak detail gagdet
    print("Nama:", gadget[1])
    print("Deskripsi:", gadget[2])
    print("Jumlah:", gadget[3])
    print("Rarity:", gadget[4])
    print("Tahun ditemukan:", gadget[5])
    print("\n")

def RaritySearch ():
 #Prosedur untuk mencari gagdet berdasarkan Rarity
    rarity = str(input("Masukkan rarity: "))
    for i in range (len(data_gadget)):    
        if (data_gadget[i][4] == rarity):#mengecek apakah rarity gadget seusai yg diminta 
            print_gad_det(data_gadget[i])

def YearSearch ():
    year = int(input("Masukkan tahun: "))
    categ = str(input("Masukkan kategori: "))
    if (categ == '>'):
        for i in range (len(data_gadget)):
            if (data_gadget[i][5] > year):
                print_gad_det(data_gadget[i])
    elif (categ == '>='):
        for i in range (len(data_gadget)):
            if (data_gadget[i][5] >= year):
                print_gad_det(data_gadget[i])
    elif (categ == '='):
        for i in range (len(data_gadget)):
            if (data_gadget[i][5] == year):
                print_gad_det(data_gadget[i])
    elif (categ == '<'):
        for i in range (len(data_gadget)):
            if (data_gadget[i][5] < year):
                print_gad_det(data_gadget[i])
    elif (categ == '<='):
        for i in range (len(data_gadget)):
            if (data_gadget[i][5] <= year):
                print_gad_det(data_gadget[i])

#RaritySearch()
#YearSearch()