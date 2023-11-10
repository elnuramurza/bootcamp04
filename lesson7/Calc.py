def calculate_total_cost(*args): 
    total_cost = 0
    for cost in args:
        total_cost += cost
    return total_cost
cost1 = 60
cost2 = 20
cost3 = 35
total = calculate_total_cost(cost1, cost2, cost3)
print("Obzhaya stoimost:", total)