def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":  # 실행을 시킨 파일이 메인
    print(add(1, 2)) # 다른 파일에서 import하면 if문의 코드가
    print(sub(3, 4)) # 실행되지 않는다.
else: 
    print(__name__)