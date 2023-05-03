'''
2023-05-03
201995114
왕명호
#문제정의
      1~입력받은 숫자까지의 합계 구하기
#문제분석
      변수 :
      num1
#알고리즘
'''

#for반복
num1=int(input("숫자1입력:"))

sum=0
for i in range(1,num1+1):
  sum=sum+i

print('1~{}까지의 합계는 {}'.format(num1,sum))

#while반복

num2=int(input("숫자2입력:"))

j=1 #반복 횟수 초기화
sum2=0 #합계
while j<=num2:  #반복 조건
  sum2=sum2+j #합계 저장
  j=j+1  #i 1증가
print('1~{}까지의 합계는 {}'.format(num2,sum2))