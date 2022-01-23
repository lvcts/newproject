#STUDIO MUSIK
''' Buatlah source code dari ilustrasi berikut;
Sebuah studio musik, dengan nama studio musik Al Izzah menyewakan alat-alat musik
dengan tarif 1 jam pertama sebesar Rp 200.000,- yang merupakan tarif tetap untuk
setiap penyewaan. Untuk tarif jam berikutnya adalah 25% dari tarif tetap. Hitung berapa
total yang harus dibayar untuk setiap penyewaan lebih dari 1 jam?'''

while True :
    def rincian():
        print('========================================')
        print('Isi Daftar Penyewa Berikut : ')
        nama = input('Nama Penyewa    : ')
        alamat = input('Alamat    : ')
        no_telp = input('No.Telp    : ')
        print('========================================')
    def rental():
        lama_rental = int(input('Lama Rental(Menit)    :'))
        if lama_rental <= 60 :
            total_bayar = (lama_rental/60)*200000
        else :
            tarifselanjutnya = 200000*25/100
            lama_rental -= 60
            bayar = (lama_rental/60)*tarifselanjutnya
            total_bayar = bayar + 200000
        print('Total Bayar    :',total_bayar)
    rincian()
    rental()
    print('TERIMA KASIH !!!!')
    print('========================================')
    menu = input('Transksi lagi ? y/t : ')
    menu = menu.lower()
    if menu == 'y' :
        True
    elif menu == "t":
        break
    else:
        print('Invalid input')
        break
