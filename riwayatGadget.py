import validasi, variabelGlobal
from datetime import datetime

def cetakRiwayatPinjam(count,sortedriwayat,panjang): # fungsi untuk mencetak riwayat pengambilan
    if panjang > 6 : # mengecek panjang list yang belum dicetak
        for i in range(count,count + 6): # prosedur percetakan
            print("\nID Pengambilan          :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4],"\n")
            if sortedriwayat[i][5] == 'n':
                print("Apa sudah dikembalikan semua : Belum")
            else:
                print("Apa sudah dikembalikan semua : Sudah")
        count += 6 # menambah jumlah data yang telah dicetak
        pil = input("\nApakah Anda ingin melihat data riwayat lainnya?(y/n)")
        if pil == "y" :
            return cetakRiwayatPinjam(count,sortedriwayat,panjang-6) # mengembalikan pada fungsi cetak riwayat dan mengurangi panjang list yang belum dicetak 
        else :
            return
    elif panjang == 0: # tidak terdapat data pada file consumable_history
        print("Tidak terdapat data riwayat peminjaman.")
        return
    else : # panjang data <= 6
        for i in range(count,len(sortedriwayat)): # prosedur percetakan
            print("\nID Pengambilan          :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4],"\n")
            if sortedriwayat[i][5] == 'y':
                print("Apa sudah dikembalikan semua : Belum")
            else:
                print("Apa sudah dikembalikan semua : Sudah")
        return

def cetakRiwayatKembali(count,sortedriwayat,panjang): # fungsi untuk mencetak riwayat pengambilan
    if panjang > 5 : # mengecek panjang list yang belum dicetak
        for i in range(count,count + 5): # prosedur percetakan
            print("\nID Pengambilan          :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4],"\n")
        count += 5 # menambah jumlah data yang telah dicetak
        pil = input("\nApakah Anda ingin melihat data riwayat lainnya?(y/n)")
        if pil == "y" :
            return cetakRiwayatKembali(count,sortedriwayat,panjang-5) # mengembalikan pada fungsi cetak riwayat dan mengurangi panjang list yang belum dicetak 
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
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.consumable['data'][k][1])
                    break
            print("Tanggal Pengambilan     :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4],"\n")
        return