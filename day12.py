menu=['cake','muffin','cup cake','roll','brownies','donnut']
menu_topping=['matcha','chocolate','taro','red velvet','cheese','tiramisu']
order=[]
topping=[]
def katalog():
    print('''
    ===============KATALOG===============
    CAKE        MUFFIN          CUP CAKE
    ROLL        BROWNIES        DONNUT
    ================TOPPING============== 
    MATCHA      CHOCOLATE       TARO
    RED VELVET      CHEESE      TIRAMISU
    ===================================== 

    ''')

katalog()
jumlah = int(input('Jumlah : '))
for i in range(0,jumlah):
    i=input('Order : ')
    i=i.lower()
    if i in menu:
        order.append(i)
    else:
        break    
for j in range(0,jumlah):
    j=input('Topping : ')
    j=j.lower()
    if j in menu_topping:
        topping.append(j)
    else:
        break 
print('Pesanan anda : \n',order)
print('Topping : \n',topping)