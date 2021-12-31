#SET
x={1,2,3,4,5,6}
y={3,6,7,8,9,5,4}
operasi = input('Operasi : ')
operasi=operasi.lower()
if operasi == 'gabungan':
    print('Gabungan himpunan x dan y : ')
    z = x.union(y)
    print(z)
elif operasi == 'irisan':
    print('Irisan himpunan x dan y : ')
    z = x.intersection(y)
    print(z)
elif operasi == 'selisih':
    print('Selisih himpunan x dan y : ')
    z = x.difference(y)
    print(z)
elif operasi == 'komplemen':
    print('Komplemen himpunan x dan y : ')
    z = x.symmetric_difference(y)
    print(z)
else:
    print('Not Found 404')