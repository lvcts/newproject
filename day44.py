'''Buat program untuk struk pembayaran di sebuah Warnet. Gunakan pernyataan Nestedif;
Jika kode P maka dia adalah pelanggan warnet, harga sewanya Rp. 4.000,- dan jika dia
menyewa lebih dari atau sama dengan 5 jam maka mendapat potongan 50% dari total
harga tapi jika dia hanya menyewa lebih besar atau sama dengan 3 jam maka dia
mendapat potongan 30% dari total harga.
Selain itu adalah pelanggan umum dengan harga sewa Rp. 5.000,- dan mendapat
potongan yang sama. Hitung lah total pembayaran dan uang kembali??'''

print('WARNETTTT')
while True:
    print('==================================')
    nama_pengunjung = input('Nama Pengunjung \t :')
    waktu = int(input('Lama Sewa \t :'))
    keterangan = input('Keterangan \t :')
    if keterangan == 'p':
        harga_sewa = 4000
        if waktu >= 5:
            harga_bayar = waktu*harga_sewa
            diskon  = harga_bayar*50/100
        elif waktu >= 3:
            harga_bayar = waktu*harga_sewa
            diskon  = harga_bayar*30/100
        else :
            harga_bayar = waktu*harga_sewa
    elif keterangan == 'u':
        harga_sewa = 5000
        if waktu >= 5:
            harga_bayar = waktu*harga_sewa
            diskon  = harga_bayar*50/100
        elif waktu >= 3:
            harga_bayar = waktu*harga_sewa
            diskon  = harga_bayar*30/100
        else :
            harga_bayar = waktu*harga_sewa
    else:
        print('404 Not Found')
    print('Total Pembayaran \t :',diskon)
    print('==================================')
    uang_bayar = int(input('Uang Bayar \t : '))
    uang_kembali = uang_bayar - diskon
    print('Uang Kembali \t :',uang_kembali)
    menu = input('Input data lagi? (y/t) \t :')
    menu = menu.lower()
    if menu == 'y':
        True
    elif menu == 'n':
        break
    else:
        exit()

