count = 5
print('カレーを召し上がれ')
key = 'y'
while key == 'y':
    print(f'{count}皿のカレーを食べました')
    key = input('おかわりはいかがですか？ (y/n)>>')
    if key == 'y':
        count += 1
print('ごちそうさまでした')

"""
count = 1
ans = True
print('カレーを召し上がれ')
while ans == True:
    print('{}皿のカレーを食べました'.format(count))
    key = input('おかわりはいかがですか?(y/n)>>')
    if key == 'y':
        count += 1
    else:
        ans = False
print('ごちそうさまでした')
"""