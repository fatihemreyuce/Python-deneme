import json



person={"name": "Fatih Emre","surname": "Yüce","age": 20,"city": "Kocaeli","hobbies":["Oyun","Muzik","Kodlama"]}
with open("Data/people.json","w",encoding="utf-8") as f:
 json_result = json.dump(person,f, ensure_ascii=False,indent=4)


#
# json_result = json.dumps(person, ensure_ascii=False,indent=4,sort_keys=True) #ASCII sağlayıcısını kapatma kısmı indent kısmı ise girinti demek sort_key ise alfabetik sıralama yapmaktadır
# print(json_result)
# print(type(json_result))

# x={
#     "name":"Fatih Emre",
#     "surname":"Yüce",
#     "age":20,
#     "city":"Kocaeli",
#     "married":False,
#     "divorced":False,
#     "parents":("Gülper","Murat"),
#     "pets":None,
#     "cars":["Fiat Doblo","BYD Seul"]
# }
#
# json_result = json.dumps(x,ensure_ascii=False,indent=4,sort_keys=True)
# print(json_result)