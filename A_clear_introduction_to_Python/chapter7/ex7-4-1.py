nums = []
for n in range(3):
    data = int(input(f'{n + 1}個目の整数を入力してください >>'))
    nums.append(data)
print(max(nums))

"""
nums = list()
for n in range(3):
    data = int(input('{}個目の整数を入力してください >>'.format(n + 1)))
    nums.append(data)
print(max(nums))
"""