# Kullandığım tasarım örüntüleri

## Faz 1 - Factory Method

Bu fazda ürün oluşturma işini `UrunFabrikasi` sınıfına aldım.

Önceden ürün adı ve fiyatı ayrı listelerde duruyordu. Bu yüzden ürün bilgileri dağınıktı. Şimdi her ürün `Urun` nesnesi olarak tutuluyor.

Factory kullanınca ürün oluşturma işi sepet sınıfının içinde kalmadı. İleride ürüne kategori, stok veya vergi gibi bilgiler eklenirse ilk bakacağım yer fabrika sınıfı olur.
