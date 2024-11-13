import os 
import termcolor 
import tabulate as tb 
import pandas as pd 
import csv

def clear():
    os.system("cls")
    
def garis(a):
    print (a*107)

def cover ():
    garis("=")
    print ("""
██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║█████╗  ███████║██║     ██║   ███████║       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║       ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║       ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""")
    garis("=")

def enter (): 
    enter = input ("tekan [ENTER] untuk melanjutkan >> ") 

def halaman_awal (): 
    clear() 
    cover () 
    print ("""
                                            1. REGISTRASI
                                            2. LOGIN SEBAGAI USER
                                            3. LOGIN SEBAGAI TENAGA KESEHATAN
                                            4. LOGIN SEBAGAI ADMIN
                                            5. EXIT 
""") 
    garis("=") 
    while True : 
        try : 
            pilih = int (input ("Pilih Opsi yang tersrdia >> ")) 
            if pilih == 1 : 
                enter() 
                registrasi() 
                break 
            elif pilih == 2 : 
                enter() 
                login_user () 
                break
            elif pilih == 3 :
                enter()
                login_tenaga_kesehatan()
                break
            elif pilih == 4 :
                login_admin()
                break
            elif pilih == 5 :
                exit()
                break
            else : 
                print ("Opsi yang anda pilih tidak tersedia") 
        except ValueError : 
            termcolor.cprint ("masukkan input dalam bentuk angka", "red") 
            enter() 
            halaman_awal () 
            


def registrasi (): 
    clear() 
    cover() 
    user,no_telp,jenis_kelamin,umur,list_username,list_password = penampung_user()

    while True : 
        nama = input ("masukkan nama lengkap anda >> ") 
        nomorhp = int (input ("Masukkan nomor HP >> "))
        jenis_kelamin = input ("Masukkan jenis kelamin (laki-laki/perempuan)>> ") 
        usia = input ("masukkan usia >> ") 
        while True : 
            try : 
                username = input ("buat username baru >> ") 
                if username in list_username: 
                    raise ValueError ("Username sudah digunakan") 
                else : 
                    break 
            except ValueError as erorr:  
                termcolor.cprint (erorr, "red") 
        while True : 
            try : 
                password = input ("buat password baru >> ")
                if password == username or len(password) < 8 : 
                    raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 

        while True : 
            try : 
                password2 = input ("konfirmasi password anda >> ") 
                if password2 != password : 
                    raise  ValueError ("password yang anda masukkan tidak sama") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 
        garis("=") 
        with open ("data_login/datauser.csv", mode = "a", newline = "\n") as file : 
            border = ["nama lengkap", "nomor hp","jenis kelamin", "usia", "username", "password"] 
            writer = csv.DictWriter (file, fieldnames=border) 
            writer.writerow ( {"nama lengkap" : nama, "nomor hp" :  nomorhp,"jenis kelamin" : jenis_kelamin,"usia" : usia, "username" : username, "password" : password2} ) 
        termcolor.cprint ("registrasi berhasil, silahkan login", "green") 
        enter()
        halaman_awal() 
        
def login_user ():
    percobaan = 0
    while True:
        clear () 
        cover ()
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red") 
            enter()
            halaman_awal()
            break
        else:
            user,no_telp,jenis_kelamin,umur,list_username,list_password = penampung_user() 
            username = input ("masukkan username anda >> ") 
            password = input ("masukkan password anda >> ") 
            garis("=")
            indikator = 0 
            for i in range (len(list_username)): 
                if username in list_username[i] and password in list_password[i] : 
                    indikator += 1 
            if indikator == 1 :  
                termcolor.cprint ("login berhasil", "green") 
                enter() 
                menu_user() 
            else : 
                termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                percobaan +=1
                enter () 
                continue

def login_tenaga_kesehatan():
    percobaan = 0
    while True:
        clear()
        cover()
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            halaman_awal()
            break
        else : 
            
            username = input ("masukkan username anda >> ")
            password = input ("masukkan password anda >> ")
            garis("=")
            tenkes, profesi_tenkes, usertenkes, passtenkes = penampung_tenkes()
            for i in range(len(usertenkes)):
                if username == usertenkes[i] and password == passtenkes[i]:
                    termcolor.cprint("LOGIN BERHASIL", "green")
                    enter()
                    menu_tenkes()
                    break
                else :
                    termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                    percobaan +=1
                    enter () 
                    continue


def login_admin():
    percobaan = 0
    while True:
        clear()
        cover()
        useradmin = []
        passadmin = []
        with open("data_login/dataadmin.csv", mode="r") as file:
            reader = csv.reader(file,delimiter=",")
            for i in reader:
                useradmin.append(i[0])
                passadmin.append(i[1])
        if percobaan > 3 :
            termcolor.cprint("anda telah mencoba 3 kali, silahkan tunggu beberapa saat untuk mencoba lagi","red")
            enter()
            halaman_awal()
            break
        else : 
            username = input ("masukkan username >> ")
            password = input ("masukkan password >> ")
            garis("=")
            for i in range(len(useradmin)):
                if username == useradmin[i] and password == passadmin[i] :
                    termcolor.cprint("LOGIN BERHASIL", "green")
                    enter()
                    menu_admin()
                    break
                else :
                    termcolor.cprint ("login tidak berhasil, silahkan masukkan username dan password yang benar", "red") 
                    percobaan +=1
                    enter () 
                    continue

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> USER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def penampung_user ():
    user = []
    no_telp = []
    jenis_kelamin = []
    umur = []
    list_username = [] 
    list_password = [] 
    with open ("data_login/datauser.csv", mode = "r") as file : 
        csv_reader = csv.reader(file) 
        for i in csv_reader:  
            user.append(i[0])  
            no_telp.append(i[1])  
            jenis_kelamin.append(i[2])  
            umur.append(i[3])  
            list_username.append(i[4])  
            list_password.append (i[5])
    return user,no_telp,jenis_kelamin,umur,list_username,list_password   

def menu_user():
    pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TENAGA KESEHATAN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def penampung_tenkes():
    tenkes = []
    profesi_tenkes = []
    usertenkes = []
    passtenkes = []
    with open ("data_login/datatenkes.csv", mode = "r") as file:
        reader =csv.reader(file, delimiter=",")
        for i in reader:
            tenkes.append(i[0])
            profesi_tenkes.append(i[1])
            usertenkes.append(i[2])
            passtenkes.append(i[3])
    return tenkes, profesi_tenkes, usertenkes, passtenkes
def menu_tenkes():
    pass
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ADMIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def menu_admin():
    while True :
        clear()
        cover()
        print ("""
                                        1. CEK USER
                                        2. CEK TENAGA KESEHATAN
                                        3. TAMBAH USER 
                                        4. TAMBAH TENAGA KESEHATAN 
                                        5. HAPUS USER
                                        6. HAPUS TENAGA KESEHATAN
""")
        garis("=")
        try :
            pilih = int (input("masukkan pilihan >> "))
            if pilih == 1 :
                enter()
                cek_user()
                break
            elif pilih == 2 :
                enter()
                cek_tenkes()
                break
            elif pilih == 3 :
                enter()
                tambah_user()
                break
            elif pilih == 4 :
                enter()
                tambah_tenkes()
                break
            elif pilih == 5 :
                enter()
                hapus_user()
                break
            elif pilih == 6 :
                enter()
                hapus_tenkes()
                break
            else : 
                raise ValueError ("inputan tidak valid")
        except ValueError as error :
            termcolor.cprint (f"opsi tidak tersedia {error}", "red")
            enter()
            continue

def cek_user():
    clear()
    cover()
    user,no_telp,jenis_kelamin,umur,list_username,list_password = penampung_user()
    print ("\n")
    if len(user) == 0 :
        print ("USER TIDAK TERSEDIA\n\n".center(107))
        garis("=")
    else :
        print ("USER INFO\n\n".center(107))
        border = ["NO","NAMA", "TELEPON", "JENIS KELAMIN", "UMUR", "USERNAME", "PASSWORD"]
        garis("=")
        print (f"|{border[0]:^3}|{border[1]:^20}|{border[2]:^15}|{border[3]:^15}|{border[4]:^7}|{border[5]:^20}|{border[6]:^20}|")
        garis("=")
        for i in range (len(user)):
            print (f"|{i+1:^3}|{user[i]:^20}|{no_telp[i]:^15}|{jenis_kelamin[i]:^15}|{umur[i]:^7}|{list_username[i]:^20}|{list_password[i]:^20}|")
            garis("=")
        garis("=")
        enter()
        menu_admin()

def cek_tenkes():
    clear()
    cover()
    tenkes, profesi_tenkes, usertenkes, passtenkes = penampung_tenkes()
    print ("\n")
    if len(tenkes) == 0 :
        print ("TENAGA KESEHATAN TIDAK TERSEDIA\n\n".center(107))
        garis("=")
    else :
        print ("TENAGA KESEHATAN\n\n".center(107))
        garis("=")
        border = ["NO","NAMA", "PROFESI", "USERNAME", "PASSWORD"]
        print (f"|{border[0]:^10}|{border[1]:^25}|{border[2]:^25}|{border[3]:^20}|{border[4]:^20}|")
        garis("=")
        for i in range (len(tenkes)):
            print (f"|{i+1:^10}|{tenkes[i]:^25}|{profesi_tenkes[i]:^25}|{usertenkes[i]:^20}|{passtenkes[i]:^20}|")
            garis("=")
        garis("=")
        enter()
        menu_admin()

def tambah_user():
    clear()
    cover()
    user,no_telp,jenis_kelamin,umur,list_username,list_password = penampung_user()

    while True : 
        nama = input ("masukkan nama lengkap user >> ") 
        nomorhp = int (input ("Masukkan nomor HP user >> "))
        jenis_kelamin = input ("Masukkan jenis kelamin user (laki-laki/perempuan)>> ") 
        usia = input ("masukkan usia user >> ") 
        while True : 
            try : 
                username = input ("buat username baru user >> ") 
                if username in list_username: 
                    raise ValueError ("Username sudah digunakan") 
                else : 
                    break 
            except ValueError as erorr:  
                termcolor.cprint (erorr, "red") 
        while True : 
            try : 
                password = input ("buat password baru user >> ")
                if password == username or len(password) < 8 : 
                    raise ValueError ("Password harus lebih dari 8 karakter dan tidak sama dengan username") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 

        while True : 
            try : 
                password2 = input ("konfirmasi password anda >> ") 
                if password2 != password : 
                    raise  ValueError ("password yang anda masukkan tidak sama") 
                else : 
                    break 
            except ValueError as error: 
                termcolor.cprint (error, "red") 
        garis("=") 
        with open ("data_login/datauser.csv", mode = "a", newline = "\n") as file : 
            border = ["nama lengkap", "nomor hp","jenis kelamin", "usia", "username", "password"] 
            writer = csv.DictWriter (file, fieldnames=border) 
            writer.writerow ( {"nama lengkap" : nama, "nomor hp" :  nomorhp,"jenis kelamin" : jenis_kelamin,"usia" : usia, "username" : username, "password" : password2} ) 
        termcolor.cprint ("registrasi berhasil, silahkan login", "green") 
        enter()
        menu_admin() 


def tambah_tenkes():
    clear()
    cover()
    nama = input("masukkan nama beserta gelar tenaga kesehatan >> ")
    profesi = input("masukkan profesi yang dari tenaga kesehatan >> ")
    user_tenaga_kesehatan = input ("buat username tenaga kesehatan >> ")
    password_tenaga_kesehatan = input ("buat password tenaga kesehatan >> ") #kurang try except
    garis("=")
    with open("data_login/datatenkes.csv", mode="a", newline="\n") as file:
        border = ["nama","profesi","username", "password"]
        writer = csv.DictWriter(file,fieldnames=border)
        writer.writerow({"nama" : nama,"profesi" : profesi,"username" : user_tenaga_kesehatan, "password" : password_tenaga_kesehatan})
    termcolor.cprint ("tenaga kesehatan berhasil ditambahkan", "green")
    enter()
    menu_admin()
def hapus_user():
    clear()
    cover()
    user,no_telp,jenis_kelamin,umur,list_username,list_password = penampung_user()
    border = ["NO","NAMA", "TELEPON", "JENIS KELAMIN", "UMUR", "USERNAME", "PASSWORD"]
    garis("=")
    print (f"|{border[0]:^3}|{border[1]:^20}|{border[2]:^15}|{border[3]:^15}|{border[4]:^7}|{border[5]:^20}|{border[6]:^20}|")
    garis("=")
    for i in range (len(user)):
        print (f"|{i+1:^3}|{user[i]:^20}|{no_telp[i]:^15}|{jenis_kelamin[i]:^15}|{umur[i]:^7}|{list_username[i]:^20}|{list_password[i]:^20}|")
        garis("=")
    garis("=")
    pilih = int(input("masukkan user yang ingin di hapus >> "))
    user.pop(pilih - 1)
    no_telp.pop(pilih - 1)
    jenis_kelamin.pop(pilih - 1)
    umur.pop(pilih - 1)
    list_username.pop(pilih - 1)
    list_password.pop(pilih - 1)
    with open("data_login/datauser.csv", mode="w", newline="\n") as file:
        writer = csv.writer(file)
        for i in range (len(user)):
            writer.writerow(user[i],no_telp[i],jenis_kelamin[i],umur[i],list_username[i],list_username[i])
    termcolor.cprint("user berhasil di hapus", "green")
    enter ()
    menu_admin()


def hapus_tenkes():
    clear()
    cover()
    tenkes, profesi_tenkes, usertenkes, passtenkes = penampung_tenkes()
    garis("=")
    border = ["NO","NAMA", "PROFESI", "USERNAME", "PASSWORD"]
    print (f"|{border[0]:^10}|{border[1]:^25}|{border[2]:^25}|{border[3]:^20}|{border[4]:^20}|")
    garis("=")
    for i in range (len(tenkes)):
        print (f"|{i+1:^10}|{tenkes[i]:^25}|{profesi_tenkes[i]:^25}|{usertenkes[i]:^20}|{passtenkes[i]:^20}|")
        garis("=")
    garis("=")
    hapus = int (input ("masukkan no tenkes yang ingin dihapus >> "))
    tenkes.pop(hapus-1)
    profesi_tenkes.pop(hapus-1)
    usertenkes.pop(hapus-1)
    passtenkes.pop(hapus-1)
    with open ("data_login/datatenkes.csv", mode = "w", newline = "\n") as file:
        writer = csv.writer(file)
        for i in range (len(tenkes)):
            writer.writerow(tenkes[i], profesi_tenkes[i], usertenkes[i], passtenkes[i])
    termcolor.cprint("berhasil menghapus tenaga kesehatan", "green")
    enter()
    menu_admin()

    
if __name__=="__main__":
    # halaman_awal()
    menu_admin()
    # menu_tenkes()
    # menu_user()
    # cek_user()
    # cek_tenkes()