#list part 3
List = ['S','I','T','I','Z','A','H','R','A',
        'S','A','L','M','A']
print("CETAK ISI LIST ")
print(List)

#print elemen menggunakan slicing
list_slicing = List[2:7]
print("\nMelakukan metode slicing elemen 2-7: ")
print(list_slicing)

#print elemen menggunakan slicing dari nilai penentu hingga akhir
list_slicing = List[3:]
print("\nMelakukan metode slicing elemen dari 3 : ")
print(list_slicing)

#print elemen menggunakan slicing dari awal hingga akhir
list_slicing = List[:]
print("\nMelakukan metode slicing elemen untuk semua: ")
print(list_slicing)

#print elemen menggunakan slicing negative
list_slicing = List[-5:-1]
print("\nMelakukan metode slicing elemen -5 hingga -1 :")
print(list_slicing)

list_slicing = List[:-1]
print("\nMelakukan metode slicing elemen -1")
print(list_slicing)
#sepertinya membalik hasil
list_slicing = List[::-1]
print("\nMelakukan metode slicing elemen -1 ::")
print(list_slicing)
