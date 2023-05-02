'''
2023-05-02
201995114
왕명호
파이썬 내장함수
'''

#자료형 변환 함수
s='123114' 

ch1=int(s) 
ch2=list(s)
ch3=tuple(s)
ch4=set(s)

print('{}의 자료형은 {}'.format(ch1,type(ch1)))
print('{}의 자료형은 {}'.format(ch2,type(ch2)))
print('{}의 자료형은 {}'.format(ch3,type(ch3)))
print('{}의 자료형은 {}'.format(ch4,type(ch4)))

print()
num1=abs(-5)
num2=round(4.6)
num3=bin(10)
str1=chr(97)
str2=ord('A')

print('-5의 절대값:',num1)
print('4.6의 반올림값:',num2)
print('정수10의 이진수값:',num3)
print('97에 해당하는 문자:',str1)
print('A의 아스크코드 값:',str2)

print()

num10=[6,3,5,1,9,2,8]
print('num10 원소의 길이:',len(num10))
print('num10 원소 중 가장  큰 값:',max(num10))
print('num10 원소 중 가장  작은 값:',min(num10))
print('num10 원소들의 합계:',sum(num10))
print('num10 원소들 정렬:',sorted(num10))

print()

print(zip('123',('wang','lee','part')))

print(list(zip('123',('wang','lee','part'))))

print(tuple(zip('123',('wang','lee','part'))))