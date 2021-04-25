import validasi, variabelGlobal

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

def PinjamGadget():
    #Prosedur
    #I.S. Pengguna sudah login dan memilih opsi peminjaman gadget
    #F.S. pengguna sudah meminjam gadget (bila gadget masih tersedia) dan terekam dalam gadget_borrow_history
    # bila gadget sudah tidak tersedia, pengguna mendapat pesan peringatan
    valid = False
    while not valid:
        id_item = input('Masukkan ID item:')
        valid = validasi.isIDGadgetValid(id_item)
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
        variabelGlobal.gadget_borrow_history['data'].append([1, variabelGlobal.id_user, id_item, tanggal_peminjaman, jumlah_peminjaman])
    else :
        indeks_terakhir = int(variabelGlobal.gadget_borrow_history['data'][-1][0])
        variabelGlobal.gadget_borrow_history['data'].append([indeks_terakhir+1, variabelGlobal.id_user, id_item, tanggal_peminjaman, jumlah_peminjaman])
        
    #Mengurangi jumlah di gadget
    for indeks in range(len(variabelGlobal.gadget['data'])) :
        if variabelGlobal.gadget['data'][indeks][0] == id_item:
            variabelGlobal.gadget['data'][indeks][3] = str(int(variabelGlobal.gadget['data'][indeks][3])-int(jumlah_peminjaman))
