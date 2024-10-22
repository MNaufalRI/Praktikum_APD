# Jika Ingin Login Menggunakan Admin :
# Nama = admin
# password = admin1234

done = True
data_registrasi = {}
def menu1():
    return (
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

def menu2():
    return (
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

def menu3_admin():
    return (
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

def menu4_user():
    return (
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

def pilihan_menu1_registrasi(choice):
    while choice:
            if choice == 1:
                        break
            elif choice == 2:
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

def login_gagal():
      print("Login Tidak Berhasil")

def ban():
      print("Anda kena ban")
      exit()

def login_berhasil_admin():
        print("Login Berhasil")
        print(menu3_admin())

def login_admin(salah):
        while program:
            if salah <3 :
                nick_admin = "admin"
                pw_admin = "admin1234"
                nick = input("Masukkan Nama : ")
                pw = input("Masukkan Password : ")
                if nick == nick_admin and pw == pw_admin:
                    login_berhasil_admin()
                    break
                else :
                    login_gagal(salah)
                    salah += 1
                    continue
            else:
                ban()

def login_user_berhasil(nickn):
    print(f"Selamat datang {nickn}!")
    done = False
    print(menu4_user())

def login_user(salah2):
    while program :
        if salah2 < 3 :
            nickn = input("Masukkan Nama User : ")
            pwuser = input("Masukkan Password : ")
            if nickn in data_registrasi and data_registrasi[nickn] == pwuser:
                login_user_berhasil(nickn)
                break
            else:
                login_gagal()
                salah2 += 1
                continue
        else :
             ban()


def tambah_data():
    nama_lukisan = input("\nTambahkan Nama Lukisan : ")
    nama_pelukis = input("Tambahkan Nama Pelukis: ")
    tahun_lukisan = input("Lukisan Di Buat Pada Tahun : ")
    data_lukisan[(nama_lukisan)] = {
        "Pelukis": nama_pelukis,
        "Tahun": tahun_lukisan
    }
    print(f"\nLukisan {nama_lukisan} telah ditambahkan di Museum of Art!")

def tampilkan_data():
    nomor = 1
    if data_lukisan:
        for j, k in (data_lukisan.items()):
            print(f"\nDaftar Lukisan ke-{nomor} \nNama Lukisan: {j}\nNama Pelukis: {k['Pelukis']}\nTahun Dibuat: {k['Tahun']}")
            nomor += 1

    else:
        print("Belum ada data lukisan.") 

def tampilkan_nama():
     nomor = 1
     for i, j in data_lukisan.items():
          print(f"\nDaftar Lukisan ke-{nomor}\nNama Lukisan: {i}")
          nomor += 1

def ubah_data():
    tampilkan_nama()
    ubah_lukisan = input("\nLukisan Mana Yang Mau Di Ubah? : ")
    if ubah_lukisan in data_lukisan:
        del data_lukisan[ubah_lukisan]
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

def hapus_data():
        tampilkan_nama()
        hapus_lukisan = input("\nPilih Lukisan Mana Yang Ingin Dihapus : ")
        if hapus_lukisan in data_lukisan:
            del data_lukisan[hapus_lukisan]
            print(f"\nLukisan '{hapus_lukisan}' berhasil dihapus")
        else:
            print("Lukisan tidak ditemukan")

salah = 0
salah2 = 0
mark = False
while salah <3 and salah2 <3:
    ulang = False
    if ulang == False and salah <3 and salah2 <3:
        print(menu1())
        try:
            choice = int(input("Answer : "))
        except:
            print("Input yang anda masukkan bukan angka!")
            continue
        pilihan_menu1_registrasi(choice)
        print(menu2())
        try:
            login = int(input("Answer :  "))
            program = True
            done = False
        except:
            print("Input yang anda masukkan bukan angka!")
            continue

        while program and not done:
            salah = 0
            salah2 = 0
            if login == 1 and salah < 3:
                login_admin(salah)
                data_lukisan = {}
                while True:
                    try:
                        pilih = int(input("\nPilih Opsi : "))

                        if pilih == 1:
                            tambah_data()
                            mark = True

                        elif pilih == 2:
                            tampilkan_data()

                        elif pilih == 3:
                            ubah_data()

                        elif pilih == 4:
                            hapus_data()

                        elif pilih == 5:
                            done = True
                            break
                        else:
                            print("Anda Salah Input")
                            continue
                    except:
                        print("Input yang anda masukkan bukan angka!")
                        continue

            elif login == 2 and not done and salah2 < 3:
                    login_user(salah2)
                    while True:
                        try :
                            pilih2 = int(input("\nPilih Opsi : "))
                        except:
                            print("Input yang anda masukkan bukan angka!")
                            continue
                        if pilih2 == 1:
                            if mark:
                                tampilkan_data()
                            else:
                                print("Lukisan Kosong")
                        elif pilih2 == 2:
                            done = True
                            break
                        else:
                            print("Opsi Invalid")
                            continue
            elif login == 3:
                done = True
                break

            elif login == 1 and salah == 3 or login == 2 and salah2 == 3:
                ban()     
            else:
                print("Opsi Tidak diketahui")
                break
    elif ulang == True:
        continue