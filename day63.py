class taman_bunga():
    jumlah_bunga = 0
    
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        taman_bunga.jumlah_bunga += 1
        
    def berapa_jumlah():
        print('Total Produk Kita: ', Produk.jumlah_bunga)
        
    def detail_produk(self):
        print("Nama : ", self.nama)
        print("Jenis: ", self.jenis)
        print()
        
produk1 = taman_bunga('mawar', 'merah')

produk2 = taman_bunga('melati', 'putih')

produk1.detail_produk()
produk2.detail_produk()

