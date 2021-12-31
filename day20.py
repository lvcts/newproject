def luas_lingkaran(r):
    pi = 3.14
    return pi * (r*r);
def luas_segitiga(a,t):
    rumus = 0.5 
    return rumus*a*t;
def luas_persegi_panjang(p,l):
    return p*l;
def luas_persegi(s):
    return s*s;
print('Luas lingkaran = %.1f ' % luas_lingkaran(5))
print('Luas segitiga = %.1f ' % luas_segitiga(5,10))
print('Luas persegi pnjang = %.1f ' % luas_persegi_panjang(5,10))
print('Luas persegi = %.1f ' % luas_persegi(10))