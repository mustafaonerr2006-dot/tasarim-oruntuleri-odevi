# Tasarım Örüntüleri Ödevi

Seçtiğim konu: D - E-Ticaret Sepeti

Bu projede basit bir alışveriş sepeti yaptım. İlk halinde kod biraz dağınıktı. Sonraki fazlarda tasarım örüntüleriyle adım adım daha düzenli hale getirdim.

## Proje ne yapıyor?

- Sepete ürün ekliyor.
- Sepet toplamını hesaplıyor.
- İndirim ve hediye paketi gibi ek işlemleri uyguluyor.
- Kargo türüne göre kargo ücretini hesaplıyor.
- Sipariş oluşunca dinleyicilere haber veriyor.

## Kullandığım örüntüler

- Faz 1: Factory Method
  - Ürün oluşturma işi `UrunFabrikasi` sınıfına alındı.

- Faz 2: Decorator
  - Yüzde indirim, sabit indirim ve hediye paketi ayrı sınıflara ayrıldı.

- Faz 2: Facade
  - Sepeti dışarıdan daha kolay kullanmak için `SepetFacade` yazıldı.

- Faz 3: Strategy
  - Kargo hesaplama şekilleri ayrı strateji sınıflarına ayrıldı.

- Faz 3: Observer
  - Sipariş oluşunca çalışan dinleyiciler eklendi.

## Mimari diyagram

Final diyagramı burada:

`docs/diagrams/faz3-final.md`

## Çalıştırma

```bash
python3 src/shopping_cart.py
```

## Kısa not

Bu proje fazlar ilerledikçe kötü başlangıç kodundan daha düzenli bir yapıya dönüştürüldü. Amacım bütün sistemi baştan mükemmel yazmak değil, tasarım örüntülerinin kodu nasıl toparladığını göstermekti.
