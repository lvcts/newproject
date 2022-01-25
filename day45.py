''' Toko Buku Sejahtera menjual buku-buku diantara:
1. Sukses Belajar Borland C++ harga Rp. 50.000,-
2. Kunci Pribadi Sukses harga Rp. 35.000,-
3. Mencari Mutiara Di Dasar Hati harga Rp. 45.000,-
Akan mendapat potongan 10% dari total pembelian jika anda membeli lebih dari dan
sama dengan 3 buah buku serta mendapat bonus “buku saku”, jika beli kurang dari 3
buah buku, anda tidak dapat potongan serta akan tampil pesan “maaf tidak dapat
bonus”. Semua pembelian akan terkena ppn sebesar 2% dari total pembelian'''

def buku():
    print('''
                 Toko Buku 
        1. Sukses Belajar Borland C++ : Rp. 50.000,-
        2. Kunci Pribadi Sukses : Rp. 35.000,-
        3. Mencari Mutiara Di Dasar Hati : Rp. 45.000,-
        ''')
buku()
print('========================================================')
nomor_buku = input('Nomor buku \t :')
jumlah = int(input('Jumlah buku \t :'))
if nomor_buku == '1':
    print('Judul buku \t : Sukses Belajar Borland C++')
    harga = 50000
elif nomor_buku == '2':
    print('Judul buku \t : Kunci Pribadi Sukses')
    harga = 35000
elif nomor_buku == '3':
    print('Mencari Mutiara Di Dasar Hati')
    harga = 45000
else:
    exit()
total_harga = harga * jumlah
print('Harga buku yang anda beli \t :',total_harga)
if jumlah >= 3 :
    diskon = total_harga * 10/100
    total_bayar = total_harga - diskon
    bonus = 'Buku saku'
    print('Anda dapat potongan \t :',diskon)
    print('Bonus yang anda peroleh \t :',bonus)
else :
    print('Tidak dapat potongan')
    bonus='-'
    total_bayar = total_harga
biaya_ppn = total_bayar*2/100
fix_bayar = total_bayar + biaya_ppn
print('Total bayar buku \t :',fix_bayar)



    
