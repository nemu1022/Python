temp = []
for i in range(10):
     t = input(f'{i+8}時の気温 >>')
     temp.append(t)
for n in range(len(temp)):
    print(f'{n+8}時 {temp[n]}度')

"""
for count in range(len(temp)):
    print('{}時 {}度'.format(count+8, temp[count]))
"""