import string

kisi = {"İsim":"Ahmet","Yaş" : 20, "Şehir":"İstanbul","Hobiler":["Sinema","Futbol","Basketbol"]}
print(kisi)

kisi["İsim"] = "Ayşe" #Güncelleme Kısmı
print(kisi)

kisi.update({"İsim":"Ali","Yaş":25}) #Birden fazla güncelleme yapılacağı zaman kullanılıyor
print(kisi)

kisi["ID"] = 1234

print(kisi)

del kisi["ID"] #Silme işlemi için
print(kisi)

for x in kisi: #Sözlükteki Keyleri yazdırıyor
    print(x)

for x in kisi:   #Sözlükteki Keylerin karşılığı olan value değerlerini yazıyor
    print(kisi[x])


print(kisi.keys()) #Sadece Keysleri yazıyor

print(kisi.items()) #Sözlükteki hem key hem de value değerlerinmi ceker items() metodu ile

for k,v in kisi.items():
    print(k,v)

print(kisi.get("id","bulunamadı")) #Sözlükte erişmek istediğim eleman yoksa hata mesajı vermek yerine None değerini göndürüyor (yok demek) varsa yazdırıyor

print("-----------------Telefon Rehberi------------------------------------")

rehber={"Ahmet":"05555555555","Ayşe":"05444444444","Hasan":"032222222222","Mehmet":"05555555555","Fatma":"05555555555"}



del rehber["Ahmet"]


kisi.update({"Melike":"09999999999"})

for k,v in rehber.items():
    print(k,v)

print(rehber.get("Arda","Bulunamadı"))


print("----------------Öğrenci Not Sistemi---------------------")

ogrenci={"Ali":[80,90,70],"Mehmet":[60,85,75],"Ayşe":[100,90,80]}

ortalamalar = {ogrenci: sum(notlar) / len(notlar) for ogrenci, notlar in ogrenci.items()}
print(ogrenci)
print(ortalamalar)


print("----------------------------Kelime Sayacı-----------------")
cumle = "Bugün eve gidemedim çünkü her yerde trafik vardı."

kelimeler = cumle.lower().split()

kelime_sayaci = {}

for kelime in kelimeler:
    kelime_sayaci[kelime] = kelime_sayaci.get(kelime, 0) + 1

print(kelime_sayaci)

