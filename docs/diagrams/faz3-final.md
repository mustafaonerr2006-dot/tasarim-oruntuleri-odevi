# Faz 3 final diyagramı

```mermaid
classDiagram
    class SepetFacade
    class UrunFabrikasi
    class Urun
    class TutarDecorator
    class YuzdeIndirimDecorator
    class SabitIndirimDecorator
    class HediyePaketiDecorator

    class SiparisYoneticisi {
        kargo_stratejisi
        dinleyici_ekle()
        siparisi_tamamla()
    }

    class StandartKargoStratejisi
    class HizliKargoStratejisi
    class MagazadanTeslimStratejisi

    class KonsolDinleyici
    class SiparisSayacDinleyici

    SepetFacade --> UrunFabrikasi
    UrunFabrikasi --> Urun
    TutarDecorator <|-- YuzdeIndirimDecorator
    TutarDecorator <|-- SabitIndirimDecorator
    TutarDecorator <|-- HediyePaketiDecorator
    SiparisYoneticisi --> StandartKargoStratejisi
    SiparisYoneticisi --> HizliKargoStratejisi
    SiparisYoneticisi --> MagazadanTeslimStratejisi
    SiparisYoneticisi --> KonsolDinleyici
    SiparisYoneticisi --> SiparisSayacDinleyici
```
