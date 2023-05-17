'''
2023-05-17
201995114
왕명호
for문은 이용한 파일 읽이
'''

with open("/Users/wangminghao/Desktop/data/linetest.txt","r") as f:
    for line in f:
        print(line,end='')


print()

with open("/Users/wangminghao/Desktop/data/linetest.txt","r") as f:
    while True:
        line=f.readline()
        print(line,end='')

        if line=='':
            break
        
#readlines():한 줄씩 읽어서 리스트형으로 반환
with open("/Users/wangminghao/Desktop/data/linetest.txt","r") as f:
    textlists=f.readlines()
    print(type(textlists))
    print(textlists)



#print()함수로 파일에 출력하기
f=open("/Users/wangminghao/Desktop/data/ptest.txt","w")

print("aaaaaaa",file=f)
print("bbbbbbb",file=f)
print("ccccccc",file=f)

f.close()