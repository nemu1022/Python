temp = []
for i in range(10):
     t = input(f'{i+8}時の気温 >>')
     temp.append(t)

temp_new = []
for i in range(10):
    if i != 5:
          temp_new.append(temp[i])
    else:         
         temp_new.append('N/A')
    
for n in range(len(temp)):
    print(f'{n+8}時 {temp[n]}度　', end = '')
    print(f'{n+8}時 {temp_new[n]}度')

"""
temp_new = list()
for count in range(len(temp)):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)
"""