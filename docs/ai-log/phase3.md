# Faz 3 AI notu

## Sorduğum soru

Sepet projemde behavioral pattern kullanmam gerekiyor. Sipariş tamamlanınca bildirim gibi şeyler çalışsın, ayrıca kargo türünü de değiştirebilmek istiyorum. Hangi patternler daha mantıklı olur?

## Aldığım cevap

AI, kargo seçimi için Strategy kullanabileceğimi söyledi. Çünkü standart kargo, hızlı kargo ve mağazadan teslim gibi seçeneklerin hesaplaması farklıydı.

Sipariş tamamlanınca başka sınıfların haber alması için de Observer kullanabileceğimi söyledi.

## Ben ne yaptım

Kargo için Strategy kullandım. `StandartKargoStratejisi`, `HizliKargoStratejisi` ve `MagazadanTeslimStratejisi` sınıflarını yazdım.

Observer için de sipariş oluşunca çalışan dinleyiciler ekledim. Biri ekrana bilgi yazıyor, biri sipariş sayısını tutuyor.

## AI olmadan ne kadar sürerdi?

Bence AI olmadan bu fazı yapmak 3 saatten fazla sürerdi. Çünkü Strategy ve Observer isimlerini biliyordum ama hangisini nereye koyacağımı seçmekte zorlanırdım.

## AI beni nerede yanılttı?

AI ilk başta Command pattern de önerebilirdi gibi anlattı ama benim projede geri alma veya komut kuyruğu gibi bir ihtiyaç yoktu. O yüzden onu kullanmadım.
