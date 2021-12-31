def angka(batas, i=1):
    if (i< batas):
        angka(batas, i + 1)
    print(f'Perulangan ke {i}')
angka()
