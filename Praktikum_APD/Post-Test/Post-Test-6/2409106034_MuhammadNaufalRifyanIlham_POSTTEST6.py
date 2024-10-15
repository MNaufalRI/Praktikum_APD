# Jika Ingin Login Menggunakan Admin :
# Nama = admin
# password = admin1234

salah = 0
salah2 = 0
mark = False
while salah <3 and salah2 <3:
    ulang = False
    if ulang == False and salah <3 and salah2 <3:
        print(
            """
            
            ^                           ^
            =============================
            |          WELCOME          |
            |       MUSEUM OF ART       |
            =============================
            |      1. LOG IN            |
            |      2. REGISTRASI        |
            |      3. KELUAR            |
            ============================= 

            """
            )
        choice = int(input("Answer : "))
        while choice:
            if choice == 1:
                break
            elif choice == 2:
                data_registrasi = {}
                regis = input("Masukkan Nama User : ")
                pwregis = input("Masukkan Password : ")
                data_registrasi[regis] = pwregis
                print("Registrasi berhasil, Silahkan kembali login sebagai User\n")
                break
            elif choice == 3:
                print("Terima Kasih telah mengunjungi Museum of Art")
                exit()
            else :
                print("Opsi tidak diketahui, Silahkan muat ulang")
                exit()

        print(
            """

            ^                           ^
            =============================
            |          WELCOME          |
            |       MUSEUM OF ART       |
            =============================
            |      LOGIN SEBAGAI        |
            |      1. ADMIN             |
            |      2. USER              |
            |      3. KEMBALI           |
            =============================

            """
            )
        login = int(input("Answer :  "))
        program = True
        done = False

        while program and not done:
            if login == 1 and salah <3 :
                nick_admin = "admin"
                pw_admin = "admin1234"
                nick = input("Masukkan Nama : ")
                pw = input("Masukkan Password : ")
                if nick == nick_admin and pw == pw_admin:
                    print("Login Berhasil")
                    print(
            """

            ^                           ^
            =============================
            |      DAFTAR LUKISAN       |
            |       MUSEUM OF ART       |
            =============================
            |      1. TAMBAH DATA       |
            |      2. TAMPILKAN DATA    |
            |      3. UBAH DATA         |
            |      4. HAPUS DATA        |
            |      5. KEMBALI           |
            =============================

            """
            )
              
                    data_lukisan = {}
                    while True:
                        pilih = int(input("\nPilih Opsi : "))

                        if pilih == 1:
                            mark = True
                            nama_lukisan = input("\nTambahkan Nama Lukisan : ")
                            nama_pelukis = input("Tambahkan Nama Pelukis: ")
                            tahun_lukisan = input("Lukisan Di Buat Pada Tahun : ")
                            data_lukisan[nama_lukisan] = {
                                "Pelukis": nama_pelukis,
                                "Tahun": tahun_lukisan
                            }
                            print(f"\nLukisan {nama_lukisan} telah ditambahkan di Museum of Art!")

                        elif pilih == 2:
                            nomor = 1
                            if data_lukisan:
                                for j, k in (data_lukisan.items()):
                                    print(f"\nDaftar Lukisan ke-{nomor} \nNama Lukisan: {j}\nNama Pelukis: {k['Pelukis']}\nTahun Dibuat: {k['Tahun']}")
                                    nomor += 1

                            else:
                                print("Belum ada data lukisan.")

                        elif pilih == 3:
                            nomor = 1
                            for i, j in data_lukisan.items():
                                print(f"\nDaftar Lukisan ke-{nomor}\nNama Lukisan: {i}")
                                nomor += 1
                            ubah_lukisan = input("\nLukisan Mana Yang Mau Di Ubah? : ")
                            if ubah_lukisan in data_lukisan:
                                nama_lukisan_baru = input("\nNama Lukisan Baru : ")
                                nama_pelukis_baru = input("Nama Pelukis Baru : ")
                                tahun_lukisan_baru = input("Memperbarui Tahun Dibuat : ")
                                data_lukisan[nama_lukisan_baru] = {
                                    "Pelukis": nama_pelukis_baru,
                                    "Tahun": tahun_lukisan_baru
                                }
                                print(f"\nLukisan {ubah_lukisan} telah di ubah menjadi Lukisan {nama_lukisan_baru}")
                            else:
                                print("Lukisan tidak ditemukan")

                        elif pilih == 4:
                            nomor = 1
                            for i, j in data_lukisan.items():
                                print(f"\nDaftar Lukisan ke-{nomor}\nNama Lukisan: {i}")
                                nomor += 1
                            hapus_lukisan = input("\nPilih Lukisan Mana Yang Ingin Dihapus : ")
                            if hapus_lukisan in data_lukisan:
                                del data_lukisan[hapus_lukisan]
                                print(f"\nLukisan '{hapus_lukisan}' berhasil dihapus")
                            else:
                                print("Lukisan tidak ditemukan")

                        elif pilih == 5:
                            done = True
                            break
                        else:
                            print("Anda Salah Input")
                            continue
                else:
                    print("Login Tidak Berhasil")
                    salah += 1
                    continue
            elif login == 2 and not done and salah2 < 3:
                nickn = input("Masukkan Nama User : ")
                pwuser = input("Masukkan Password : ")
                if nickn in data_registrasi and data_registrasi[nickn] == pwuser:
                    print(f"Selamat datang {nickn}!")
                    done = False
                    print(
                """

                ^                               ^
                =================================
                |         DAFTAR LUKISAN        |
                |         MUSEUM OF ART         |
                =================================
                |      1. TAMPILKAN LUKISAN     |
                |      2. KEMBALI               |
                =================================

                """
                )


                    while True:
                        pilih2 = int(input("\nPilih Opsi : "))
                        if pilih2 == 1:
                            if mark:
                                nomor = 1
                                for i, j in data_lukisan.items():
                                    print(f"\nDaftar Lukisan ke-{nomor}\nNama Lukisan: {i}\nNama Pelukis: {j['Pelukis']}\nTahun Dibuat: {j['Tahun']}")
                                    nomor += 1
                            else:
                                print("Lukisan Kosong")
                        elif pilih2 == 2:
                            done = True
                            break
                        else:
                            print("Opsi Invalid")
                            continue
                else:
                    print("Nickname atau Password salah")
                    salah2 += 1
                    continue
            elif login == 3:
                done = True
                break

            elif login == 1 and salah == 3 or login == 2 and salah2 == 3:
                print("Anda Kena Ban")
                exit()
                
            else:
                print("Opsi Tidak diketahui")
                break
    elif ulang == True:
        continue