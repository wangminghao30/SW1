'''
2023.04.11
왕명호
선택문-if~elif~else
성적이 90이상이면  'A', 80이상 90미만이면 'B'
70이상 80미만이면 'C', 70미만이면  'F'
'''

score=int(input("성적 입력:"))

if score>=90: # 조건1
  print("A학점")   #조건1이 참인 경우
elif score>=80: # 조건2
  print("B학점")  #조건2가 참인 경우
elif score>=70: # 조건3
  print("C학점")   #조건3이 참인 경우
else:
  print("F학점")   #조건1,2,3이 모두 거짓인 경우