# Kullandığım tasarım örüntüleri

## Faz 1 - Factory Method

Bu fazda ürün oluşturma işini `UrunFabrikasi` sınıfına aldım.

Önceden ürün adı ve fiyatı ayrı listelerde duruyordu. Bu yüzden ürün bilgileri dağınıktı. Şimdi her ürün `Urun` nesnesi olarak tutuluyor.

Factory kullanınca ürün oluşturma işi sepet sınıfının içinde kalmadı. İleride ürüne kategori, stok veya vergi gibi bilgiler eklenirse ilk bakacağım yer fabrika sınıfı olur.

## Faz 2 - Decorator

Bu fazda indirimleri ve ek ücretleri Decorator yapısıyla ayırdım.

Önceden indirimler `if-elif` içinde duruyordu. Şimdi yüzde indirim, sabit indirim ve hediye paketi gibi işlemler ayrı decorator sınıflarında duruyor.

Bunun iyi yanı şu oldu: Birden fazla indirim üst üste uygulanabiliyor. Mesela VIP sepette önce yüzde indirim, sonra sabit indirim uygulanıyor.

## Faz 2 - Facade

`SepetFacade` sınıfını kullanarak sepeti dışarıdan daha kolay kullanılır hale getirdim.

Main tarafında artık detay sınıflarla çok uğraşmıyorum. Ürün ekleyip `normal_sepet_yazdir` veya `vip_sepet_yazdir` gibi metotları çağırıyorum.

Facade burada kodu tamamen değiştirmedi ama kullanımını daha sade yaptı.
