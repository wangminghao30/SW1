'''
2023-05-30
201995114
왕명호
시퀀스 자료형-문자열 메소드 연습
'''
st=input("영어 문장 입력:")

print=("입력된 문자의 길이:",len(str))
print=("입력받은 문장의 첫 문자만 대문자:",st.capitalize())
print=("입력받은 문장의 각 단어의 첫 글자 대문자:",st.title())
print=("모두 대문자로:",st.upper())
print=("모두 수문자로:",st.lower())
print=("문자열에서 a의 갯수:",st.count('a'))
print=("모두 문자열로 구성되었는가:",st.isalpha())
print=("스페이스의 갯수:",st.count(''))
print=("스페이스를 삭제한 문장:",st.replace('',''))