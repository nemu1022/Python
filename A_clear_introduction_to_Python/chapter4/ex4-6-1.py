numbers = [1, 1]
add = 2
while (numbers[-1] + numbers[-2]) < 1000:
    add = numbers[-1] + numbers[-2]
    numbers.append(add)
print(numbers)

"""
numbers = [1, 1]
data = sum(numbers)
count = 2
while data <= 1000:
    numbers.append(data)
    data = data + numbers[count-1]
    count += 1
print(numbers)
"""