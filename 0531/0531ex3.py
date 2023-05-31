'''
2023-05-31
201995114
왕명호
'''
fruit=('사과','배','파일애플','포도')
price=(5000,7000,4500,6000)

fp_list=[]

for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])

print("과일:",fruit)
print("가격:",price)
print("과일+가격 리스트:",fp_list)