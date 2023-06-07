'''
2023-06-07
201995114
왕명호
'''

import random

lotto = set()
i=0
while True:
    lotto.add(random.randint(1,45))

    i=i+1
    if len(lotto)==6:
        break
print("이번주 로또 넙버 :",sorted(lotto))

print("중복된 난수의 발생 횟수 :",i-6)