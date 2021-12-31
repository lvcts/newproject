#Tipe data list on program
cake = ['cookies','tart','pie','pudding','brownies']
print(''' 
    Menu
==============
''')
for i in cake:
    print(i)
buy=input("What u would to buy? \n")
buy = buy.lower()
if buy == 'cookies':
    cake.pop(0)
elif buy == 'tart':
    cake.pop(1)
elif buy == 'pie':
    cake.pop(2)   
elif buy == 'pudding':
    cake.pop(3) 
elif buy == 'brownies':
    cake.pop(4) 
else:
    print('Not availble')
print('The rest of the menu : ',cake)