#membuat fungsi
def bmi(bb,tb):
    indeks_bmi = bb/(tb*tb)
    print('BMI anda adalah : ',indeks_bmi)
bmi(50,155)

def bmi2(bb2,tb2):
    indeks_bmi = bb2/(tb2*tb2)
    print('BMI anda adalah : ',indeks_bmi)
    return indeks_bmi
bmi2(50,155)