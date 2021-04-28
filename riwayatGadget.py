import validasi, variabelGlobal
from datetime import datetime

def cetakRiwayatPinjam(count,sortedriwayat,panjang): # fungsi untuk mencetak riwayat pengambilan
    if panjang > 1 : # mengecek panjang list yang belum dicetak
        for i in range(count,count + 1): # prosedur percetakan
            print("\nID Peminjaman           :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Peminjaman      :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4])
        count += 1 # menambah jumlah data yang telah dicetak
        pil = input("\nApakah Anda ingin melihat data riwayat lainnya?(y/n)")
        if pil == "y" :
            return cetakRiwayatPinjam(count,sortedriwayat,panjang-1) # mengembalikan pada fungsi cetak riwayat dan mengurangi panjang list yang belum dicetak 
        else :
            return
    elif panjang == 0: # tidak terdapat data pada file consumable_history
        print("Tidak terdapat data riwayat peminjaman.")
        return
    else : # panjang data <= 1
        for i in range(count,len(sortedriwayat)): # prosedur percetakan
            print("\nID Peminjaman           :", sortedriwayat[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayat[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayat[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Peminjaman      :", sortedriwayat[i][3])
            print("Jumlah                  :", sortedriwayat[i][4])
        return

def cetakRiwayatKembali(count,sortedriwayatPinjam,sortedriwayatKembali,panjang): # fungsi untuk mencetak riwayat pengambilan
    if panjang > 1 : # mengecek panjang list yang belum dicetak
        for i in range(count,count + 1): # prosedur percetakan
            print("\nID Pengembalian         :", sortedriwayatKembali[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayatKembali[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayatKembali[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.gadget['data'][k][1])
                    break
            print("Tanggal Pengembalian    :", sortedriwayatKembali[i][2])
            if sortedriwayatPinjam[i][5] == 'y':
                print("Status                  : Sudah dikembalikan semua")
            else:
                sisa = int(sortedriwayatPinjam[i][4]) - int(sortedriwayatKembali[i][3])
                print("Status                  : Belum dikembalikan semua")
                print("Sisa                    : {}".format(sisa))
        count += 1 # menambah jumlah data yang telah dicetak
        pil = input("\nApakah Anda ingin melihat data riwayat lainnya?(y/n)")
        if pil == "y" :
            return cetakRiwayatKembali(count,sortedriwayatPinjam,sortedriwayatKembali,panjang-1) # mengembalikan pada fungsi cetak riwayat dan mengurangi panjang list yang belum dicetak 
        else :
            return
    elif panjang == 0: # tidak terdapat data pada file consumable_history
        print("Tidak terdapat data riwayat pengembalian.")
        return
    else : # panjang data <= 1
        for i in range(count,len(sortedriwayatKembali)): # prosedur percetakan
            print("\nID Pengembalian         :", sortedriwayatKembali[i][0])
            for j in range(len(variabelGlobal.user['data'])):
                if sortedriwayatKembali[i][1] == variabelGlobal.user['data'][j][0]:
                    print("Nama Pengambil          :", variabelGlobal.user['data'][j][1])
                    break
            for k in range(len(variabelGlobal.gadget['data'])):
                if sortedriwayatKembali[i][2] == variabelGlobal.gadget['data'][k][0]:
                    print("Nama Gadget             :", variabelGlobal.consumable['data'][k][1])
                    break
            print("Tanggal Pengembalian    :", sortedriwayatKembali[i][2])
            if sortedriwayatPinjam[i][5] == 'y':
                print("Status                  : Sudah dikembalikan semua")
            else:
                sisa = int(sortedriwayatPinjam[i][4]) - int(sortedriwayatKembali[i][3])
                print("Status                  : Belum dikembalikan semua")
                print("Sisa                    : {}".format(sisa))
        return
