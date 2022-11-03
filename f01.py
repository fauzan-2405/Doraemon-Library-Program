from read_file_user import data_user
def run():
    datas = []
    datas = data_user
    found=False
    username=input("Masukan username: ")
    nama=input("Masukkan nama: ")
    alamat=input("Masukkan alamat: ")
    password=input("Masukkan password: ")
    for data in data_user:
        if username in data:
            found=True
    #print(found,matched)
    if found:
        print("Anda sudah terdaftar")
    elif not found:
        new_user=[str(int(data_user[-1][0])+1),username, nama, alamat, password, "user"]
        data_user.append(new_user)
        print("Register anda berhasil")
