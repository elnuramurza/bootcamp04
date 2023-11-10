
def extract_digits(input_string):
    digits = [int(char) for char in input_string if char.isdigit()]
    return digits


input_string = "lsj94ksd231 9"
extracted_digits = extract_digits(input_string)
total_sum = sum(extracted_digits)

print("vyvod =", extracted_digits)
print("summa =", total_sum)