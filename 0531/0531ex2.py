'''
2023-05-31
201995114
왕명호
#문제정의
   이차원 리스트의 학생 점수를 참고하여
   각 학생의 3과목 총점 구하기
#문제분석
    변수-점수리스트(num)
#알고리즘
    
'''
num=[[20001,20002,20003,20004,20005],
     [89,74,88,99,95],[91,75,68,98,88],[79,94,68,94,92]]

j=0

for i in range(len(num[0])): #리스트 요소 만큼 반복(학생수)
    print(num[j][i],"학생의 총점:",num[j+1][i]+num[j+2][i]+num[j+3][i])