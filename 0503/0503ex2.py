'''
2023-05-03
201995114
왕명호
1~10까지 합계 구하기
'''

#while반복
i=1 #반복 횟수 초기화
sum=0 #합계
while i<=10:  #반복 조건
  sum=sum+i #합계 저장
  i=i+1  #i 1증가
print('1~10까지의 합계:',sum)

#for반복
sum1=0
for j in range(1,11):
    sum1=sum1+j

print('1~10까지의 합계:',sum1)