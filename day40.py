#List
def a():
    List = [0, 1, 2, 2, 3, 3, 4, 5, 6, 7]
    print("\nList yang berisi angka: ")
    print(List)
    
    List = [1, 2, 3, 'apel', 4, 'anggur']
    print("\nList yang berisi angka dan string ")
    print(List)

#Panjang list
def b():
    List1 = []
    print(len(List1))
     
    List2 = [0, 1, 2, 2, 3, 3, 4, 5, 6, 7]
    print(len(List2))

#menambahkan elemen pada list
def c():
    List = []
    print("List ini berisi : ")
    print(List)

    #menambahkan elemen pada list
    List.append(2)
    List.append(4)
    List.append(6)
    print("\nList setelah ditambahkan 3 element: ")
    print(List)
     
    #menambahkan elemen pada list menggunakan perulangan
    for i in range(1, 4):
        List.append(i)
    print("\nList setelah ditambahkan 3 element menggunakan perulangan: ")
    print(List)
     
    #menambahkan tuple pada list
    List.append((3, 5))
    print("\nList setelah ditambahkan tuple: ")
    print(List)
     
    #menambahkan list kedalam list
    List2 = ['kucing', 'kipas']
    List.append(List2)
    print("\nList setelah ditambahkan list: ")
    print(List)
#menggunakan insert()
def d():
    List = [1,2,3,4]
    print("List ini berisi: ")
    print(List)

    List.insert(1, 2)
    List.insert(0, 'HI')
    print("\nList setelah menggunakan insert(): ")
    print(List)
a()
print('============================')
b()
print('============================')
c()
print('============================')
d()


