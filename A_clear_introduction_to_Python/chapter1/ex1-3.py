height = int(input('身長(cm)>>'))
weight = int(input('体重(kg)>>'))
height = height / 100
print('BMIは{}です'.format(weight / height / height))

"""
h = int(input('身長(cm)は? >>')) / 100
w = float(input('体重(kg)は? >>'))
bmi = w / h / h
print('BMIは{}です'.format(bmi))
"""

"""
h, w = int(input('身長(cm)は? >>')) / 100, \
float(input('体重(kg)は? >>'))
print(f'BMIは{ w / h ** 2 }です')
"""