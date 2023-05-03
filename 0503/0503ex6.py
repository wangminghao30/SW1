'''
2023-05-03
201995114
왕명호
#문제정의
      구구단 출력(중첩 반복)
#문제분석
      변수 -i,j
#알고리즘
     논리(반복-중첩 반복(for))
      (조건) for i in range(1,10): #단 반복
                    제목 출력
                    for j  in  range(1,10): #단 안에서 곱하는 수 반복
                        구구단 출력
'''

for i  in  range(1,10):
    print("##",i,"단 ##")
    for j  in  range(1,10):
      print('{}*{}={}'.format(i,j,i*j))