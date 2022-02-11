def segitiga(a,t):
   luas=(1/2)*a*t
   return luas

a = float(input("Masukan Panjang : "))
t = float(input("Masukan Lebar : "))
print("Luas Persegi :",segitiga(a,t))

#variabel global
print('==========================')
x=5
def change():
   x=10
   return x
change()
print(x)
print('==========================')
def change1():
   global x#untuk mengakses variabel global
   x = 10
   return x
change1()
print(x)
