nomor = int(input("Enter a number: "))
menu = False
if nomor > 1:
    for i in range(2, nomor):
        if (nomor % i) == 0:
            menu = True
            break
if menu:
    print(nomor, "bukan bilangan prima")
else:
    print(nomor, "adalah bilangan prima")
