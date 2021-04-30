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
        username, role = user.login()
        break
    elif inUser == 'exit':
        sys.exit()
    else:
        print(" inputan tidak ada pada pilihan, coba ketik \"help\" untuk melhat list help")
    
variabelGlobal.username = username
variabelGlobal.role = role
#Ketika berhasil login, username pengguna disimpan di variabel 'username' dan id pengguna yang bersangkutan
#disimpan di variabel 'id_user' (dideklarasi di dalam fungsi isCredentialValid)
dashboard.Show(role)
