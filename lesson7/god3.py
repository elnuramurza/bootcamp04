def is_leap(year):
    
    
    if((year % 400 == 0) or
        (year % 100 != 0) and
        (year % 4 == 0)):         
        print("etot god vysokosny")
    else:
        print("etot god ne vysokosny")
            
year = int(input("enter dly numera"))   
is_leap(year)           
