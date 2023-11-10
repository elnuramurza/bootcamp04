seasons = {"Zima":(1, 2, 12),
           "Vesna":(3, 4, 5),
           "Leto":(6, 7, 8),
           "Osen":(9, 10, 11)}

month = int(input("vyberi month:"))  
for key in seasons.keys():
    if month in seasons[key]:
        print(key)         