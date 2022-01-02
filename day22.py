def penjumlahan(x, y):
    return x + y
def pengurangan(x, y):
    return x - y
def perkalian(x, y):
    return x * y
def pembagian(x, y):
    return x / y


print("Pilih operasi")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")

while True:
    pilihan = input("Masukkan pilihan : ")
    if pilihan in ('1', '2', '3', '4'):
        num1 = float(input("Angka 1 : "))
        num2 = float(input("Angka 2 : "))

        if pilihan == '1':
            print(num1, "+", num2, "=", penjumlahan(num1, num2))

        elif pilihan == '2':
            print(num1, "-", num2, "=", pengurangan(num1, num2))

        elif pilihan == '3':
            print(num1, "*", num2, "=", perkalian(num1, num2))

        elif pilihan == '4':
            print(num1, "/", num2, "=", pembagian(num1, num2))

        menu = input("Lagi ?(y/t) ")
        menu=menu.lower()
        if menu == "y":
            True
        elif menu == "t":
            break
        else:
            print('Invalid input')
            break
    
    else:
        print("Invalid Input")
        break