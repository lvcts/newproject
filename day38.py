#any all pada python (and/or)
#any
#any menyimpan prinsip or dimana jika salah satunya true maka akan true
print (any([False, False, False, False]))
print (any([False, True, False, False]))
print (any([True, False, False, False]))

#all
#berbeda dengn any all memiliki turunan sifat dari and yang man jik salah satynya false
#maka false
print (all([True, True, True, True]))
print (all([False, True, True, False]))
print (all([False, False, False]))

print('=================================')
#any dalam list
nomor1 = []
nomor2 = []
  
# index dengan janglauan 1 sampai 10
for i in range(1,11):
    nomor1.append(4*i) 
  
# indeks yang mengakses list 2 dari 0 sampai 9
for i in range(0,10):
    nomor2.append(nomor1[i]%5==0)
  
print('apakah ada bilangan habis dibagi 5 dalam list?')
print(nomor1)
print(nomor2)
print(any(nomor2))


print('=================================') 
list1=[]
list2=[]
  
# semua nomor dlm list 1 aadalah nomor dari 4*i-3
for i  in range(1,21):
    list1.append(4*i-3)
  
# list 2 mengumpulkan jawaban dari wakecho
for i in range(0,20):
    list2.append(list1[i]%2==1)
  
print('apakah ada bilangan ganjil =>')
print(list1)
print(list2)
print(all(list2))
