'''
2023-06-13
201995114
왕명호
'''
def findmax(a,b,c):
    if a>b:
        biggist=a
    else:
        biggist=b

    if biggist<c:
        biggist=c

    return biggist

num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))

biggist_number=findmax(num1,num2,num3)

print("가장 큰 숫자는:",biggist_number)