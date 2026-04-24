def is_leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
year = int(input('西暦 >>'))
if is_leapyear(year):
    print(f'西暦{year}年は、うるう年です')
else:
    print(f'西暦{year}年は、うるう年ではありません')

"""
def is_leapyear(y):
    return (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))

current_year = int(input('現在の西暦を入力してください >>'))
if is_leapyear(current_year):
    print('西暦{}年は、うるう年です'.format(current_year))
else:
    print('西暦{}年は、うるう年ではありません'.format(current_year))
"""