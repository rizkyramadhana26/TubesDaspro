import gadget, modifItem, user, save, consumable #riwayatkembali, riwayatpinjam
def Show(role):    # Laman Utama [Ini tidak sesuai spesifikasi yang diinginkan]
    inUser = input(">>> ")
    # aksi yang terjadi berdasarkan input user
    if inUser == 'caritahun':
        while True:
            gadget.caritahun()
            pil = input("Apa masih mencari caritahun (y/n)?:\n>>> ")
            if pil == 'n':
                Show(role)
    if inUser == 'carirarity':
        while True:
            gadget.carirarity()
            pil = input("Apa masih mencari carirarity (y/n)?:\n>>> ")
            if pil == 'n':
                Show(role)
    if inUser == 'tambahitem':
        if role == 'admin':
            while True:
                modifItem.tambahitem()
                pil = input("Apa masih ingin menambah item (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'hapusitem':
        if role == 'admin':
            while True:
                modifItem.hapusitem()
                pil = input("Apa masih ingin menghapus item (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'ubahjumlah':
        if role == 'admin':
            while True:
                modifItem.ubahjumlah()
                pil = input("Apa masih ingin mengubah jumlah item (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'register':
        if role == 'admin':
            while True:
                user.register()
                pil = input("Apa masih ingin me-register lagi (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'pinjam':
        if role == 'user':
            while True:
                gadget.PinjamGadget()
                pil = input("Apa masih ingin meminjam lagi (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role) 
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'kembalikan':
        if role == 'user':
            while True:
                gadget.KembalikanGadget()
                pil = input("Apa masih ingin mengembalikan lagi (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role) 
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'minta':
        if role == 'user':
            while True:
                consumable.minta()
                pil = input("Apa masih ingin meminta lagi (y/n)?:\n>>> ")
                if pil == 'n':
                    Show(role) 
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'riwayatambil':
        if role == 'admin':
            consumable.riwayatambil()
            Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'riwayatpinjam':
        if role == 'admin':
            gadget.riwayatpinjam()
            Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'riwayatkembali':
        if role == 'admin':
            gadget.riwayatkembali()
            Show(role)
        else:
            print('Anda tidak memiliki ijin akses')
            Show(role)
    if inUser == 'help':
        Help(role)
        Show(role)
    if inUser == 'save':
        save.Save()
        Show(role)
    if inUser == 'exit':
        pil = input("Apa Anda ingin untuk menyimpan perubahan (y/n)?\n>>> ")
        if pil == 'y':
            save.Save()
        exit()
    else:
        print('Terdapat kesalahan input, ketik \'help\' agar melihat list command')
        Show(role)
    return

def Help(role):
    print("\n======== Help Command =========")
    print(" 1.  Mencari gadget berdasarkan rarity       [carirarity]")
    print(" 2.  Mencari gadget berdasarkan tahun        [caritahun]")
    if role == 'admin':
        print(" 3.  Menambah item (gadget/consumable)       [tambahitem]")
        print(" 4.  Menghapus item (gadget/consumable)      [hapusitem]")
        print(" 5.  Mengubah jumlah item (gadget/consumable)[ubahjumlah]")
        print(" 6.  Melihat riwayat peminjaman gadget       [riwayatpinjam]")
        print(" 7.  Melihat riwayat pengembalian gadget     [riwayatkembali]")
        print(" 8.  Melihat riwayat pengambilan consumable  [riwayatambil]")
        print(" 9.  Menambah user baru                      [register]")
        print(" 10. Menyimpan perubahan                     [save]")
        print(" 11. Meminta list command                    [help]")
        print(" 12. Keluar dari kantong ajaib               [exit]\n")
    if role == 'user':
        print(" 3.  Meminjam gadget                         [pinjam]")
        print(" 4.  Mengembalikan gadget                    [kembalikan]")
        print(" 5.  Meminta consumable                      [minta]")
        print(" 6.  Menyimpan perubahan                     [save]")
        print(" 7.  Meminta list command                    [help]")
        print(" 8.  Keluar dari kantong ajaib               [exit]\n")
