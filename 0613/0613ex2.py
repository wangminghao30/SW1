'''
2023-06-13
201995114
왕명호
'''
def dnumber(num,num_list):
    for i in range(1,num+1):
        if num%i==0:
            num_list.append(i)

num=int(input("자연수 입력:"))
num_list=[]

if num>0:
    dnumber(num,num_list)
    print(num,"의 약수:",num_list)

else:
    print("자연수가 아니다.")
