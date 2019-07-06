#Veri Tipleri ,değişkenlr veri tipi dönüşümleri String üzerine çalışmalar

print(3+7)
print(81/8)
#Değişkenler
i=10
print(i)
i=i+10
print(i)

a="merhaba"

print(a[0])
print(a[-1])#en son indisdeki değeri alıyor
print(len(a))#string'in uzunluğunu vermekte.

b=5
print("float",float(b))
c=5.8
print("int",int(c))#tam kısmı alınır.
#sayıların karaktere dönüştürülmesi için str kullanılur
print("str sonrasında len ile karakterin uzunluğu alındı",len(str(c)))

#\n ve \t karakterleri
print("bir alt\nsatıra\ngeçmek\niçin kullanılır.\n")
print("bir tab bırakmak\tiçin kullanılır.")

#listeler
liste=["selam","nasılsın",10]
print("liste=",liste)
listeBos=[]
listeBos2=list()
liste.append("python")
print(liste)
print("pop ile en son eleman atıldı",liste.pop())
print("pop ile 1.indiste bulunan  eleman atıldı",liste.pop(1),"\n")

a=input()
print(a)