hours1 = input("enter the hours worked: ")
hours = int(hours1)
rate1 = input("enter the rate: ")
rate = int(rate1)

if hours < 40:
    salary = hours*rate
    print(salary)
else:
    salary = (hours*rate + (hours - 40)*rate*0.5) 
    print(salary)    