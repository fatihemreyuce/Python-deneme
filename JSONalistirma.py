import json
with open("Data/deneme.json","r",encoding="utf-8") as f:
    result=json.load(f)
    print(type(result))
    print(result)