from read_file_user import data_user
def run():
    global data_user
    found=False
    matched=False
    while not found or not matched :
        username=input("Masukan username: ")
        password=input("Masukkan pass: ")
        id_user=""
        role_user=""
        for data in data_user:
            if username in data:
                found=True
                if password==data[4]:
                    matched=True
                    id_user=data[0]
                    role_user=data[5]
        #print(found,matched)
        if found and matched:
            print("Halo "+username+"! Selamat datang di Kantong Ajaib.")
            return id_user,role_user
        elif not found or not matched:
            print("Maaf username atau password anda salah")