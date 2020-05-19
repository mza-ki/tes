def bangunDatar():
    print("1. Persegi Panjang")
    print("2. Persegi")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Trapesium")
    print("6. Layang-Layang")
    print("7. Belah Ketupat")
    print("")
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        print("1. Keliling")
        print("2. Luas")
        print("")
        mencari = int(input("Masukkan pilihan anda : "))
        print("")
        if mencari == 1:
            panjang = int(input("masukkan panjang : "))
            lebar = int(input("masukkan lebar : "))
            keliling = 2 * (panjang + lebar)
            print("keliling persegi panjang", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            panjang = int(input("masukkan panjang : "))
            lebar = int(input("masukkan lebar : "))
            luas = panjang * lebar
            print("luas persegi panjang : ", luas)
            print("terima kasih telah berkunjung")
        else:
            print("mohon masukkan sesuai pilihan")

    elif pilihan == 2:
        print("1. Keliling")
        print("2. Luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            sisi = int(input("masukkan sisi : "))
            keliling = 4 * sisi
            print("keliling persegi anda adalah", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            sisi = int(input("masukkan sisi : "))
            luas = sisi * sisi
            print("luas persegi anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 3:
        print("1. keliling")
        print("2. luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:
            sisi_a = int(input("masukkan sisi pertama : "))
            sisi_b = int(input("masukkan sisi kedua : "))
            sisi_c = int(input("masukkan sisi ketiga : "))
            keliling = (sisi_a + sisi_b) + (sisi_b + sisi_c) + (sisi_a + sisi_c)
            print("Keliling segitiga anda adalah", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            alas = float(input("masukkan alas : "))
            tinggi = float(input("masukkan tinggi : "))
            luas = 0.5 * alas * tinggi
            print("luas segitiga anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")
    elif pilihan == 4:
        print("1. Keliling")
        print("2. luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:
            sisi_a = int(input("masukkan sisi pertama : "))
            sisi_b = int(input("masukkan sisi kedua : "))
            sisi_c = int(input("masukkan sisi ketiga : "))
            sisi_d = int(input("masukkan sisi keempat : "))
            keliling = (sisi_a + sisi_b) + (sisi_b + sisi_c) + (sisi_c + sisi_d) + (sisi_a + sisi_d)
            print("keliling jajar genjang anda adalah ", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            alas = int(input("masukkan alas : "))
            tinggi = int(input("masukkan tinggi : "))
            luas = alas * tinggi
            print("luas jajar genjang anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 5:
        print("1. keliling")
        print("2. luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:
            sisi_a = int(input("masukkan sisi pertama : "))
            sisi_b = int(input("masukkan sisi kedua : "))
            sisi_c = int(input("masukkan sisi ketiga : "))
            sisi_d = int(input("masukkan sisi keempat : "))
            keliling = (sisi_a + sisi_b) + (sisi_b + sisi_c) + (sisi_c + sisi_d) + (sisi_a + sisi_d)
            print("keliling trapesium anda adalah ", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            sisi_sejajar = int(input("masukkan jumlah sisi sejajar : "))
            tinggi = int(input("masukkan tinggi : "))
            luas = 1 / 2 * sisi_sejajar * tinggi
            print("luas trapesium anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 6:
        print("1. keliling")
        print("2. luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:
            sisi_a = int(input("masukkan sisi pertama : "))
            sisi_b = int(input("masukkan sisi kedua : "))
            sisi_c = int(input("masukkan sisi ketiga : "))
            keliling = 2 * ((sisi_a * sisi_b) + (sisi_b * sisi_c))
            print("keliling layang-layang anda adalah ", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            diagonal1 = int(input("masukkan diagonal 1 : "))
            diagonal2 = int(input("masukkan diagonal 2 : "))
            luas = 1 / 2 * diagonal1 * diagonal2
            print("luas layang-layang anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 7:
        print("1. keliling")
        print("2. luas")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:
            sisi = int(input("masukkan sisi : "))
            keliling = 4 * sisi
            print("keliling belah ketupat anda adalah ", keliling)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            diagonal1 = int(input("masukkan diagonal 1 : "))
            diagonal2 = int(input("masukkan diagonal 2 : "))
            luas = 1 / 2 * diagonal1 * diagonal2
            print("luas belah ketupat anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    else:
        print("masukkan pilihan sesuai yang disediakan")


def bangunRuang():
    print("1. Kubus")
    print("2. Balok")
    print("3. Limas")
    print("4. Prisma")
    print("5. Tabung")
    print("6. Kerucut")
    print("7. Bola")
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        print("1. volume")
        print("2. Luas Permukaan")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            sisi = int(input("masukkan sisi : "))
            volume = sisi ** 3
            print("volume kubus anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            sisi = int(input("masukkan sisi : "))
            luas = 6 * sisi ** 2
            print("luas permukaan balok anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 2:
        print("1. volume")
        print("2. Luas Permukaan")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            panjang = int(input("masukkan panjang : "))
            lebar = int(input("masukkan lebar : "))
            tinggi = int(input("masukkan tinggi : "))
            volume = panjang * lebar * tinggi
            print("volume kubus anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            panjang = int(input("masukkan panjang : "))
            lebar = int(input("masukkan lebar : "))
            tinggi = int(input("masukkan tinggi : "))
            luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
            print("luas permukaan kubus anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 3:
        print("1. volume")
        print("2. Luas Permukaan")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            luasAlas = int(input("masukkan luas alas : "))
            tinggi = int(input("masukkan tinggi : "))
            volume = 1 / 3 * luasAlas * tinggi
            print("volume limas anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            luasAlas = int(input("masukkan luas alas : "))
            jumlahSegitiga = int(input("masukkan jumlah luas segitiga pada bidang tegak : "))
            luas = luasAlas + jumlahSegitiga
            print("luas permukaan limas anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 4:
        print("1. volume")
        print("2. Luas Permukaan")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            luasALas = int(input("masukkan luas alas : "))
            tinggi = int(input("masukkan tinggi : "))
            volume = luasALas * tinggi
            print("volume kubus anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            luasALas = int(input("masukkan luas alas : "))
            tinggi = int(input("masukkan tinggi : "))
            kelilingLuas = int(input("masukkan keliling luas : "))
            luas = (2 * luasALas) + (kelilingLuas * tinggi)
            print("luas permukaan kubus anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 5:
        print("1. volume")
        print("2. Luas Permukaan")
        print("3. Luas Selimut")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            jari = int(input("masukkan jari-jari : "))
            tinggi = int(input("masukkan tinggi : "))
            volume = 22 / 7 * jari ** 2 * tinggi
            print("volume tabung anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            jari = int(input("masukkan jari-jari : "))
            tinggi = int(input("masukkan tinggi : "))
            luas = 2 * 22 / 7 * jari * (jari + tinggi)
            print("luas permukaan tabung anda adalah", luas)
            print("terima kasih telah berkunjung")
        elif mencari == 3:
            jari = int(input("masukkan jari-jari : "))
            tinggi = int(input("masukkan tinggi : "))
            luas = 2 * 22 / 7 * jari * tinggi
            print("luas selimut tabung anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 6:
        print("1. volume")
        print("2. Luas Permukaan")
        print("3. Luas Selimut")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            jari = int(input("masukkan jari-jari : "))
            tinggi = int(input("masukkan tinggi : "))
            volume = 1 / 3 * 22 / 7 * jari ** 2 * tinggi
            print("volume kerucut anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            jari = int(input("masukkan jari-jari : "))
            panjangGaris = int(input("masukkan panjang garis pelukis kerucut : "))
            luas = 22 / 7 * jari * (jari + panjangGaris)
            print("luas permukaan kerucut anda adalah", luas)
            print("terima kasih telah berkunjung")
        elif mencari == 3:
            jari = int(input("masukkan jari-jari : "))
            panjangGaris = int(input("masukkan panjang garis pelukis kerucut : "))
            luas = 22 / 7 * jari * panjangGaris
            print("luas selimut kerucut anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    elif pilihan == 7:
        print("1. volume")
        print("2. Luas Permukaan")
        print("")
        mencari = int(input("masukkan pilihan anda : "))
        if mencari == 1:  # keliling
            jari = int(input("masukkan jari-jari : "))
            volume = 4 / 3 * 22 / 7 * jari ** 3
            print("volume kubus anda adalah", volume)
            print("terima kasih telah berkunjung")
        elif mencari == 2:
            jari = int(input("masukkan jari-jari : "))
            luas = 4 * 22 / 7 * jari ** 2
            print("luas permukaan balok anda adalah", luas)
            print("terima kasih telah berkunjung")
        else:
            print("terima kasih telah berkunjung")

    else:
        print("masukkan pilihan sesuai yang disediakan")


def lagi():
    print("masukkan pilihan kategori pencarian anda")
    print("1. Bangun Datar")
    print("2. Bangun Ruang")
    print("")
    userInput = int(input("Masukkan pilihan anda : "))
    if userInput == 1:
        bangunDatar()
    elif userInput == 2:
        bangunRuang()
    else:
        print("masukkan lah sesuai input yang tersedia")


lagi()

print("")
lanjut = str(input("mau mencoba lagi(y/n) : "))
if lanjut == "y":
    lagi()
else:
    print("makasih telah berkunjung")

