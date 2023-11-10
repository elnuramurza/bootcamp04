sea = []
for i in range(5):
    sea.append([]) #[[]]
    for j in range(5):
        sea[-1].append('')
# dobovlaem korobli
ships = 3
for k in range(ships):
    y = int(input (f " koordinaty "y" korabl {k+1}:" )) 
    x = int(input (f " koordinaty  "x" korabl {k+1}:"))
    sea[y] [x] = "s"

#nachinaaem igru
while ships:
        #otrisovka mor
    for row in sea:
        for cell in row:
            print(cell, end= "")
                print()
               
                #xod protivnika 
fire_point = input ("protivnik strelaet:")  #2  4
points_list = fire_point.split() #["2", "4"]  
fire_y = int(points_list[0]) #2
fire_x = int(points_list[1]) #4
      
      #proverka popadaniy
if sea [fire_y] [fire_x] == "s":
    print("popal")
    sea[fire_y][fire_x]= " "
    ships -=1
else:
print("mimo")
print("end game")



