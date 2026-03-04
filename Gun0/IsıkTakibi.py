import time

isik_acilma_zamani = None

while True:
    komut = input("Komut (ac/kapa/durum): ")
    if komut == "ac":
        isik_acilma_zamani = time.time()
        print("Isik acildi!")
    elif komut == "kapa":
        if isik_acilma_zamani is not None:
            sure = time.time() - isik_acilma_zamani
            print(f"Isik {sure:.1f} saniye acik kaldi")
        isik_acilma_zamani = None
    elif komut == "durum":
        if isik_acilma_zamani is None:
            print("Isik KAPALI")
        else:
            sure = time.time() - isik_acilma_zamani
            print(f"Isik ACIK ({sure:.1f} sn)")