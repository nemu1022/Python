temp = []
for i in range(10):
     t = float(input(f'{i+8}時の気温 >>'))
     temp.append(t)

temp_new = []
for i in range(10):
    if i != 5:
          temp_new.append(temp[i])
    else:         
         temp_new.append('N/A')

total = 0
count = 0
for i in temp_new:
    if isinstance(i, float):
         total += i
         count += 1
         
print(f'平均気温は{total/count}度')

"""
total = 0
for data in temp_new:
    if isinstance(data, float):
        total = total + data
print(total / (len(temp_new) - 1))
"""