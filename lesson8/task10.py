a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
a = [abs(x) for x in a]
a = [round(x) if isinstance(x, float) else x for x in a]
if len(a) >= 2:
    a[0] = a[0] ** 3
    a[-1] = a[-1] ** 3
print(a)
