my_post = {
  "post": {
    "name": "python",
     "comments":[
            {
                 "id": "1",
                 "text":"ok, that's good",
            },
            {
                 "id": "6", 
                 "text": "not bad",
            },
        ]
    },
    "userId": 1,
    "id": 1,
}
#polucit i vyvesti spisok commentari:["ok,that's good","not bad"]

print(my_post["post"]["comments"][0]["text"])
print(my_post["post"]["name"])

comments_list = []
for comment in my_post["post"]["comments"]:
    comments_list.append(comment["text"])
print(comments_list)