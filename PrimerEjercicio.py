hours = input("enter the hours worked: ")
rate = input("enter the rate: ")

if hours < 40:
    salary = hours*rate
    print(salary)
else:
    salary = (hours*rate + (hours - 40)*rate*0.5) 
    print(salary)    