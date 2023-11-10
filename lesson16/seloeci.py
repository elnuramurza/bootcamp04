while True:
    try:
        user_input = input("vvedite seloe cislo:")
        number = int(user_input)
        print("vvedennoe cislo:", number)
        print("tip dannyx:", type(number).name)
        break
    except ValueError:
        print("Eto ne seloe cislo.Pojolucta, poprobyte snova.")

 
# while True:
#     try:
#         user_input = input("vvedite cislo s plavaysh tockoi: ")
#         number = float(user_input)
#         print("vvedennoe cislo:", number)
#         print("tip dannyx:", type(number).name)
#         break
#     except ValueError:
#         print("eto ne cislo s plavayshe tochkoi. Pojolucta, poprobyte snova.")





