'''
2023-06-07
201995114
왕명호
'''

phone=dict()

for i in range(5):
    id=int(input(str(i+1)+"번쩨 학생 학번 입력:"))
    pnum=input(str(i+1)+"번쩨 학생 전화번호:")

    phone[id]=pnum

print("학생 전화번호부 완성")

id=(int(input("검색을 원하는 학번 입력:")))

if id in phone:
    print("입력한 학생의 전화번호:",phone[id])

else:
    print("입력한 학생의 전화번호가 없습니다.")