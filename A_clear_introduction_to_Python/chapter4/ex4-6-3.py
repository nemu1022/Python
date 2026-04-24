numbers = [1, 1]
ratios = []
ratios.append(numbers[-1] / numbers[-2])
while (numbers[-1] + numbers[-2]) < 1000:
    add = numbers[-1] + numbers[-2]
    numbers.append(add)

    div = numbers[-1] / numbers[-2]
    div = int(div * 1000)
    div = div / 1000
    ratios.append(div)
print(numbers)
print(ratios)

"""
for count in range(len(ratios)):
    ratios[count] = int(ratios[count] * 1000) / 1000
print(ratios)
"""