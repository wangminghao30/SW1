'''
2023-05-16
201995114
왕명호
파일 입출력 -seek(o):파일의 처음으로 포인트 이동
         -read(int n):지정한 갯수만큼 파일 읽어 오기
'''

f=open("/Users/wangminghao/Desktop/data/test.txt","r")

print(f.read(10),end="")
print(f.read(10),end="")
print(f.read(10))

f.seek(0)

print(f.read(10),end="")
print(f.read(10),end="")
print(f.read(10))

f.close()