"""
(1) 2 + 10 * 5
→ 2 + 50
→ 52
   
(2) '7' * (3 + 4)
→ '7' * 7
→ '7777777'

(3) f'version{3 + 2 * 0.1 + 9 * 0.01}'
→ f'version{3 + 0.2 + 9 * 0.01}'
→ f'version{3 + 0.2 + 0.09}'
→ f'version{3.2 + 0.09}'
→ f'version{3.29}'
→ version3.29

(4) 4 * 'num' + '回目のTyoeError'
→ 'numnumnumnum' + '回目のTypeError'
→ 'numnumnumnum回目のTypeError'
"""