nama = input("Masukkan Nama : ")
nim = int(input("Masukkan NIM : "))
pinjaman = int(input("Masukkan jumlah pinjaman : "))
lama_cicilan = int(input("Masukkan lama cicilan dalam tahun (1/2/3) : "))

if lama_cicilan == 1:
        bunga_perbulan = ((0.07)/12)*pinjaman
        total_cicilan = (pinjaman+bunga_perbulan)/12
        print("\n"+nama+" dengan NIM "+str(nim)+" ingin meminjam uang di Bank sebesar Rp."+str(pinjaman)+"\nmaka, total cicilan yang harus dibayar per bulan adalah sebesar Rp."+str(int(total_cicilan))+"\n")
elif lama_cicilan == 2:
        bunga_perbulan = ((0.13)/12)*pinjaman
        total_cicilan = (pinjaman+bunga_perbulan)/24
        print("\n"+nama+" dengan NIM "+str(nim)+" ingin meminjam uang di Bank sebesar Rp."+str(pinjaman)+"\nmaka, total cicilan yang harus dibayar per bulan adalah sebesar Rp."+str(int(total_cicilan))+"\n")
elif lama_cicilan == 3:
        bunga_perbulan = ((0.19)/12)*pinjaman
        total_cicilan = (pinjaman+bunga_perbulan)/36    
        print("\n"+nama+" dengan NIM "+str(nim)+" ingin meminjam uang di Bank sebesar Rp."+str(pinjaman)+"\nmaka, total cicilan yang harus dibayar per bulan adalah sebesar Rp."+str(int(total_cicilan))+"\n")
else :
        print("Mohon masukkan nomor dengan (1/2/3)")