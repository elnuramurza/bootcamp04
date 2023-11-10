
def get_sorted_names(input_list):
    names = [item.capitalize() for item in input_list if isinstance(item, str)]
    sorted_names = sorted(names)
    return sorted_names

def print_reverse_sorted_integers(input_list):
    integers = [item for item in input_list if isinstance(item, int)]
    sorted_integers = sorted(integers, reverse=True)
    print(sorted_integers)

def sum_float_numbers(input_list):
    float_numbers = [item for item in input_list if isinstance(item, float)]
    total = sum(float_numbers)
    return total


list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
sorted_names = get_sorted_names(list_1)
print(sorted_names)

print_reverse_sorted_integers(list_1)

sum_of_floats = sum_float_numbers(list_1)
print(sum_of_floats)
