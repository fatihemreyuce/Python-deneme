Rehber= {"Ahmet": "05555555555", "Hasan": "0666666666", "Fatma": "03333333333", "Ayşe": "02222222222",
         "Mehmet": "07777777777", "Murat": "0888888888888"}



print(Rehber.get("Mesut","Bulunamadı"))

Rehber.update({"Ahmet":"01111111111111"})

print("------Kişiler-----")
for x in Rehber.items():
    print(x)


del Rehber["Ahmet"]

print("------Kişiler-----")
for x in Rehber.items():
    print(x)