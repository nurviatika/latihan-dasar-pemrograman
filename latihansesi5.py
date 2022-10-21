# siti nurviatika
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen barang
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen / 100
# print harga barang beserta nama barang

#harga_keuntungan =int(harga barang) * persen / 100
#harga_jual + int(harga barang) + harga keuntungan
#print(nama_barang,"dijual dengan: ",harga_jual)


while(True):    
    nama_barang = input ("masukan nama barang : ")
    harga_barang = int(input("masukan harga barang : "))
    besaran_untung = int(input("masukan besaran untung : "))

    harga_keuntungan = int(harga_barang) * besaran_untung / 100
    harga_jual = int(harga_barang + harga_keuntungan)

    print (nama_barang, "dijual dengan harga :",harga_jual)

    apakah_lanjut = input("apakah akan menghitung barang lain? Y lanjut N tidak")
    if(apakah_lanjut != 'Y'):
        break

# print harga barang beserta nama barang

modal_keseluruhan = 0
laba_keseluruhan = 0

while (True):
    nama_barang = input("masukan nama barang ")
    harga_barang = int(input("masukan harga barang "))
    persen = int(input("masukan persen barang "))
    barang_terjual = int(input("masukan jumlah barang terjual "))

    keuntungan_persen = harga_barang * persen / 100
    harga_jual = harga_barang + keuntungan_persen

    # menghitung modal
    modal = harga_barang * barang_terjual
    # menghitung modal keseluruhan
    modal_keseluruhan = modal_keseluruhan + modal

    # menghitung laba
    laba = keuntungan_persen * barang_terjual
    # menghitung laba keseluruhan
    modal_keseluruhan = laba_keseluruhan + laba

    print("barang", nama_barang)
    print("harga_barang", harga_barang)
    print("keuntungan per barang", keuntungan_persen)
    print("dijual dengan harga", harga_jual)
    print("terjual", barang_terjual)
    print("modal", modal)         
    print("laba", laba)

    apakah_lanjut = input("apakah ingin input barang lain? Y lanjut N tidak")
    if(apakah_lanjut != "Y"):
        break

print("---------------")
print("modal keseluruhan",modal_keseluruhan)
print("laba keseluruhan",laba_keseluruhan)
