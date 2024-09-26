def sumfunc(num1):
    sum1=0
    for i in range(1,num1+1):
        sum1=i+sum1
    return sum1

a=int(input("1이상의 정수를 입력하세요 : "))

print(f"1~{a}까지의 정수의 합은 {sumfunc(a)}입니다.")