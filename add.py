def Input():
    num1=int(input('enter the first number'))
    num2=int(input('enter the second number'))
    return num1,num2

def addition():
    num1,num2=Input()
    Result=num1+num2
    return Result
   
def output():
    result=addition()
    print(result)

output()

