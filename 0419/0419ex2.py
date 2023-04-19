'''
2023.04.19
왕명호

#문제분석
    변수:
    수식:
#알고리즘(단순if)
        1. 
        2. 
#알고리즘(다중if)
        1.변수 선언
        num 에 정수 입력
'''

num = int(input("숫자 입력 : "))

if (num < 0 ):
  print("입력값 %d은(는) 움수입니다."%num)
if (num == 0 ):
  print("입력값 %d은 0입니다."%num)
if (num > 0 ):
  print("입력값 %d은 양수입니다."%num)



num = int(input("숫자 입력:"))
if (num < 0 ):
  print("입력값 %d은(는) 움수입니다."%num)
elif (num == 0 ):
  print("입력값 %d은 0입니다."%num)
else :
  print("입력값 %d은(는) 양수입니다."%num)