'''
2023-05-17
201995114
왕명호
#문제정의
      학생이름 성적 3개 입력 받아서 파일에 저장하기
#문제분석
      변수:이름성적입력(score)
#알고리즘
      1.파일 객체 생성(w모드)
      2.이름성적입력(5명-반복)
          while i<=5:
              score변수에 이름성적 입력
              파일에 쓰기
              i 1증가
'''

f=open("/Users/wangminghao/Desktop/data/stu.txt","w")

i=1
while i<=5:
    score=input("%d번째 학생이름과 3과목 성적입력:"%i)
    f.write(score+"\n")
    i+=1

f.close()