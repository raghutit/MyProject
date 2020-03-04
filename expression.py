n=int(input("Enter the value: "))

def fun(n):
    y = 1
    for i in range(1,20):
        y = y * n
        result = 1 / y
        print("%.3f" %result,end=' ')
        print("%.3f" %(1/n**i),end=' ')

fun(n)
