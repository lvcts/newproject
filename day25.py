import random

waktu = random.randrange(0,24)
jarak = int(input('Jarak in km : '))
kecepatan = jarak/waktu
print(f'Jarak : {jarak}')
print(f'Waktu : {waktu}')
print(f'Kecepatan : {kecepatan} km/jam')
if kecepatan >= 180 :
    print('bahaya')
elif kecepatan >= 120 :
    print('pelan-pelan')
elif kecepatan >= 80 :
    print('sans')
else:
    print('lambat')