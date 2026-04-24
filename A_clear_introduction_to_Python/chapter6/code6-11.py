print('identifyの変化を比較')

names = list() # リストの場合
print(f'変更前のlistのidentity: {id(names)}')
names.append('松田')
print(f'変更後のlistのidentity: {id(names)}')

name = '松田'   # 文字列の場合
print(f'変更前のstrのidentity: {id(names)}')
name = 'スーパー' + name
print(f'変更後のstrのidentity: {id(names)}')