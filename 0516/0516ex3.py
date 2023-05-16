'''
2023-05-16
201995114
왕명호
파일 입출력 - 읽기(read()-전체 내용을 허나의 문자열로 반환)
'''

f=open("/Users/wangminghao/Desktop/data/test.txt","r")

txts=f.read()

print(txts)

f.close()