import validasi, variabelGlobal
from datetime import datetime
from riwayatGadget import cetakRiwayatPinjam, cetakRiwayatKembali

def carirarity():   # Fungsi carirarity
    rarity = input("\nMasukkan rarity: ")
    print('\nHasil Pencarian:\n')
    count = 0
    for i in range(len(variabelGlobal.gadget['data'])):   # mengecek apakah barang dengan rarity tersebut ada, serta menghitung
        if rarity == variabelGlobal.gadget['data'][i][4]: # jumlah dari barang dengan rarity tersebut
            count += 1
            cetakKet(i)
    if count == 0:
        print("Tidak ada gadget yang ditemukan")
    return

def caritahun():    # Fungsi caritahun
    tahun = int(input("\nMasukkan tahun: "))
    catg = input("Masukkan kategori: ")
    print("\nHasil Pencarian:\n")
    count = 0
    if catg == "=":
        for i in range(len(variabelGlobal.gadget['data'])):
            if tahun == int(variabelGlobal.gadget['data'][i][5]):
                count += 1
                cetakKet(i)
    elif catg == '<':
        for i in range(len(variabelGlobal.gadget['data'])):
            if tahun > int(variabelGlobal.gadget['data'][i][5]):
                count += 1
                cetakKet(i)
    elif catg == '>':
        for i in range(len(variabelGlobal.gadget['data'])):
            if tahun < int(variabelGlobal.gadget['data'][i][5]):
                count += 1
                cetakKet(i)
    elif catg == '<=':
        for i in range(len(variabelGlobal.gadget['data'])):
            if tahun >= int(variabelGlobal.gadget['data'][i][5]):
                count += 1
                cetakKet(i)
    elif catg == '>=':
        for i in range(len(variabelGlobal.gadget['data'])):
            if tahun <= int(variabelGlobal.gadget['data'][i][5]):
                count += 1
                cetakKet(i)
    if count == 0:
        print("Tidak ada gadget yang ditemukan")
    return

def cetakKet(i):    # beberapa data yang akan ditampilkan pada carirarity dan caritahun
    print("Nama             : {}".format(variabelGlobal.gadget['data'][i][1]))
    print("Deskripsi        : {}".format(variabelGlobal.gadget['data'][i][2]))
    print("Jumlah           : {}".format(variabelGlobal.gadget['data'][i][3]))
    print("Rarity           : {}".format(variabelGlobal.gadget['data'][i][4]))
    print("Tahun ditemukan  : {}\n".format(variabelGlobal.gadget['data'][i][5]))
    return

def IDToNama(x):
    #input : id_gadget, selalu valid
    #output : nama gadget dari id yang bersangkutan
    for record in variabelGlobal.gadget['data'] :
        if record[0] == x :
            return record[1]

def KembalikanGadget():
    #I.S. Pengguna sudah login, semua informasi user dan data sudah tersimpan di modul variabelGlobal
    # pengguna memilih 'kembalikan'
    #F.S. Tercatat riwayat pengembalian pada gadget_return_history
    data = TunjukkanDaftarGadget()
    valid = False
    while not valid :
        yangDikembalikan = input('Masukkan nomor peminjaman: ')
        if yangDikembalikan.isnumeric():
            yangDikembalikan = int(yangDikembalikan)
            if (0<yangDikembalikan) and (yangDikembalikan <=len(data[0])) :
                valid = True 
            else :
                print('Nomor tidak valid !')
                lanjutkan = input('Ingin mengulangi ? y/n : ')
                if (lanjutkan !='y'):
                    return
        else :
            print('Nomor tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return

    valid = False
    while not valid:        
        tanggal_pengembalian = input('Tanggal pengembalian (DD/MM/YYYY): ')
        valid = validasi.isTanggalValid(tanggal_pengembalian)
        if not valid :
            print('Tanggal tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return

    valid = False
    while not valid:
        jumlah_pengembalian = input('Masukkan jumlah gadget yang ingin dikembalikan: ')
        if jumlah_pengembalian.isnumeric():
            jumlah_pengembalian = int(jumlah_pengembalian)
            if (0<jumlah_pengembalian) and (jumlah_pengembalian <= data[1][yangDikembalikan-1]):
                valid = True
            else :
                print('Jumlah tidak valid !')
                lanjutkan = input('Ingin mengulangi ? y/n : ')
                if (lanjutkan !='y'):
                    return
        else :
            print('Jumlah tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return
    
    id_peminjaman = data[2][yangDikembalikan-1]
    
    #Mencatat di gadget_return_history
    if variabelGlobal.gadget_return_history['data'] == []:
        variabelGlobal.gadget_return_history['data'].append([1, id_peminjaman, tanggal_pengembalian, jumlah_pengembalian])
    else :
        indeks_terakhir = int(variabelGlobal.gadget_return_history['data'][-1][0])
        variabelGlobal.gadget_return_history['data'].append([indeks_terakhir+1, id_peminjaman, tanggal_pengembalian, jumlah_pengembalian])

    #Menambah jumlah di gadget
    for indeks in range(len(variabelGlobal.gadget['data'])) :
        if variabelGlobal.gadget['data'][indeks][1] == data[0][yangDikembalikan-1]:
            variabelGlobal.gadget['data'][indeks][3] = str(int(variabelGlobal.gadget['data'][indeks][3])+jumlah_pengembalian)
    
    #Mengubah status di gadget_borrow_history apabila semua porsi peminjaman satu gadget sudah dikembalikan 
    for i in range(len(variabelGlobal.gadget_borrow_history['data'])):
        if variabelGlobal.gadget_borrow_history['data'][i][0]==id_peminjaman:
            total_peminjaman = int(variabelGlobal.gadget_borrow_history['data'][i][4])
    for j in range(len(variabelGlobal.gadget_return_history['data'])):
        if variabelGlobal.gadget_return_history['data'][j][1]==id_peminjaman:
            total_peminjaman -= int(variabelGlobal.gadget_return_history['data'][j][3])

    if total_peminjaman == 0:
        for i in range(len(variabelGlobal.gadget_borrow_history['data'])):
            if variabelGlobal.gadget_borrow_history['data'][i][0] == id_peminjaman:
                variabelGlobal.gadget_borrow_history['data'][i][5] = 'y'

    print('Item '+data[0][yangDikembalikan-1]+' telah dikembalikan sebanyak '+str(jumlah_pengembalian)+' buah !')


def PinjamGadget():
    #Prosedur
    #I.S. Pengguna sudah login dan memilih opsi peminjaman gadget
    #F.S. pengguna sudah meminjam gadget (bila gadget masih tersedia) dan terekam dalam gadget_borrow_history
    # bila gadget sudah tidak tersedia, pengguna mendapat pesan peringatan
    valid = False
    while not valid:
        id_item = input('Masukkan ID item:')
        valid = (validasi.isIDGadgetValid(id_item) and (not validasi.isSedangDipinjam(variabelGlobal.id_user, id_item)))
        if not valid :
            print('ID item tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return

    valid = False
    while not valid:        
        tanggal_peminjaman = input('Tanggal peminjaman (DD/MM/YYYY): ')
        valid = validasi.isTanggalValid(tanggal_peminjaman)
        if not valid :
            print('Tanggal tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return

    valid = False
    while not valid:        
        jumlah_peminjaman = input('Jumlah peminjaman: ')
        valid = validasi.isJumlahPeminjamanValid(id_item,jumlah_peminjaman)
        if not valid :
            print('Jumlah tidak valid !')
            lanjutkan = input('Ingin mengulangi ? y/n : ')
            if (lanjutkan !='y'):
                return
    #Mencatat di gadget_borrow_history
    if variabelGlobal.gadget_borrow_history['data'] == []:
        variabelGlobal.gadget_borrow_history['data'].append([1, variabelGlobal.id_user, id_item, tanggal_peminjaman, jumlah_peminjaman, 'n'])
    else :
        indeks_terakhir = int(variabelGlobal.gadget_borrow_history['data'][-1][0])
        variabelGlobal.gadget_borrow_history['data'].append([indeks_terakhir+1, variabelGlobal.id_user, id_item, tanggal_peminjaman, jumlah_peminjaman,'n'])
        
    #Mengurangi jumlah di gadget
    for indeks in range(len(variabelGlobal.gadget['data'])) :
        if variabelGlobal.gadget['data'][indeks][0] == id_item:
            variabelGlobal.gadget['data'][indeks][3] = str(int(variabelGlobal.gadget['data'][indeks][3])-int(jumlah_peminjaman))

    print('Item '+IDToNama(id_item)+' berhasil dipinjam!')

def TunjukkanDaftarGadget():
    #I.S. Pengguna sudah login, semua informasi user dan data sudah tersimpan di modul variabelGlobal
    #F.S. Daftar gadget yang dipinjam oleh user tersebut tercetak pada layar 
    daftarIDGadgetYangDipinjam = []
    jumlahGadgetYangDipinjam = []
    IDPeminjaman = []
    for record in variabelGlobal.gadget_borrow_history['data'] :
        if (record[1]==variabelGlobal.id_user) and (record[5]=='n'):
            jumlahDipinjam = int(record[4])
            for baris in variabelGlobal.gadget_return_history['data'] :
                if record[0]==baris[1]:
                    jumlahDipinjam -= int(baris[3])
            #Dijamin hanya ada satu record peminjaman dengan status 'n' untuk tiap gadget pada user yang sama 
            daftarIDGadgetYangDipinjam.append(record[2])
            jumlahGadgetYangDipinjam.append(jumlahDipinjam)
            IDPeminjaman.append(record[0])

    
    daftarGadgetYangDipinjam = [IDToNama(x) for x in daftarIDGadgetYangDipinjam]
    #Cetak pada layar
    for i in range(len(daftarGadgetYangDipinjam)):
        print(str(i+1)+'. '+daftarGadgetYangDipinjam[i]+' ('+str(jumlahGadgetYangDipinjam[i])+' buah)')

    return [daftarGadgetYangDipinjam, jumlahGadgetYangDipinjam, IDPeminjaman] #Mengembalikan data gadget yang dipinjam
    
def riwayatpinjam():
    sortedriwayatPinjam = sorted(variabelGlobal.gadget_borrow_history['data'], key = lambda row: datetime.strptime(row[3], "%d/%m/%Y"), reverse = True)
    count = 0
    panjang = len(sortedriwayatPinjam)
    cetakRiwayatPinjam(count,sortedriwayatPinjam,panjang)

def riwayatkembali():
    sortedriwayatPinjam = sorted(variabelGlobal.gadget_borrow_history['data'], key = lambda row: datetime.strptime(row[3], "%d/%m/%Y"), reverse = True)
    sortedriwayatKembali = sorted(variabelGlobal.gadget_return_history['data'], key = lambda row: datetime.strptime(row[2], "%d/%m/%Y"), reverse = True)
    count = 0
    panjang = len(sortedriwayatKembali)
    cetakRiwayatKembali(count,sortedriwayatPinjam,sortedriwayatKembali,panjang)
