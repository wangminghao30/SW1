'''
2023.04.12
왕명호
입력받을 두 수의 크기 비교
#문제분석
    1.  변수 선언
          숫자1(num1),숫자2(num2)
    2. 논리(선택)
          if num1>num2:
              (참)큰 수는 num1, 작은 수 num2
          else:
              (거짓)큰 수는 num2, 작은 수 num2
'''
num1=int(input("첫 번쩨 숫자 입력 : "))
num2=int(input("두 번쩨 숫자 입력 : "))

if num1>num2 :
  print("두 수 중에 클 수는{},작은 수 {}이다 ".format(num1,num2))

else :
  print("두 수 중에 클 수는{},작은 수 {}이다 ".format(num2,num1))
  