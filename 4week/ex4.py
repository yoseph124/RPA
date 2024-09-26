def sumfunc(num1):
    sum1=0
    if  num1 > 0:
        for i in range(1,num1+1):
            sum1=i+sum1
        print(f"1~{num1}까지의 정수의 합은 {sum1}입니다.")
        return
    else:
        print("1이상의 정수를 입력하세요")
        return

a=int(input("1이상의 정수를 입력하시오 : "))
sumfunc(a)
