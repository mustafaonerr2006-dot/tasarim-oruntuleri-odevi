class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat


class UrunFabrikasi:
    @staticmethod
    def urun_olustur(ad, fiyat):
        if fiyat < 0:
            print("Ürün fiyatı negatif olamaz")
            fiyat = 0
        return Urun(ad, fiyat)


class SepetUygulamasi:
    def __init__(self):
        self.urunler = []
        self.indirim_turu = "YOK"
        self.indirim_degeri = 0

    def urun_ekle(self, ad, fiyat):
        urun = UrunFabrikasi.urun_olustur(ad, fiyat)
        self.urunler.append(urun)

    def indirim_sec(self, tur, deger):
        self.indirim_turu = tur
        self.indirim_degeri = deger

    def sepeti_yazdir(self):
        toplam = 0

        print("--- Sepet ---")
        for urun in self.urunler:
            print(urun.ad, "-", urun.fiyat, "TL")
            toplam = toplam + urun.fiyat

        print("Ara toplam:", toplam, "TL")

        if self.indirim_turu == "YUZDE":
            toplam = toplam - (toplam * self.indirim_degeri / 100)
            print("Yüzde indirim uygulandı")
        elif self.indirim_turu == "SABIT":
            toplam = toplam - self.indirim_degeri
            print("Sabit indirim uygulandı")
        elif self.indirim_turu == "VIP":
            toplam = toplam * 0.80
            toplam = toplam - 50
            print("VIP indirimi uygulandı")
        elif self.indirim_turu == "SEZON":
            if toplam > 1000:
                toplam = toplam - 150
                print("Sezon indirimi uygulandı")
            else:
                print("Sezon indirimi için tutar yetmedi")
        elif self.indirim_turu == "YOK":
            print("İndirim yok")
        else:
            print("Bilinmeyen indirim türü")

        if toplam < 0:
            toplam = 0

        print("Ödenecek tutar:", toplam, "TL")


if __name__ == "__main__":
    sepet = SepetUygulamasi()
    sepet.urun_ekle("Klavye", 900)
    sepet.urun_ekle("Mouse", 350)
    sepet.urun_ekle("Kulaklık", 700)

    sepet.indirim_sec("SEZON", 0)
    sepet.sepeti_yazdir()
