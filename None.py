import time
kronometre = None

while True:
    komut = input("Değer Giriniz:")
    if komut == "Başla":
        kronometre = time.time()
        print("Kronometre başladı!!")
    elif komut == "Dur":
        if kronometre is not None:
            sure = time.time() - kronometre
            print(f"Geçen süre: {sure:.2f} saniye")
        kronometre = None