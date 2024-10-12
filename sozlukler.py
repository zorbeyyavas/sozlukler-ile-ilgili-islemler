#sözlük ifadesi python dilinde anahtar ve o anahtara ait değer arasında bağ kuran bir veri tipidir. anahtar ve değer birbirlerinden iki nokta üst üste (:) operatörü ile ayrılır.
#sözlüker tanımlanırken süslü parantez kullanılır. geniş veritabanlarında herhangi bir elamana ait anahtar ve değerin alt alta sıralanmış bir biçimde çıkması için ilk elemanın 
#yanında bulunan virgülden sonra "ENTER" tuşuna basılır. her elemandan sonra bu işlem tekrarlanır
#aşağıdaki gibi tanımlanır
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#sözlükte herhangi bir elemanın değerini görmek için o elemana ait anahtar yazılmalı 
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 
print(telefon["salih"])

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#sözlüğe yeni bir kayıt eklemek aşağıdaki gibidir
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 
telefon["zeki"]="0567 983 83 90"
print(telefon)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#sözlükteki herhangi bir elemanı değiştirmek aşağıdaki gibidir 
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 
telefon["zeki"]="0567 983 83 90"
telefon["zeki"]="0768 321 98 70"
print(telefon)


#bir sözlükteki bütün elemanları silmek için clear() kullanılır
telefon={"ahmet":"0545 453 63 76","salih":"0578 879 89 07"} 
telefon.clear()
print(telefon)