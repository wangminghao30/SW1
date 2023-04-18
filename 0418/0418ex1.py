'''
2023.04.18
왕명호
성적처리 프로그램(중첩 if문으로 작정 )
입력받은 성적이 90이상이면  'A', 80이상 90미만이면 'B'
70이상 80미만이면 'C', 70미만이면  'F'
'''

jumsu=int(input("성적 입력:")) #점수를 정수로 입력

if jumsu>=70: # 조건1
    if jumsu>=80: # 조건2
        if jumsu>=90: # 조건3
            print("A학점")
        else:
              print("B학점")
    else:
          print("C학점")
else:
      print("F학점")          