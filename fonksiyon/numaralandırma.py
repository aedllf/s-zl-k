def sozluk (x):
#x değişkeni liste türünde olmalıdır
#sozluk fonksiyonun adı
    dic ={}
#dic dictionary yani boş bi sözlük tanımlıyoruz
    v=0
#herhangi bi değişken atadık 0 olarak çünkü her kelimeye farklı bir sayı değerine atıyacağız.
    for c in x:
        dic[v]=c
#her seferinde kelimeleri farklı sayı değerlerine atıyoruz.
        v=v+1
    v=0
#tekrar 0 a eşitledik 
    for c in x :
        dic[c]=v
#atadığmız değerlerin tersinide atadık
        v=v+1
    return f
#fonksiyon değerini değişkene atamak için return kullandık
