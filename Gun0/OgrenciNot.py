print("----------Öğrenci Not Sisteri-----------")

ogrenci={"Melih":[60,90,100],"Hasan":[20,90,10],"Murat":[100,30,70]}

ortalama = {ogrenci:sum(notlar)/len(notlar) for ogrenci,notlar in ogrenci.items()}
print(ogrenci)
print(f"{ortalama}:")