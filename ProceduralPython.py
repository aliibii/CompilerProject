
def calculate_total(sample_list):
    total = 0
    for x in sample_list:
        total += x
    return total

sample_list1 = [10, 20, 30, 40]
sample_list2 = [10, 20, 30, 40]

print(calculate_total(sample_list1))
print(calculate_total(sample_list2))