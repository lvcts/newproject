#jenis input

""" input dari console di python """
var = int(input('Input : '))
var += 10
print(var)

''' multiple input menggunakan split()'''
var1, var2 = input('masukkan 2 variabel : ').split()
print('variabel 1 berisi : ',var1)
print('variabel 2 berisi : ',var2)
print('isi pertama adalah {} dan yang kedua adalah {}'.format(var1,var2))

''' multiple input  menggunakan fungsi list()'''
var3 = list(map(int,input('isi : ').split()))
print('listnya adalah : ', var3)

''' multiple input  menggunakan list()'''
var1, var2 = [int (var1) for var1 in input('masukkan hasil').split()]
print('angka pertama :',var1)
print('angka kedua :',var2)
print('angka pertama adalah {} dan angka kedua adalah {}'.format(var1,var2))