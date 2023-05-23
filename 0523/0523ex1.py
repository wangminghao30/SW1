'''
2023-05-23
201995114
왕명호
#문제정의
      stu.txt 파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
#문제분석
      변수-한줄씩 읽어서 저장(score),리스트자료로 변환(scorelist)
          리스트에서 이름 항목 저장(name),합계(sum)
#알고리즘
      1.파일 열기(쓰기)
      2.파일 처리
          2.1 (반복)while True:
                    한 줄 읽어서 score저장
                    (선택)if score=='':
                            break
                    읽어온 내용을 리스트로 변환해서 scorelist저장
                    scorelist에서 첫번째 항목(이름)을 name변수에 저장
                    (반복) for i in range(1,4):
                            scorelist의 1,2,3항목의 값을 sum에 더하기
      3.파일 닫기
'''

f=open("/Users/wangminghao/Desktop/data/stu.txt","r")

while True:
    score=f.readline()
    if score=='':
        break
    
    scorelist=score.split()
    name=scorelist[0]

    sum=0
    for i in range(1,4):
        sum=sum+int(scorelist[i])

    print(name+"의 평균 성석은:%.1f"%(sum/3))
f.close()