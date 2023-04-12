'''
2023.04.12
왕명호
평점을 입력받아서. 평점출력, 4.2이상이면 "해외연수"
#문제분석
      변수-평점(score)
#알고리즘
      1.변수선언
          score에 평점 실수로 입력받기
      2.논리(선택)
            if score>=4.2:
'''

score=float(input("Enter your score : "))
print("당신의 평점을:",score)

if score>=4.2:  #조건
    print("해외연수")  #조건