import argparse, sys, os, time, variabelGlobal, dashboard, validasi, user
#Mengambil argumen yang diberikan melalui CLI
parser = argparse.ArgumentParser()
parser.add_argument("namaFolder")
args = parser.parse_args()
folderDir = args.namaFolder

os.chdir('saves')
if not os.path.isdir(folderDir) :
    print('Nama folder tidak valid')
    sys.exit()

#PROSEDUR UNTUK LOAD DATA
variabelGlobal.Load(folderDir)
print("Loading..")
time.sleep(2)
print("\nSelamat datang di \"Kantong Ajaib!\"")
while True:
    inUser = input("\n>>> ")
    if inUser == 'help': 
        print("\n======= HELP =======") # dengan asumsi help hanya berisi login dan exit
        print(" login - login ke sistem kantong ajaib")
        print(" exit - keluar dari sistem kantong ajaib")
    elif inUser == 'login':
        break
    elif inUser == 'exit':
        sys.exit()
    else:
        print(" inputan tidak ada pada pilihan, coba ketik help untuk melhat list help")
#WAJIB LOGIN TERLEBIH DAHULU
while True: # Akan terus mengulang sampe username dan password yang dimasukkan sesuai
    print("\n======= Login =======")
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    if validasi.isCredentialValid(username,password):
            print('Halo {}!, Selamat datang di Kantong Ajaib.'.format(username))
            role = user.checkRole(username)
            break
    print("Username atau password mungkin salah")
    
variabelGlobal.username = username
variabelGlobal.role = role
#Ketika berhasil login, username pengguna disimpan di variabel 'username' dan id pengguna yang bersangkutan
#disimpan di variabel 'id_user' (dideklarasi di dalam fungsi isCredentialValid)
dashboard.Show(role)

