'''
2023.04.19
왕명호
두 개의 숫자를 입력받아서 두 번재 수의 약수인지 구분하기
#문제분석
    변수:정수1(num1), 정수2(num2)
    수식:num1%num2== (num2는 num1의 약수)
#알고리즘
        1. 변쑤 선언
                    num1, num2 정수로 입력 받기
        2. 논리(선택 if~else)
            if num1%num2==0:
                num2는 num1의 약수
            else:
                  num2는 num1의 약수가 아니다
'''

num1=int(input("첫 번쩨 숫자 입력하세요 : "))
num2=int(input("두 번쩨 숫자 입력하세요 : "))

if num1%num2==0:
        print("{}는 {}의 약수입니다.".format(num2,num1))
else:
        print("{}는 {}의 약수가 아닙니다.".format(num2,num1))