tb = float (input ("Masukkan tinggi dalam meter:"))
bb = float (input ("Masukkan berat dalam kg:"))


bmi = bb / (tb ** 2)

print ("BMI anda ialah: {0} dan anda adalah:" .format (bmi), end = " ")

if (bmi <16):
   print ("Kurus BgT")

elif (bmi>= 16 and bmi <18.5):
   print ("Kusur dikir")

elif (bmi>= 18.5 and bmi <25):
   print ("Sehat")

elif (bmi>= 25 and bmi <30):
   print ("Mulai obesitas")

elif (bmi>= 30):
    print ("Obesitas")
