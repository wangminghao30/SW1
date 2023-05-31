'''
2023-05-31
201995114
왕명호
#문제정의
   튜플안에 있는 숫자들의 종류와 반복 갯수 분석하기
#문제분석
#알고리즘   
'''
num=(1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,9,0)
num_list=[]

print("생성된 튜플:",num)

for i in range(len(num)):
    if num[i] not in num_list:
        num_list.append(num[i])
        print(num[i],"개수:",num.count(num[i]))

