figures = input("hello! what's your name?")
print("hello," + figures + "!")
number_of_sides = int(input("how many sides does a figure have? "))
if number_of_sides == 3:
    print("this is a triangle.")
elif number_of_sides == 4:
    print("it's a square.")
elif number_of_sides == 5:
    print("this is a pentagon.")
else:
    print("we don't have such a figure")    