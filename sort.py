def bubble_sort(data): 
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

dataset = [12, 10, 15, 45, 77, 3, 16, 30, 55]
bubble_sort(dataset)
print(dataset)
print(bubble_sort(dataset))