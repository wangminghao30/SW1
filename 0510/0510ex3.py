'''
2023-05-10
201995114
왕명호
#문제정의
      입력받은 숫자 만큼
#문제분석
      변수 :정수(num)
#알고리즘
      1.변수 초기화
             num변수에 정수 입력
      2.논리(중첩 반복)
            (반복) for i in range(1,num+1):
                    (반복) for j in range(1,i+1):
                              별 찍기
'''
num=int(input("숫자 입력:"))
for i in range(1,num+1):
        for j in range(1,i+1):
          print("*",end="")
        print( )

print("\n거꾸로 출력")

num2=int(input("숫자 입력:"))
for i in range(1,num+1):
        for j in range(i,num2+1):
          print("*",end="")
        print( )