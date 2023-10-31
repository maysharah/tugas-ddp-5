# 1. buatkan program python dgn list dengan nilai (kodekendaraan,namakendaraan,cc,nama)
kendaraan = [12, "Vario", "150cc", "Merah"]
print(kendaraan)

# 2. dari list nomor 1 tambahkan : diakhir tambah harga dan jumlah roda, disisipkan setelah nama kendaraan merk dan jenis kendaraan
kendaraan.append('35 juta')
kendaraan.append('roda dua')
kendaraan.insert(2,"honda")
kendaraan.insert(3,"motor")
print(kendaraan)

# 3. membuat program python dgn match case i= untuk menghitung luas bangun datar
ket = '''selamat datang di applikasi menghitung luas bangun datar
masukkan pilihan : 
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung luas segitiga
'''
print(ket)
pilihan = (input("masukkan pilihan : "))

match pilihan:
    case "1":
        print("menghitung luas persegi")
        sisi = int(input("masukan sisi: "))
        luas = sisi * sisi
        print("luas dari persegi dengan sisi", sisi, "adalah", luas)
    case "2":
        print("menghitung luas lingkaran")
        jari = int(input("masukan jari-jari: "))
        luas = 3.14 * jari * jari
        print("luas dari lingkaran dengan jari", jari, "adalah", luas)
    case "3":
        print("menghitung luas segitiga")
        alas = int(input("masukan alas: "))
        tinggi = int(input("masukan tinggi: "))
        luas = alas * tinggi * 0.5
        print("luas dari segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas)
    case _:
        print("input tidak valid")