#output
#print() function
print('aku mau makan')

makan='roti'
print('aku mau makan ',makan)

print('aku',end='')
print('mau makan')

print('aku','mau','makan',sep='')

#try something new
import time
 
waktu = 5
for i in reversed(range(waktu + 1)):
    if i > 0:
        print(i, end='>>>', flush = True)
        time.sleep(1)
    else:
        print('\n')

loading = 10
print('Loading procces : ')
for i in reversed(range(loading + 1)):
    if i > 0:
        print(end='===', flush = True)
        time.sleep(1)
    else:
        print('Makannnnn')