#function
#fungsi biasa
def fungsi():
    print('ini fungsi biasa')
fungsi()

 
def fungsi1(x, y=17):
    print("x: ", x)
    print("y: ", y)

fungsi1(45)

def kata(kata1, kata2):
    print(kata1, kata2)

kata(kata1='Siti', kata2='Zahra Salma')
kata(kata1='Nurpadila', kata2='Padila')

def func(x):
    x[1] = 9
 
listt = [10, 11, 12, 13, 14, 15]
func(listt)
print(listt)
