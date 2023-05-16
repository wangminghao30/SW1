'''
2023-05-16
201995114
왕명호
'''
ft=open("/Users/wangminghao/Desktop/data/test.txt","w")

for i in range(1,11):
    ft.write("%d번째 줄입니다.\n"%i)

ft.close()

