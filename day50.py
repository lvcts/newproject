nama = []
nilai_mid = []
nilai_final = []
hasil=[]
hasil2=[]
hasil_ujian =[]

input_data = int(input('Masukkan jumlah banyak data : '))

for i in range (input_data):
    print(f"Data ke - {i}")
    input_mhs = input('Nama : ')
    nama.append(input_mhs)
    input_mhs1 = int(input('Mid : '))
    nilai1 = input_mhs1*40/100
    hasil.append(nilai1)
    nilai_mid.append(input_mhs1)
    input_mhs2 = int(input('Final : '))
    nilai2 = input_mhs1*60/100
    hasil2.append(nilai2)
    nilai_final.append(input_mhs2)
print('===================================================')
print('No.\t    Nama Siswa\t    Nilai Mid Tes\t Nilai Final\t   Hasil Ujian')
for a in range (input_data):
    hasil_hit = hasil[a] + hasil2[a]
    hasil_ujian.append(hasil_hit)
for x in range (input_data):
    print(x,'\t','\t',nama[x],'\t','\t',nilai_mid[x],'\t','\t',
          nilai_final[x],'\t','\t',hasil_ujian[x])
