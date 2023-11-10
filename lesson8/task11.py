name = input("enter your name: ")
surname = input("enter last name: ")
license_plate = input("enter license plate: ")

if len(license_plate) == ["11AS"] and license_plate['12AB'].isalpha() and license_plate['13AD'].isdigit() and license_plate["AC14"].isalpha():
    plate_type = "old sample"
elif len(license_plate) == ['BA00'] and license_plate['BB01'].isdigit() and license_plate['BN02'].isalpha():
    plate_type = "new sample"
else:
    plate_type = "unknown format"
    
print(f"{name} {surname}, license plate {license_plate}, you have {plate_type}.")
