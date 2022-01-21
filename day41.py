#list part 2
#mengakses elemen list
def a():
    List = ["kucing", "ku", "sakit"]
    print("Mengakses elemen list")
    print(List[0])
    print(List[2])
     
    # list multi-dimensional
    List = [['kucing', 'makan'], ['ikan']]
    print("mengakses elemen list dari list multi-dimensional")
    print(List[0][1])
    print(List[1][0])

#list index negatif
def b():
    List = [1,2,3,'kucing','makan',4,'ikan']
    print("list index negatif")
    print(List[-1])
    print(List[-4])
#menghapus elemen dari list
def c():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print("List : ")
    print(List)
    #menghapus elemen list
    List.remove(3)
    List.remove(6)
    print("\nList setelah dilakukan remove: ")
    print(List)
    #menghapus elemen list menggunalan perulangan
    for i in range(1, 3):
        List.remove(i)
    print("\nList setelah dilakukan remove menggunakan perulangan: ")
    print(List)
#pop() pada list
def d():
    List = [11,12,13,14,15,'winter','january']
    print(List)
    List.pop()
    print("\nList setelah dilakukan pop():")
    print(List)
    List.pop(2)
    print("\nList setelah dilakukan pop() secara spesifik: ")
    print(List)
a()
print('======================================')
b()
print('======================================')
c()
print('======================================')
d()
