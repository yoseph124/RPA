i=0
num=int(input("1~9 사이의 정수 입력\n"))

if num>0 and num<10:
    for i in range(1,10):
        print(f"{num} X {i} = {num*i}")
else:
    print("1~9 사이의 수를 입력하세요")