# spiski=[name,last_name,age,7 so znacenie 77,code-language, city]
profile = {
"name": "Elnura",
"last_name": "Murzakerimova",
"age": 40,
"code_language": "python",
"city": "Bishkek"
}
profile_list = ['Elnura' , "Murzakerimova" , 40 ,"python" ,"Bishkek"]

print(profile)
# obroshenie k elementy
print(profile['age']) #40 'age' - klych, 40 - znacenie
#dobavlenie 
profile['mesta raboty'] = "ne rabotaet" # 'mesta rabota'- kluch
# izmenenie ß
print(profile)
for t in profile: # t - kluch
    print(t, profile[t])

