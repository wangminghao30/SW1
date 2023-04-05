'''
2023.04.05
왕명호
본봉과 수당을 정수로 입력 받아서 이번달 월급 수령액 구하는 프로그램
(세금은 총액의 20%)(p116-9)
'''
sal=int(input("본봉:"))
allo=int(input("수당:"))

tax=(sal+allo)*0.2
total_sal=sal+allo-tax

print("본봉이 {}이고, 수당이 {}일때 실수령액은 {}이디.".format(sal,allo,total_sal))