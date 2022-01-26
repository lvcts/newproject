#Tuple
tuplee = ()
print("Ini tuple :  ")
print(tuplee)

tuplee = ('satu', 'dua', 'tiga')
print("\nTuple dengan string : ")
print(tuplee)

listt = [17,2,2002]
print("\nTuple yang berisikan list ")
print(tuple(listt))

tuple1 = (0, 1, 2, 3)
tuple2 = ('satu', 'dua','tiga')
tuple3 = (tuple1, tuple2)
print("\nMenggabungkan isi tuple :")
print(tuple3)

tuplee = ('SZS',) * 17
print("\nTuple dengan pengulangan : ")
print(tuplee)


tuplee = ('Siti Zahra Salma')
n = 5
print("\nPerulangan tuple")
for i in range(int(n)):
    tuplee = (tuplee)
    print(tuplee)
