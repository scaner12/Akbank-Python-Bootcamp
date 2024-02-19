class Kütüphane:
    def __init__(self):
        self.dosya = open("kitaplar.txt", "a+")

    def __del__(self):
        self.dosya.close()

    def kitaplarıListele(self):
        self.dosya.seek(0)
        satırlar = [i.strip() for i in self.dosya.readlines()]
        for satır in satırlar:
            print(satır)

    def kitapEkle(self):
        başlık = input("Başlık: ")
        yazar = input("Yazar: ")
        yayınYılı = input("Yayın yılı: ")
        sayfaSayısı = input("Sayfa sayısı: ")
        bilgi = başlık + "," + yazar + "," + yayınYılı + "," + sayfaSayısı
        self.dosya.write(bilgi + "\n")
        self.dosya.flush()

    def kitapSil(self):
        başlık = input("Silmek istediğiniz kitabın başlığını girin: ")
        satırlar = [i.strip() for i in self.dosya.readlines()]
        başlıklar = [i.split(",")[0] for i in satırlar]

        if başlık in başlıklar:
            silinecekIndex = başlıklar.index(başlık)
            del satırlar[silinecekIndex]

            self.dosya.seek(0)
            self.dosya.truncate()

            for satır in satırlar:
                self.dosya.write(satır + "\n")
            self.dosya.flush()
            print(f"{başlık} başlıklı kitap silindi.")
        else:
            print(f"'{başlık}' başlıklı kitap bulunamadı.")

# Kodun geri kalanı aynı kalır

kütüphane = Kütüphane()

while True:
    print("*** MENÜ ***\n1) Kitapları Listele\n2) Kitap Ekle\n3) Kitap Sil\n4) Çıkış")
    seçim = input("Lütfen seçiminizi girin: ")
    if seçim == "1":
        kütüphane.kitaplarıListele()
    elif seçim == "2":
        kütüphane.kitapEkle()
    elif seçim == "3":
        kütüphane.kitapSil()
    elif seçim == "4":
        sys.exit()
    else:
        print("Lütfen doğru bir seçenek girin")
