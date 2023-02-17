# write a function:
# adds two numbers
# dividing
# giving remainder

# sum1=eval(input("enter num1: "))
# sum2=eval(input("enter num2: "))

# def sum(num1,num2):
    # sum_1=(num1+num2)
    # print(sum_1)
# sum(sum1,sum2)


data=[]

while True:
    name=input("enter emails: ")
    data.append(name)

    choice=input("enter another?? (y/n) : ")
    if choice.casefold()=='n':
        break
for x in data:
    print(x)