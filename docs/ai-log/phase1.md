# Faz 1 AI notu

## Sorduğum soru

Sepet kodumda ürün adları ve fiyatları ayrı listelerde duruyor. Faz 1'de creational pattern kullanmam gerekiyor. Burada hangi pattern daha mantıklı olur?

## Aldığım cevap

AI, ürünleri ayrı listelerde tutmak yerine `Urun` diye bir sınıf açmamı söyledi. Ürün oluşturma işini de ayrı bir factory sınıfına almamı önerdi. Böylece sepet sınıfı ürünün nasıl oluşturulduğunu çok bilmek zorunda kalmayacaktı.

## Ben ne yaptım

Ben de `Urun` ve `UrunFabrikasi` sınıflarını ekledim. Ürün eklerken artık direkt listeye ad ve fiyat atmıyorum, önce factory üzerinden ürün oluşturuyorum.

AI indirim tarafını da ayırmayı önerdi ama ben onu bu fazda yapmadım. Çünkü bu fazda özellikle nesne oluşturma kısmına odaklanmak istedim.
