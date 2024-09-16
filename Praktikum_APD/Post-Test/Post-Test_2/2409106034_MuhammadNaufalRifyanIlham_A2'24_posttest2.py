print("\nSelamat datang di toko beras!\nSilahkan masukkan data berikut\n")
nama = input("Mohon masukkan namamu : ")
nim = int(input("Masukkan NIM : "))
harga_beras = int(input("Masukkan harga beras yang ingin dibeli : "))
print("\n" + nama + " dengan NIM " + str(nim) + " ingin membeli beras seharga RP." + str(harga_beras))

mawar1 = float((harga_beras)*(0.11))
mawar2 = int(harga_beras-mawar1)

sania1 = float(harga_beras*(0.14))
sania2 = int(harga_beras-sania1)

maknyus1 = float(harga_beras*(0.17))
maknyus2 = int(harga_beras-maknyus1)

print("Jika dia membeli beras Mawar ia harus membayar Rp."+str(mawar2)+" setelah mendapat diskon 11%.")
print("Jika dia membeli beras Sania ia harus membayar Rp."+str(sania2)+" setelah mendapat diskon 14%.")
print("Jika dia membeli beras Maknyus ia harus membayar Rp."+str(maknyus2)+" setelah mendapat diskon 17%.")