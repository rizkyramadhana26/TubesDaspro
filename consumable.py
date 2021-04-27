import validasi, variabelGlobal
from datetime import datetime

def datalogin(username): # prosedur untuk menyimpan data user menjadi sebuah array
    datasLogin = []
    for i in range(len(variabelGlobal.user['data'])):
        if variabelGlobal.user['data'][i][2] == username :
            datasLogin.append(variabelGlobal.user['data'][i])
    return datasLogin

def minta(): # fungsi minta item consumable
    idx = input("Masukan ID item        : ")
    return checkIDconsum(idx) # melanjutkan ke fungsi cek ID item

def checkIDconsum(idx): # fungsi cek id item
    if (idx[0] != "C"): # mengecek kevalidan id item
        print("\nMasukan ID item consumable tidak valid!")
        pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
        if pil == "y" :
            return minta() # mengembalikan pada fungsi minta item
        else:
            return 
    else: # mengecek ada tidaknya item pada data
        N = len(variabelGlobal.consumable['data'])
        i = 0
        while (i < N):
            if (variabelGlobal.consumable['data'][i][0] == idx):
                if (variabelGlobal.consumable['data'][i][3] == 0): # mengecek ketersediaan item
                    print("\nMaaf, jumlah item yang diminta kosong.")
                    pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
                    if pil == "y" :
                        return minta() # mengembalikan pada fungsi minta item
                    else:
                        return 
                else: # jumlah item != 0
                    return masukanconsum(idx,i) # melanjutkan pada fungsi untuk mengisi masukan
            else:
                i += 1
        if (i == N): # item yang dicari tidak ditemukan pada data consumab
            print("\nMaaf, item yang diminta tidak tersedia.")
            pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
            if pil == "y" :
                return minta() # mengembalikan pada fungsi minta item
            else:
                return 

def masukanconsum(idx,i): # fungsi untuk menerima masukan jumlah dan tanggal
    datasLogin = datalogin(variabelGlobal.username) # menyimpan data user pada array
    amount = int(input("Jumlah                 : ")) 
    if (amount <= 0): # mengecek valid tidaknya masukan jumlah (jumlah <= 0)
        print("\nMaaf, jumlah item yang dimasukkan tidak valid.")
        pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
        if pil == "y" :
            return minta() # mengembalikan pada fungsi minta item
        else:
            return 
    else: # jumlah valid (jumlah > 0)
        if (amount > int(variabelGlobal.consumable['data'][i][3])): # jumlah yang diminta melebihi jumlah consumables
            print("\nMaaf, jumlah item yang tersisa hanya {}.".format(variabelGlobal.consumable['data'][i][3]))
            pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
            if pil == "y" : 
                return minta() # mengembalikan pada fungsi minta item
            else:
                return 
        else: # masukan jumlah telah valid dan tidak melebihi consumables yang tersedia
            date = input("Tanggal permintaan     : ")
            if not(isTanggalValid(date)): # validasi input tanggal
                print("\nMaaf, masukan tanggal Anda tidak valid.")
                pil = input("Apa ingin mengulangi prosedur minta item?(y/n)")
                if pil == "y" :
                    return minta() # mengembalikan pada fungsi minta item
                else:
                    return 
            else: # semua input telah valid
                variabelGlobal.consumable['data'][i][3] = str(int(variabelGlobal.consumable['data'][i][3]) - amount)  # mengurangi jumlah item yang diminta
                idpengambil = datasLogin[0][0] # mengambil id user dari array datasLogin
                idconsm = idx # mengambil id item dari input
                print("\nItem {}".format(variabelGlobal.consumable['data'][i][1]),"(x{}) telah berhasil diambil!".format(amount))
                if variabelGlobal.consumable_history['data'] == [] : 
                    newData = [1,idpengambil,idconsm,date,amount]
                    variabelGlobal.consumable_history['data'].append(newData) # mencatat data pada consumable_history
                    return
                else :
                    idMinta = int(variabelGlobal.consumable_history['data'][-1][0]) + 1
                    newData = [idMinta,idpengambil,idconsm,date,amount]
                    variabelGlobal.consumable_history['data'].append(newData) # mencatat data pada consumable_history
                    return

def riwayatambil(): # fungsi riwayat ambil
    sortedriwayat = sorted(variabelGlobal.consumable_history['data'], key = lambda row: datetime.strptime(row[3], "%d/%m/%Y"), reverse = True) # menyimpan data consumbale_history yang telah diurutkan berdasarkan tahun pada list
    count = 0 # banyak data yang telah dicetak
    panjang = len(sortedriwayat)
    cetakRiwayat(count,sortedriwayat,panjang) # melanjutkan pada fungsi cetak riwayat

def cetakRiwayat(count,sortedriwayat,panjang): # fungsi untuk mencetak riwayat pengambilan
    if panjang > 5 : # mengecek panjang list yang belum dicetak
        for i in range(count,count + 5): # prosedur percetakan
            print("\nID Pengambilan          :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.consumable['data'])):
                if sortedriwayat[i][2] == variabelGlobal.consumable['data'][k][0]:
                    print("Nama Consumable         :", variabelGlobal.consumable['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4])
        count += 5 # menambah jumlah data yang telah dicetak
        pil = input("\nApakah Anda ingin melihat data riwayat lainnya?(y/n)")
        if pil == "y" :
            return cetakRiwayat(count,sortedriwayat,panjang-5) # mengembalikan pada fungsi cetak riwayat dan mengurangi panjang list yang belum dicetak 
        else :
            return
    elif panjang == 0: # tidak terdapat data pada file consumable_history
        print("Tidak terdapat data riwayat pengambilan.")
        return
    else : # panjang data <= 5
        for i in range(count,len(sortedriwayat)): # prosedur percetakan
            print("\nID Pengambilan          :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.consumable['data'])):
                if sortedriwayat[i][2] == variabelGlobal.consumable['data'][k][0]:
                    print("Nama Consumable         :", variabelGlobal.consumable['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4])
        return
