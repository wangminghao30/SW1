'''
2023-05-17
201995114
왕명호
#문제정의
      기존파일을 새로운 파일에 복사하는 프로그램 만들기
#문제분석
      변수:원본파일입력(source),복사할파일 (target)
          원본파일의 내용(texts)

#알고리즘
      1.source에 원본파일 이름 입력
      2.target에 복사할파일 이름 입력
      3.파일처리
        source파일 객체생성
            한 줄식 읽어 오기
            내용을 texts변수에 저장
        target파일 객체생성
            texts파일 쓰기
        파일생성 메시지 출력
'''
source=input("source  파일 입력:")
target=input("target  파일 입력:")

with open("/Users/wangminghao/Desktop/data/linetest.txt","r") as f:
    texts=f.read()

with open("/Users/wangminghao/Desktop/data/copylinetest.txt","w") as fp:
    fp.write(texts)

    print(target+"파일이 생성되었습니다.")