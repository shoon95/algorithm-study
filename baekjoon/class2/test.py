def my_avg(*value):
    total = 0
    for i in value:
        total += i
    return total/len(value)
    
print(my_avg(77, 83, 95, 80, 70))