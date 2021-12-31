def program1():
    gaji=int(input('Masukkan gaji : \n'))
    if gaji >= 5000000 :
        gaji_bersih = gaji-(gaji*10/100)
    elif gaji >= 3000000 :
        gaji_bersih = gaji-(gaji*5/100)
    else:
        print('Aman')
    print('Gaji anda sebesar : ',gaji_bersih)
def program2():
    jenis_pekerjaan = input('Jenis pekerjaan : ')
    gaji=int(input('Masukkan gaji : '))
    if gaji >= 5000000 :
        if jenis_pekerjaan == 'pns':
            gaji_bersih = gaji-(gaji*15/100)
        else:
            gaji_bersih = gaji-(gaji*10/100)
    elif gaji >= 3000000 :
        if jenis_pekerjaan == 'pns':
            gaji_bersih = gaji-(gaji*10/100)
        else:
            gaji_bersih = gaji-(gaji*5/100)
    elif gaji <= 3000000 and jenis_pekerjaan == 'pns':
        gaji_bersih = gaji-(gaji*5/100)
    else:
        print('Aman')
    print('Gaji anda sebesar : ',gaji_bersih)
program2()