import requests
server_response = requests.get("https://jsonplaceholder.typicode.com/users")
#print(server_response.status.code)

date = server_response.json()
#print (date)
print(type(date))
# est spisok slovarei
#nado polucit is nego spisok imen
names = []
for element in date:
    names.append(element["name"])
# print (names
#est spisok imen
#nado ego zapisat v fails
with open ('user.txt','w') as users_file:
    for name in names:
        users_file.write(f"{name}\n")

