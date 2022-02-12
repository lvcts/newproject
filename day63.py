class taman_bunga():
    jumlah_bunga = 0
    
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        taman_bunga.jumlah_bunga += 1
        
    def berapa_jumlah():
        print('Total Produk Kita: ', Produk.jumlah_bunga)
        
    def detail_produk(self):
        print("Nama : ", self.nama)
        print("Harga: ", self.harga)
        print()
        
# membuat objek pertama
produk1 = taman_bunga('mawar', 500)

# membuat objek kedua
produk2 = taman_bunga('melati', 300)

# mengakses attribut objek
produk1.detail_produk()
produk2.detail_produk()

taman_bunga.berapa_jumlah()
