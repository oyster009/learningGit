list = [1, 2, 3, 4, 5]

def mean(lists):
    lenght = len(lists)
    total = sum(lists)
    mean = total / lenght
    return mean


for i in range(len(list)):
    print(list[i])

print("mean of the list:")
print(mean(list))