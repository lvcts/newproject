'''Buat sebuah program, tampilan struk pembayaran di sebuah kafe. Yang menyediakan 3
buah paket yaitu paket hemat, paket nasi, paket spesial dengan harga yang berbedabeda:
a. Untuk paket hemat harga Rp. 7.500,-
b. Untuk paket nasi harga Rp. 10.000,-
c. Untuk paket spesial harga Rp. 15.000,-
Dan akan dikenakan Ppn untuk setiap paketnya adalah 10% dari total.
Untuk tampilan awal program buat pilihan kode paket;
1. Untuk paket hemat kodenya 
2. Untuk paket nasi kodenya 2
3. Untuk paket spesial kodenya 3
Tambahkan juga input untuk jumlah pembelian, kode kasir dan nama kasir. Ketiga
inputan ini akan ditampilkan lagi pada tampilan output program.'''

kode = input('Masukkan Kode [1....3]?\t:')
jumlah = int(input('Jumlah Beli \t:'))
kode_kasir = input('Kode Kasir \t:')
nama_kasir = input('Nama Kasir \t:')

print('''
            SEJAHTER CAFE
        JL. PDI PERJUANGAN NO.16
        TELP.7236574-7236574
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ''')
if kode == '1':
    harga = 7500
    print('''
                PAKET SPESIAL
                ''',jumlah,''' X ''',harga)
elif kode == '2':
    harga = 10000
    print('''
                PAKET SPESIAL
                ''',jumlah,''' X ''',harga)
elif kode == '3':
    harga = 15000
    print('''
                PAKET SPESIAL
                ''',jumlah,''' X ''',harga)
else:
    print('404')
total_harga = jumlah*harga
ppn = total_harga*10/100
bayar = total_harga+ppn
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\t\tTotal \t:',total_harga)
print('\t\tPPN 10% \t:',ppn)
print('\t\tJumlah Bayar \t:',bayar)
dbayar = int(input('\t\tJumlah Bayar \t:'))
kembali = dbayar-bayar
print('\t\tKembali \t:',kembali)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('''
            SELAMAT MENIKMATI
            TERIMA KASIH \n\t'''
                ,kode_kasir,nama_kasir)
