for i in range(9):
    if (i+1) % 2 == 0:
        continue
    else:
        for j in range(9):
            if ((i+1) * (j+1)) > 50:
                break
            else:
                print(f'{(i+1) * (j+1)} ',end='')
    print('')

"""
for i in range(9):
    if (i+1) % 2 == 0:
        continue
    for j in range(9):
        if (i+1)*(j+1) > 50:
            break
        print('{}×{}={}'.format(i+1, j+1, (i+1)*(j+1)))
"""