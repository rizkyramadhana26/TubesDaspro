import os, time, utility, variabelGlobal
def Save():
    #I.S. variabel user,gadget,gadget_return_history, gadget_borrow_history, consumable, consumable_history sudah terdefinisi
    #F.S. variabel-variabel di atas akan disimpan di file csv yang berkaitan
    folderDir = input('Masukkan nama folder penyimpanan: ')
    if os.path.isdir(folderDir):
        utility.SimpanCSV(variabelGlobal.user['header'], variabelGlobal.user['data'], folderDir +'/user.csv')
        utility.SimpanCSV(variabelGlobal.gadget['header'], variabelGlobal.gadget['data'], folderDir +'/gadget.csv')
        utility.SimpanCSV(variabelGlobal.gadget_borrow_history['header'], variabelGlobal.gadget_borrow_history['data'], folderDir +'/gadget_borrow_history.csv')
        utility.SimpanCSV(variabelGlobal.gadget_return_history['header'], variabelGlobal.gadget_return_history['data'], folderDir +'/gadget_return_history.csv')
        utility.SimpanCSV(variabelGlobal.consumable['header'], variabelGlobal.consumable['data'], folderDir +'/consumable.csv')
        utility.SimpanCSV(variabelGlobal.consumable_history['header'], variabelGlobal.consumable_history['data'], folderDir +'/consumable_history.csv')
        print("saving..")
        time.sleep(2)
        print("Data telah disimpan pada folder {}".format(folderDir))
    else:
        os.makedirs(folderDir)
        utility.SimpanCSV(variabelGlobal.user['header'], variabelGlobal.user['data'], folderDir +'/user.csv')
        utility.SimpanCSV(variabelGlobal.gadget['header'], variabelGlobal.gadget['data'], folderDir +'/gadget.csv')
        utility.SimpanCSV(variabelGlobal.gadget_borrow_history['header'], variabelGlobal.gadget_borrow_history['data'], folderDir +'/gadget_borrow_history.csv')
        utility.SimpanCSV(variabelGlobal.gadget_return_history['header'], variabelGlobal.gadget_return_history['data'], folderDir +'/gadget_return_history.csv')
        utility.SimpanCSV(variabelGlobal.consumable['header'], variabelGlobal.consumable['data'], folderDir +'/consumable.csv')
        utility.SimpanCSV(variabelGlobal.consumable_history['header'], variabelGlobal.consumable_history['data'], folderDir +'/consumable_history.csv')
        print("saving..")
        time.sleep(2)
        print("Data telah disimpan pada folder {}".format(folderDir))
