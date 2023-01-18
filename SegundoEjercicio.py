name = input ("enter your name please:")
hours1 = input("enter the hours worked: ")
hours = float(hours1)
rate1 = input("enter the rate: ")
rate = float(rate1)

if hours < 40:
    salary = hours*rate
    print(salary)
else:
    salary = (hours*rate + (hours - 40)*rate*0.5) 
    print(salary)

list1 = [name, salary]
print(list1)