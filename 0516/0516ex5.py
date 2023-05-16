'''
2023-05-16
201995114
왕명호
파일 입출력 - writelines()->리스트나 튜플 같은 자료형을 파일에 출력
                      ->리스트나 튜플의 자료형은 문자열 이어야 한다.
         - write()->문자열만 파일에 출력
'''

L1=['충청남동','충청북도\n','전라남도','전라북동\n','경상남동','경상북동\n']

L2=[1,2,3,4,5]

with open("/Users/wangminghao/Desktop/data/linetest.txt","w") as f:
  f.writelines(L1)