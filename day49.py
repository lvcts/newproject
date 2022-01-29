nama = []
nilai_mid = []
nilai_final = []

input_data = int(input('Masukkan jumlah banyak data : '))

for i in range (input_data):
    print(f"Data ke - {i}")
    input_mhs = input('Nama : ')
    nama.append(input_mhs)
    input_mhs1 = int(input('Mid : '))
    nilai_mid.append(input_mhs1)
    input_mhs2 = int(input('Final : '))
    nilai_final.append(input_mhs2)

    print(nama)
    print(nilai_mid)
    print(nilai_final)
