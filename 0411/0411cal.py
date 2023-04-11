'''
2023.04.11
왕명호
'''
num1=int(input("정수1 입력:"))
op=input("문자열 입력:")
num2=int(input("정수2 입력:"))

if  op == "+":
  num3 = num1 + num2
  print("num3={}".format(num1+num2))
elif op == "-":
  num3 = num1 - num2
  print("num3={}".format(num1-num2))
elif op == "*":
  num3 = num1 * num2
  print("num3={}".format(num1*num2))
else :
  num3 = num1 / num2
  print("num3={}".format(num1/num2))