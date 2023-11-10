def find_concsripts(ages):
    concsripts = [age for age in ages if 18 <= age <=27]
    return concsripts
ages = [15,18,20,25,30,40]
concsripts = find_concsripts(ages)
print(concsripts)