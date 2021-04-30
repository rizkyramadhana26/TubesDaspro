import variabelGlobal

def tambahitem(): # Fungsi tambahitem
    idx = input("Masukkan ID: ")
    checkIDtambah(idx)
    return

def hapusitem(): # Fungsi hapusitem
    idx = input("Masukkan ID: ")
    checkIDhapus(idx)
    return

def checkIDtambah(idx):
# Fungsi ini digunakan untuk mengecek apakah ID item yang diinput user sudah sesuai atau belum
    if idx[0] != 'G' and idx[0] != 'C':
        print('\nGagal menambahkan item karena ID tidak valid')
    else:
        if idx[0] == 'G':
            for i in range(len(variabelGlobal.gadget['data'])):
                if variabelGlobal.gadget['data'][i][0] == idx: # jika ID sudah terpakai, maka proses modifikasi data item gagal
                    print('\nGagal menambahkan item karena ID sudah ada')
                    return
            # jika item memang belum ada, dilakukan beberapa pendetilan dari data item yang ditambahkan
            namaGadget = input('Masukkan Nama: ') # nama item
            descGadget = input('Masukkan Deskripsi: ') # deskripsi
            nGadget = input('Masukkan Jumlah: ')    # jumlah item
            rareGadget = input('Masukkan Rarity: ') # rarity
            tahunGadget = input('Masukkan Tahun Ditemukan: ') # tahun ditemukan
            if rareGadget != 'C' and rareGadget != 'B' and rareGadget != 'A' and rareGadget != 'S':
                print('\nInput rarity tidak valid!')
            else:
                print('\nItem telah berhasil ditambahkan ke database')
                newData = [idx,namaGadget,descGadget,nGadget,rareGadget,tahunGadget]
                variabelGlobal.gadget['data'].append(newData)
            return
        else:
            for i in range(len(variabelGlobal.consumable['data'])):
                if variabelGlobal.consumable['data'][i][0] == idx:
                    print('\nGagal menambahkan item karena ID sudah ada')
                    return
            namaConsum = input('Masukkan Nama: ') 
            descConsum = input('Masukkan Deskripsi: ')
            nConsum = input('Masukkan Jumlah: ')
            rareConsum = input('Masukkan Rarity: ')
            if rareConsum != 'C' and rareConsum != 'B' and rareConsum != 'A' and rareConsum != 'S':
                print('\nInput rarity tidak valid!')
            else:
                print('\nItem telah berhasil ditambahkan ke database')
                newData = [idx,namaConsum,descConsum,nConsum,rareConsum]
                variabelGlobal.consumable['data'].append(newData)
            return            
    return

def checkIDhapus(idx):
    if idx[0] != 'G' and idx[0] != 'C':
        print('\nTidak ada item dengan ID tersebut')
    else:
        if idx[0] == 'G':
            newdata = []
            for i in range(len(variabelGlobal.gadget['data'])):
                if idx != variabelGlobal.gadget['data'][i][0]:
                    newdata.append(variabelGlobal.gadget['data'][i])
            if newdata == variabelGlobal.gadget['data']:
                print('\nTidak ada item dengan ID tersebut')
            else:
                variabelGlobal.gadget['data'] = newdata
                print('\nItem telah berhasil dihapus dari database')
            return
        else:
            newdata = []
            for i in range(len(variabelGlobal.consumable['data'])):
                if idx != variabelGlobal.consumable['data'][i][0]:
                    newdata.append(variabelGlobal.consumable['data'][i])

            if newdata == variabelGlobal.consumable['data']:
                print('\nTidak ada item dengan ID tersebut')
            else:
                variabelGlobal.consumable['data'] = newdata
                print('\nItem telah berhasil dihapus dari database')
            return
    return

def ubahjumlah():
    idx = input("Masukkan id: ")
    if idx[0] == "G":
        for i in range(len(variabelGlobal.gadget['data'])):
            if idx == variabelGlobal.gadget['data'][i][0]:
                add = int(input("Masukkan berapa yang diambil/ditambah pada {}: ".format(variabelGlobal.gadget['data'][i][1])))
                result = int(variabelGlobal.gadget['data'][i][3]) + add
                if result < 0:
                    print("Tidak mungkin diubah karena {} - {} < 0".format(variabelGlobal.gadget['data'][i][3],abs(add)))
                    return
                variabelGlobal.gadget['data'][i][3] = str(result)
                print("\nData berhasil diubah")
                return
        print("\nTidak ada item dengan ID tersebut")
    elif idx[0] == 'C':
        for i in range(len(variabelGlobal.consumable['data'])):
            if idx == variabelGlobal.consumable['data'][i][0]:
                add = int(input("Masukkan berapa yang diambil/ditambah pada {}: ".format(variabelGlobal.consumable['data'][i][1])))
                result = int(variabelGlobal.consumable['data'][i][3]) + add
                if result < 0:
                    print("Tidak mungkin diubah karena {} - {} < 0".format(variabelGlobal.consumable['data'][i][3],abs(add)))
                    return
                variabelGlobal.consumable['data'][i][3] = str(result)
                print("\nData berhasil diubah")
                return
        print("\nTidak ada item dengan ID tersebut")
    else:
        print('\nTidak ada item dengan ID tersebut')
    return
