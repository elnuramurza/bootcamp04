
def create_squares_dict(n):
    squares_dict = {x: x**2 for x in range(1, n+1)}
    return squares_dict
n = 10
squares_dict = create_squares_dict(n)
print(squares_dict)
