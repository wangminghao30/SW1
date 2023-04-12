'''
2023.04.12
왕명호
입력받을 두 수의 크기 비교
#문제분석
    1.  변수 선언
          변수 - 정수1(num1),정수2(num2)
     수식 - num1%2==0 (num1은 짝수)/num1%2!=0 (num1은 홀수)
    2. 논리(선택)
'''

num1=int(input("첫 번쩨 숫자 입력 : "))
num2=int(input("두 번쩨 숫자 입력 : "))

if num1%2==0 and num2%2==0 :
  print("{} + {} ={}".format(num1,num2,num1+num2))
elif num1%2==1 and num2%2==0 :
  print("첫 번쩨 숫자를 짝  수로 입력하세요.")
elif num1%2==0 and num2%2==1 :
  print("두 번쩨 숫자를 짝  수로 입력하세요.")
else  :
  print("두 숫자 모두를 짝수로 입력하세요.")