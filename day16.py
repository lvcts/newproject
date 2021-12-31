menu=['cake','muffin','cup cake','roll','brownies','donnut']
menu_topping=['matcha','chocolate','taro','red velvet','cheese','tiramisu']
order=[]
topping=[]
pay=[]
pay_topping=[]
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
def program():
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
    if 'cake' in order:
        harga = order.count('cake')*35000
        pay.append(harga)
    elif 'donnut' in order:
        harga = order.count('donnut')*10000
        pay.append(harga)
    elif 'muffin' in order:
        harga = order.count('muffin')*20000
        pay.append(harga)
    elif 'cup cake' in order:
        harga = order.count('cup cake')*20000
        pay.append(harga)
    elif 'roll' in order:
        harga = order.count('roll')*40000
        pay.append(harga)
    elif 'brownies' in order:
        harga = order.count('brownies')*50000
        pay.append(harga)
    harga_order = sum(pay)
    if 'matcha' in topping:
        harga_topping = topping.count('matcha')*5000
        pay_topping.append(harga_topping)
    elif 'chocolate' in topping:
        harga_topping = topping.count('chocolate')*6000
        pay_topping.append(harga_topping)
    elif 'red velvet' in topping:
        harga_topping = topping.count('red velvet')*3000
        pay_topping.append(harga_topping)
    elif 'cheese' in topping:
        harga_topping = topping.count('cheese')*4000
        pay_topping.append(harga_topping)
    elif 'taro' in topping:
        harga_topping = topping.count('taro')*5500
        pay_topping.append(harga_topping)
    elif 'tiramisu' in topping:
        harga_topping = topping.count('tiramisu')*3500
        pay_topping.append(harga_topping)
    harga_total_topping = sum(pay_topping)
    payment = harga_total_topping + harga_order
    print(f'''
    =================PAYMENT===============
    Total bayar : {payment}
    =======================================
    ''')
katalog()
program()

#Belum sempurna, jika memesan lebih dari satu hitunganya salah