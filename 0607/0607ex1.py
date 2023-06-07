'''
2023-06-07
201995114
왕명호
#문제정의 
#문제분석
#알고리즘
      1.랜덤모듈 추가
      2.비어있는 세트 변수 생성
      3.반복(무한반복)
'''
import random

num1=set()
num2=set()

while True:
    if len(num1)<10:
        num1.add(random.randint(1,100))
    if len(num2)<10:
        num1.add(random.randint(1,100))

    if len(num1) == 10 and len(num2) == 10:
        break

print("발생된 10개의 난수 num1:",num1)
print("발생된 10개의 난수 num2:",num2)

print("num1,num2의 합세트 :",num1 | num2)
print("num1,num2의 교세트 :",num1 & num2)
print("num1,num2의 차세트 :",num1 - num2)