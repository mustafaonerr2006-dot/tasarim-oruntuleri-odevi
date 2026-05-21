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

    def urun_ekle(self, ad, fiyat):
        urun = UrunFabrikasi.urun_olustur(ad, fiyat)
        self.urunler.append(urun)

    def urunleri_yazdir(self):
        print("--- Sepet ---")
        for urun in self.urunler:
            print(urun.ad, "-", urun.fiyat, "TL")

    def toplam_hesapla(self):
        toplam = 0
        for urun in self.urunler:
            toplam = toplam + urun.fiyat
        return toplam


class SepetTutari:
    def __init__(self, sepet):
        self.sepet = sepet

    def toplam_hesapla(self):
        return self.sepet.toplam_hesapla()


class TutarDecorator:
    def __init__(self, hesaplayici):
        self.hesaplayici = hesaplayici

    def toplam_hesapla(self):
        return self.hesaplayici.toplam_hesapla()


class YuzdeIndirimDecorator(TutarDecorator):
    def __init__(self, hesaplayici, yuzde):
        super().__init__(hesaplayici)
        self.yuzde = yuzde

    def toplam_hesapla(self):
        toplam = self.hesaplayici.toplam_hesapla()
        return toplam - (toplam * self.yuzde / 100)


class SabitIndirimDecorator(TutarDecorator):
    def __init__(self, hesaplayici, miktar):
        super().__init__(hesaplayici)
        self.miktar = miktar

    def toplam_hesapla(self):
        toplam = self.hesaplayici.toplam_hesapla() - self.miktar
        if toplam < 0:
            toplam = 0
        return toplam


class HediyePaketiDecorator(TutarDecorator):
    def __init__(self, hesaplayici):
        super().__init__(hesaplayici)

    def toplam_hesapla(self):
        return self.hesaplayici.toplam_hesapla() + 40


class SepetFacade:
    def __init__(self):
        self.sepet = SepetUygulamasi()

    def urun_ekle(self, ad, fiyat):
        self.sepet.urun_ekle(ad, fiyat)

    def normal_sepet_yazdir(self):
        hesaplayici = SepetTutari(self.sepet)
        self.yazdir(hesaplayici)

    def sezon_indirimli_yazdir(self):
        hesaplayici = SepetTutari(self.sepet)
        if hesaplayici.toplam_hesapla() > 1000:
            hesaplayici = SabitIndirimDecorator(hesaplayici, 150)
        self.yazdir(hesaplayici)

    def vip_sepet_yazdir(self):
        hesaplayici = SepetTutari(self.sepet)
        hesaplayici = YuzdeIndirimDecorator(hesaplayici, 20)
        hesaplayici = SabitIndirimDecorator(hesaplayici, 50)
        self.yazdir(hesaplayici)

    def hediye_paketli_yazdir(self):
        hesaplayici = SepetTutari(self.sepet)
        hesaplayici = HediyePaketiDecorator(hesaplayici)
        self.yazdir(hesaplayici)

    def yazdir(self, hesaplayici):
        self.sepet.urunleri_yazdir()
        print("Ödenecek tutar:", hesaplayici.toplam_hesapla(), "TL")


if __name__ == "__main__":
    sepet = SepetFacade()
    sepet.urun_ekle("Klavye", 900)
    sepet.urun_ekle("Mouse", 350)
    sepet.urun_ekle("Kulaklık", 700)

    print("Normal sepet:")
    sepet.normal_sepet_yazdir()

    print("\nVIP sepet:")
    sepet.vip_sepet_yazdir()
