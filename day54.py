from operator import truediv


def pilihan(): 
    print('''
    1       PAKET MEWAH     2000K
    2       PAKET SEDANG    1500K
    3       PAKET SEDERHANA 1000K

    Pilihan atraksi tambahan :
    B       BADUT           300K
    S       SULAP           500K
    else    PENYANYI CILIK  600K
    ''')
def way():
    print('********** PAKET ULANG TAHUN **********')
    nama = input('\t\t\t')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    pilihan_paket = input('Paket pilihannya adalah\t:')
    if pilihan_paket == '1':
        harga=2000000
        print('Jenis paket pilihan\t:Mewah')
        print('Harga per paket\t:',harga)
    elif pilihan_paket == '2':
        harga=1500000
        print('Jenis paket pilihan\t:Mewah')
        print('Harga per paket\t:',harga)
    elif pilihan_paket == '3':
        harga=1000000
        print('Jenis paket pilihan\t:Mewah')
        print('Harga per paket\t:',harga)
    else:
        print('404')
    atraksi = input('Atraksi pilihan\t:')
    atraksi = atraksi.lower()
    if atraksi == 'b':
        harga_atraksi = 300000
        print('Harga atraksi\t:',harga_atraksi)
    elif atraksi == 's':
        harga_atraksi = 500000
        print('Harga atraksi\t:',harga_atraksi)
    else:
        harga_atraksi = 600000
        print('Harga atraksi\t:',harga_atraksi)
    print('=============================================')
    print('Bonus => Black Forest')
    print('=============================================')
    total = harga + harga_atraksi
    discount = total * 10 / 100
    total_bayar = total - discount
    print('Total seluruh\t:',total)
    print('Potongan yang diperoleh\t:',discount)
    uang_bayar = int(input('Uang bayar\t:'))
    uang_kembali = uang_bayar - total_bayar
    print('Uang kembali\t:',uang_kembali)
    print('=============================================')

while True:
    pilihan()
    way()
    menu = input('Mau input data lagi? [y/t]\t:')
    menu = menu.lower()
    if menu == 'y':
        True
    elif menu == 't':
        break
    else: 
        exit