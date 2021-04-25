import utility, variabelGlobal
def isIDGadgetValid(id_gadget):
    #input : sebuah id_gadget bertipe string
    #output : True apabila id_gadget ada di gadgets.csv, False apabila id_gadget tidak ada di gadgets.csv
    listofIDGadget = [item[0] for item in variabelGlobal.gadget['data']]
    return (id_gadget in listofIDGadget)

def isJumlahPeminjamanValid(id_gadget, jumlahPeminjaman) : 
    #input : id_gadget bertipe string, jumlahPeminjaman  bertipe string
    #output : True apabila jumlah peminjaman kurang dari sama dengan jumlah gadget yang tersisa, selain itu False
    if isIDGadgetValid(id_gadget) and jumlahPeminjaman.isnumeric() :
        listofIDGadget = [item[0] for item in variabelGlobal.gadget['data']]
        indeks = listofIDGadget.index(id_gadget)
        sisaGadget = variabelGlobal.gadget['data'][indeks][3]
        return int(jumlahPeminjaman) <= int(sisaGadget)
    else :
        return False

def isSedangDipinjam(user_id, gadget_id):
    #input : user_id dan gadget_id
    #output : mengembalikan True apabila user dengan id user_id sedang meminjam gadget dengan id gadget_id, selain itu False
    sedangDipinjam = False
    for baris in variabelGlobal.gadget_borrow_history['data']:
        if (baris[1] == user_id) and (baris[2]==gadget_id) and (baris[5]=='n'):
            sedangDipinjam = True
    return sedangDipinjam

def isTanggalValid(tanggal):
    #input : sebuah string yang merepresentasikan tanggal
    #output : True apabila tanggal sesuai dengan format 'DD/MM/YYYY'
    valid = True
    elemenTanggal = []
    temporary = ''
    for i in range(len(tanggal)):
        if (tanggal[i] =='/') or (i==len(tanggal)-1) :
            elemenTanggal.append(int(temporary))
            temporary=''
        elif tanggal[i].isnumeric():
            temporary+=tanggal[i]
        else :
            valid = False
            break
    if (len(elemenTanggal) == 3) :
        hari = elemenTanggal[0]
        bulan = elemenTanggal[1]
        tahun = elemenTanggal[2]
    else :
        valid = False

    if valid: #disebut valid disini bila tanggal tidak terdiri atas huruf dan terdiri dari 3 elemen
        if (tahun%400 == 0) or ((tahun%400 != 0) and (tahun%100!=0) and (tahun%4 == 0)):
            if (bulan in [1,3,5,7,8,10,12]) and (1<=hari) and (hari <=31) :
                pass
            elif (bulan in [4,6,9,11]) and (1<= hari) and (hari <= 30) :
                pass
            elif (bulan == 2) and (1<=hari) and (hari<=29):
                pass
            else :
                valid = False
        else :
            if (bulan in [1,3,5,7,8,10,12]) and (1<=hari) and (hari <=31) :
                pass
            elif (bulan in [4,6,9,11]) and (1<= hari) and (hari <= 30) :
                pass
            elif (bulan == 2) and (1<=hari) and (hari<=28):
                pass
            else :
                valid = False
    return valid

def isCredentialValid(username,password):   # mengecek ketika login, apakah username dan password ada di file csv
    for i in range(len(variabelGlobal.user['data'])):
        if variabelGlobal.user['data'][i][2] == username:
            if variabelGlobal.user['data'][i][3] == password:
                variabelGlobal.id_user = variabelGlobal.user['data'][i][0]
                return True
    return False

def isUsernameValid(x):           # mengecek apakah username telah terpakai atau belum
    for i in range(len(variabelGlobal.user['data'])):
        if variabelGlobal.user['data'][i][2] == x:
            return False
    return True
