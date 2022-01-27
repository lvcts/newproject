#function
#fungsi biasa
def fungsi():
    print('ini fungsi biasa')
fungsi()

 
def fungsi1(x, y=50):
    print("x: ", x)
    print("y: ", y)

fungsi1(45)

def student(kata1, kata2):
    print(kata1, kata2)

student(kata1='Siti', kata2='Zahra Sala=ma')
student(kata1='nurpadila', kata2='padila')

def myFun(x):
    x[0] = 20
 
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)
