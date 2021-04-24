from datetime import datetime

# Fungsi split()
def split(string, delimiters=';'):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''
    if word:
        result.append(word)
    return result

# Merapihkan data
def convert_line_to_data(line):
    raw_array_of_data = split(line)
    array_of_data = [data.strip() for data in raw_array_of_data]
    return array_of_data

# Merubah data ke string
def convert_datas_to_string():
  string_data = ";".join(header) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def convert_array_data_to_real_values(array_data):
    arr_cpy = array_data[:]
    for i in range(3):
        if (i == 0):
            arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

# Membaca file dengan ID yang bersangkutan
f = open("gadget_return_history.csv", "r")
raw_lines = f.readlines()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
f.close()

# Mencek apakah data kosong
if lines == []:
    print("Data kosong")
    exit()

# Menghilangkan header untuk sementara
raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)

# Merubah array of data menjadi datas(array of array)
raw_datas =[]
for line in lines:
    array_of_data = convert_line_to_data(line)
    real_values = convert_array_data_to_real_values(array_of_data)
    raw_datas.append(real_values)

# Mengurutkan data berdasarkan tanggal (descending)
datas = sorted(raw_datas , key = lambda row: datetime.strptime(row[3], "%d/%m/%Y"), reverse = True)

# Mengeluarkan n data (n<5) tiap sekali output
if len(datas) < 5:
    for i in range (0,len(datas)):
        print("ID Pengembalian      : ", datas[i][0])
        print("Nama Pengambil       : ", datas[i][1])
        print("Nama Gadget          : ", datas[i][2])
        print("Tanggal Pengembalian : ", datas[i][3])
        print("\n")
    exit()

# Mengeluarkan 5 data tiap sekali output
N = 5
a = 0
for i in range(a,N):
    print("ID Pengembalian      : ", datas[i][0])
    print("Nama Pengambil       : ", datas[i][1])
    print("Nama Gadget          : ", datas[i][2])
    print("Tanggal Pengembalian : ", datas[i][3])
    print("\n")
    a += 1
    N += 1
print("...")

while a != len(datas):
    showmore = input("Show more? (Y/N) : ")
    if showmore == 'Y' or showmore == 'y':
        if len(datas) < N:
            for i in range(a, len(datas)):
                print("ID Pengembalian      : ", datas[i][0])
                print("Nama Pengambil       : ", datas[i][1])
                print("Nama Gadget          : ", datas[i][2])
                print("Tanggal Pengembalian : ", datas[i][3])
                print("\n")
                a += 1

        else:
            for i in range(a, N):
                print("ID Pengembalian      : ", datas[i][0])
                print("Nama Pengambil       : ", datas[i][1])
                print("Nama Gadget          : ", datas[i][2])
                print("Tanggal Pengembalian : ", datas[i][3])
                print("\n")
                a += 1
                N += 1

    elif showmore == 'N' or showmore == 'n':
        exit()
    else:
        print("Input invalid")