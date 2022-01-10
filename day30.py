#lokal
def lokal():
    #variabel lokal
    name = "Zahra"
    print(name)
lokal()
print('============================================')

#lokal
def lokal():
    #variabel lokal
    print('Lokal(didalam fungsi)',name)
#global
name = 'Zahra'
lokal()
print('Global(diluar fungsi)',name)

print('============================================')

#lokal
def lokal():
    #variabel lokal
    name='Yaya'
    print('Lokal / global? )',name)
#global
name = 'Zahra'
lokal()
print('Lokal / global? )',name)

print('============================================')

#lokal
def lokal():
    global name
    name = name + 'adalah namaku'
    print(name)
    name = 'ini lokal'
    print(name)
#global
name = 'Zahra'
lokal()
print('ini global',name)

print('============================================')

#deklarasi variabel global
nama = 'zahra'
def lokal1():
    print('percobaan pertama',name)
def lokal2():
    #inisialisasi ulang variabel
    name='yaya'
    print('percobaan ke-2',name)
def lokal3():
    #memanggil variabel global
    global name
    #inisialisasi
print('tess1', name)
lokal1()
print('tess2', name)
lokal2()
print('tess3', name)
lokal3()
print('tess4', name)
