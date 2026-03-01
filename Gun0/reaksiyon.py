import time
import random

print("⚡ Reaksiyon Hızı Testine Hoş Geldin!")
input("Hazırsan başlamak için 'Enter'a bas...\n")

bekleme_suresi = random.uniform(2, 5)

print("Hazır ol...")

time.sleep(bekleme_suresi)

print("\n ŞİMDİ BAS!")
baslangic_zamani = time.time()

input()
bitis_zamani = time.time()
reaksiyon_suresi = bitis_zamani - baslangic_zamani

print(f"Tebrikler! Reaksiyon süren: {reaksiyon_suresi:.3f} saniye.")