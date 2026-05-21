# Faz 0'da gördüğüm sorunlar

1- Ürün adları ve fiyatları ayrı ayrı listelerde tutuluyor.
Bir ürün silinirse veya sıralama değişirse ad ve fiyat birbirine karışabilir. Bu yüzden ürün bilgisini tek bir yerde tutmak daha doğru olur.

2- İndirim türleri uzun if-elif yapısıyla kontrol ediliyor.
Yeni bir indirim eklemek istediğimde çalışan metodun içine yeni kod yazmam gerekiyor. Bu da OCP prensibine uygun değil.

3- Sepeti yazdıran metot hem hesaplama yapıyor hem ekrana çıktı basıyor.
Bir metot birden fazla işi yapınca sonradan değiştirmek zorlaşıyor. Mesela sadece çıktı şeklini değiştirmek istesem bile hesaplama koduna dokunmam gerekebilir.

4- İndirim türü String olarak tutuluyor.
"SEZON" yerine yanlışlıkla başka bir şey yazılırsa program bunu önceden fark etmiyor. Bu da hatayı bulmayı zorlaştırıyor.

5- Aynı anda birden fazla indirim uygulanamıyor.
Gerçek bir e-ticaret sepetinde hem sezon indirimi hem kupon indirimi gibi şeyler birlikte olabilir. Bu kodda sadece tek bir indirim seçilebiliyor.

# AI ile karşılaştırma

AI'a bu kodu gösterip tasarım açısından hangi sorunları gördüğünü sordum. AI da benim gördüğüm gibi if-elif yapısının büyüyeceğini, ürün bilgilerinin ayrı listelerde tutulmasının riskli olduğunu ve metodun birden fazla sorumluluğu olduğunu söyledi.

AI benim yazdıklarıma ek olarak bu sorunların SOLID prensipleriyle ilişkisini daha net açıkladı. Özellikle OCP ve SRP ihlalinden bahsetti. Ayrıca indirimleri ayırmak için Strategy kullanılabileceğini, ürün oluşturma tarafında da Factory benzeri bir yapı kurulabileceğini söyledi.

Ben ilk bakışta daha çok kodun pratikte karışacak yerlerine dikkat etmiştim. AI ise aynı sorunları daha teknik isimlerle açıkladı. Bu yüzden Faz 1'de önce nesne oluşturma tarafını düzeltmek daha mantıklı görünüyor.
