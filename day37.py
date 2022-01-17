#operator perbandingan

a=11
b=12
#hasil = a jika a<b selain itu maka b
hasil = a if a < b else b
print(hasil)

#operator perbandingan pada tuple,dictionary
a=20
b=30

'''untuk tuple
penggunaan (test False,test True)[test]
jika [a<b] adalah true yang akan mengembalikan nilai 1,
jadi elemen dengan indeks 1 akan di cetak
else [a<b] adalah false maka akan mengembalikan nulai 0,
jadi elemen dengan indeks 0 akan dicetak'''
print((b,a)[a<b])

a=40
b=30
'''untuk dictionary
jika[a<b] adalah true maka hasil dari true akan tercetak
jika [a<b] adalah false maka hasil dari false akan tercetak'''
print({True:a, False: b}[a<b])

#operator perbandingan pada nested if-else
a, b = 20, 20


'''untuk penulisannya [statemen benar] if [kondisi] else [statemen salah]'''
print ("a dan b sama" if a == b else "a lebih besar dibanding b"
        if a > b else "b lebih besar dibanding a")

#atau dapat juga ditulis seperti
a, b = 20, 10

if a != b:
    if a > b:
        print("a lebih besar dibanding b")
    else:
        print("b lebih besar dibanding a")
else:
    print("a dan b sama")
