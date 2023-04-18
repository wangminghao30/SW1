'''
2023.04.18
왕명호
두 정수 입력 x>y->x//y, x<y->x+y, x==y->x*y
단,나눗셈 몪 계산할 때 y는 0 안됨
#문제분석
    변수:
        x,y
    수식
#알고리즘
'''

x = int (input("x의 값을 입력:"))
y = int (input("y의 값을  입력:"))

if x > y :
    if y == 0:
        print ("y의 값이 0입니다.")
    else:
        print ("{}//{}={}".format(x,y,x//y))
elif x < y :
    print ("{}+{}={}".format(x,y,x+y))
else :
    print("{}*{}={}".format(x,y,x*y))