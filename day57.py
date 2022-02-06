#OOP
class bunga:
    jenis = None
    warna = None

    def nama (self):
        print(f'Ini adalah bunga {self.jenis} dan berwarna {self.warna}')
mawar = bunga()
mawar.jenis = "rose"
mawar.warna = "putih"

kamboja = bunga()
kamboja.jenis = "kamboja"
kamboja.warna = "pink"

mawar.nama()
kamboja.nama()
