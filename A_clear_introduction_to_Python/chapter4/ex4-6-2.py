numbers = [1, 1]
ratios = []
ratios.append(numbers[-1] / numbers[-2])
while (numbers[-1] + numbers[-2]) < 1000:
    add = numbers[-1] + numbers[-2]
    numbers.append(add)

    div = numbers[-1] / numbers[-2]
    ratios.append(div)
print(numbers)
print(ratios)

"""
ratios = list()
for count in range(len(numbers)):
    if count == len(numbers) - 1:
        break
    ratios.append(numbers[count+1] / numbers[count])
print(ratios)
"""