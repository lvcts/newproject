#program
while True:

    tanah = int(input('Jumlah tanah yang ingin di beli (m): '))
    harga_kotor = tanah * 300000
    if harga_kotor > 100000000 :
        pajak = harga_kotor*5/100
        harga_bersih = harga_kotor+pajak
    elif harga_kotor > 50000000 :
        pajak = harga_kotor*3/100
        harga_bersih = harga_kotor+pajak
    else :
        pajak = harga_kotor*1/100
        harga_bersih = harga_kotor+pajak
    print(f'Tanah seluas {tanah} meter')
    print(f'Harga : {harga_kotor}')
    print(f'Pajak : {pajak}')
    print(f'Harga yang harus dibayar : {harga_bersih} ')
    menu = input('Lakukan transaksi lain? (y/n)')
    menu = menu.lower()
    if menu == 'y':
        True
    elif menu =='n':
        break
    else :
        print('Salah')
        exit

