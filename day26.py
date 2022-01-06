list_nilai = list(range(0,101))
mtk = int(input('MTK : '))
b_ing = int(input('B. Ing : '))
b_indo = int(input('B. Indo : '))
if mtk in list_nilai :
    if b_indo and b_ing in list_nilai:
        skor = (mtk + b_ing + b_indo)/3
        if skor > 70 :
            print('Anda bebas memilih yang disukai')
        elif skor == 70 :
            print(f'Skor anda adalah {skor}, anda dinyatakan lolos ke bidang berikutny ')
            minat = input('Minat : ')
            if minat == 1 :
                print('Teknik Elektro')
            elif minat == 2 :
                print('Teknik Mesin')
            else :
                print('Bidang Pariwisata')
        else : 
            print(f'Anda dinyatakan tidak lolos karena skor anda adalah {skor}')
else:
    exit