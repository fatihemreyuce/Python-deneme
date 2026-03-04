print("-------Kelime Sayac-------")

cumle="Bugun yolda yürürken bir kedi gördüm. Aşırı sevimli idi. Sonra yolda yürürken bakkala da uğradım"

kelimeler=cumle.lower().split()
kelime_sayaci={}

for kelime in kelimeler:
    kelime_sayaci[kelime]=kelime_sayaci.get(kelime,0)+1

print(kelime_sayaci)