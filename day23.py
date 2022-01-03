kalimat = input('Masukkan kalimat yang akan disusun : ')
kata = [kataa.lower() for kataa in kalimat.split()]
kata.sort()
print('Hasil : ')
for kataa in kata :
    print(kataa)