def cat(*kitten):
    print('My pet name is : ' +  kitten[2])
cat('putih','hitam','orange')

def food(dessert):
    for i in dessert:
        print(i)
cake = ['banana roll', 'pie apple', 'muffin' ]
food(cake)

def cat1(**kitten):
    print('My pet name is : ' +  kitten['name2'])
cat1(name1 = 'putih', name2 = 'hitam')

def trip(country = "Turkey"):
  print("Let's trip to " + country)

trip("Australia")
trip("Japan")
trip()
trip("Korea")