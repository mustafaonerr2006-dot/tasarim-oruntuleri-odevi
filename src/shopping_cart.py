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

    def normal_hesaplayici(self):
        return SepetTutari(self.sepet)

    def sezon_hesaplayici(self):
        hesaplayici = SepetTutari(self.sepet)
        if hesaplayici.toplam_hesapla() > 1000:
            hesaplayici = SabitIndirimDecorator(hesaplayici, 150)
        return hesaplayici

    def vip_hesaplayici(self):
        hesaplayici = SepetTutari(self.sepet)
        hesaplayici = YuzdeIndirimDecorator(hesaplayici, 20)
        hesaplayici = SabitIndirimDecorator(hesaplayici, 50)
        return hesaplayici

    def hediye_paketli_hesaplayici(self):
        hesaplayici = SepetTutari(self.sepet)
        hesaplayici = HediyePaketiDecorator(hesaplayici)
        return hesaplayici

    def yazdir(self, hesaplayici):
        self.sepet.urunleri_yazdir()
        print("Sepet tutarı:", hesaplayici.toplam_hesapla(), "TL")


class StandartKargoStratejisi:
    def kargo_ucreti_hesapla(self, tutar):
        if tutar > 1000:
            return 0
        return 50


class HizliKargoStratejisi:
    def kargo_ucreti_hesapla(self, tutar):
        return 120


class MagazadanTeslimStratejisi:
    def kargo_ucreti_hesapla(self, tutar):
        return 0


class KonsolDinleyici:
    def siparis_olustu(self, toplam):
        print("Bilgi: Sipariş oluşturuldu. Toplam:", toplam, "TL")


class SiparisSayacDinleyici:
    def __init__(self):
        self.siparis_sayisi = 0

    def siparis_olustu(self, toplam):
        self.siparis_sayisi = self.siparis_sayisi + 1

    def yazdir(self):
        print("Oluşan sipariş sayısı:", self.siparis_sayisi)


class SiparisYoneticisi:
    def __init__(self, kargo_stratejisi):
        self.kargo_stratejisi = kargo_stratejisi
        self.dinleyiciler = []

    def kargo_stratejisi_degistir(self, kargo_stratejisi):
        self.kargo_stratejisi = kargo_stratejisi

    def dinleyici_ekle(self, dinleyici):
        self.dinleyiciler.append(dinleyici)

    def siparisi_tamamla(self, hesaplayici):
        sepet_toplami = hesaplayici.toplam_hesapla()
        kargo_ucreti = self.kargo_stratejisi.kargo_ucreti_hesapla(sepet_toplami)
        genel_toplam = sepet_toplami + kargo_ucreti

        print("Kargo ücreti:", kargo_ucreti, "TL")
        print("Genel toplam:", genel_toplam, "TL")

        for dinleyici in self.dinleyiciler:
            dinleyici.siparis_olustu(genel_toplam)


if __name__ == "__main__":
    sepet = SepetFacade()
    sepet.urun_ekle("Klavye", 900)
    sepet.urun_ekle("Mouse", 350)
    sepet.urun_ekle("Kulaklık", 700)

    hesaplayici = sepet.vip_hesaplayici()
    sepet.yazdir(hesaplayici)

    siparis_yoneticisi = SiparisYoneticisi(HizliKargoStratejisi())
    sayac = SiparisSayacDinleyici()

    siparis_yoneticisi.dinleyici_ekle(KonsolDinleyici())
    siparis_yoneticisi.dinleyici_ekle(sayac)

    siparis_yoneticisi.siparisi_tamamla(hesaplayici)
    sayac.yazdir()
