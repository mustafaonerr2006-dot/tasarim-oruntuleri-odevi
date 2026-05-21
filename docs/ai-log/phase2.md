# Faz 2 AI notu

## Sorduğum soru

Sepet projemde structural pattern kullanmam gerekiyor. Sepete indirim ve hediye paketi gibi şeyler eklemek istiyorum ama mevcut kodu çok bozmak istemiyorum. Decorator, Facade veya Adapter hangisi daha uygun olur?

## Aldığım cevap

AI, ekstra özellik eklemek için Decorator patternin uygun olduğunu söyledi. Çünkü toplam tutarın üstüne indirim veya ek ücret gibi davranışlar eklenebiliyordu.

Ayrıca sepeti dışarıdan daha kolay kullanmak için Facade pattern kullanılabileceğini söyledi.

## Ben ne yaptım

Ben Decorator ile yüzde indirim, sabit indirim ve hediye paketi sınıflarını yazdım. Böylece aynı sepete birden fazla işlem uygulanabilir hale geldi.

Facade olarak da `SepetFacade` sınıfını ekledim. Main tarafında çok fazla detay görünmesin diye ürün ekleme ve yazdırma işini bu sınıftan yaptım.

## AI'ın eksik veya bana uymayan tarafı

AI Adapter patterni de anlattı ama benim projede dışarıdan gelen farklı bir servis yoktu. Bu yüzden Adapter kullanmak biraz zorlama olurdu. Ben o yüzden Decorator ve Facade ile devam ettim.
