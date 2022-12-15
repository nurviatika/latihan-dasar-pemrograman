print("====== SITI NURVIATIKA=====")
print("===== aplikasi To Do List =====")

print("To Do List")
list = []  # Contoh Build-in List
for index, p in enumerate(list):
    print(index+1, p)
while (True) :
    print("\nMenu Fungsi")
    print('1. Tambah List'
          '\n2. Hapus List'
          '\n3. Quit')

    print(" \n----------------------------------------")
    listMenu = input("Masukan Pilihan : ")

    if listMenu == "1":
        print("Menu Fungsi -> Tambah List")
        while (True):
            list.append(input('\nMasukan Kegiatan : '))

            apakahLanjut = input("Apakah mau menambah lagi? Y or N : ")
            if (apakahLanjut != 'y'):
                break

        print('\nTo Do List sudah di Update :')
        for index, p in enumerate(list):
            print(index+1, p)

        print("\n=== === === === ===")

    elif listMenu == "2":
        print("Menu Fungsi -> Hapus List")
        list.clear()
        print('\nTo Do List sudah di Update : \n-')
        for index, p in enumerate(list):
            print(index+1, p)

    else:
        break
