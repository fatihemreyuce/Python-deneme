import math
import random
import time


nesneler = {
    "Araba": (100, 200),
    "Kisi": (300, 150),
    "Top": (50, 50)
}

print("--- Hareket Simülatörü Başlıyor ---\n")


for tur in range(1, 11):
    print(f"[{tur}. TUR]")


    for isim, (eski_x, eski_y) in nesneler.items():


        hareket_x = random.randint(-30, 30)
        hareket_y = random.randint(-30, 30)


        yeni_x = eski_x + hareket_x
        yeni_y = eski_y + hareket_y


        mesafe = math.sqrt((yeni_x - eski_x) ** 2 + (yeni_y - eski_y) ** 2)


        if mesafe < 10:
            durum = "HAREKETSIZ"
        else:
            durum = "HAREKET EDIYOR"


        print(f"  {isim:5} | Mesafe: {mesafe:5.2f} birim | Durum: {durum}")


        nesneler[isim] = (yeni_x, yeni_y)

    print("-" * 45)


    time.sleep(1)

print("\nSimülasyon Bitti!")