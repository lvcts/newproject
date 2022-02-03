#latihan array lage
buku_A = ['A','Novel','Airin','Pernah ada','30000']
buku_B = ['B','Cerita','Ayunindi','Meluakan segalanya','40000']
print('\t\t\tDaftar Harga Buku')
print('====================================================')
jumlah = 2
for x in range(jumlah):
    print('No \t Kode Buku \t Jenis buku \t Penulis \t Judul buku \t Harga')
    print(x,'\t','\t',buku_A[x],'\t','\t',buku_A[x+1],'\t','\t',buku_A[x+2],'\t','\t',buku_A[x+3])
    print(x,'\t','\t',buku_B[x],'\t','\t',buku_B[x+1],'\t','\t',buku_B[x+2],'\t','\t',buku_B[x+3])
