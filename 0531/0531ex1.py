'''
2023-05-31
201995114
왕명호
#문제정의
   10개의 난수를 발생시키고 리스트에 저장 한 후 최대, 최소,합계 구하기
#문제분석
    변수-빈리스트(num)
#알고리즘
    1.랜덤 모듈 추가
    2.변수 초기화
        num=[]
    3.반복
        for i in range(10):
            난수 생성
            리스트에 추가
    4.결과 출력(최대, 최소,합계,정렬)
'''
import random
num=[] #난수 저장을 위한 리스트 변수

for i in range(10): #반복 조건
    num.append(random.randint(1,100)) #난수 발생 후 리스트 변수

print("생성된 리스트:",num)
print("최대값",max(num))
print("최소값",min(num))
print("합계",sum(num))
num.sort() #오름차순 정렬
print("정렬된 리스트:",num)
num.sort(reverse=True) #내림차순 정렬
print("정렬된 리스트:",num)