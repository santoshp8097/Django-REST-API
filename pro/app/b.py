'''
import time

def fibonacci(numeric):
    if numeric<0:
        print("Incorrect Input")
    elif numeric<=2:
        return 1
    elif numeric ==3:
        return 2
    else:
        return fibonacci(numeric-1) + fibonacci(numeric-2)

number = int(input("Enter the number which you want to check in fibonacci sequence:"))    
if number < 0:
    print("please enter the valid number")
else:
    start_time = time.time()
    numeric = int(number)
    print("The number you have entered the :",numeric)
    output = fibonacci(numeric)
    print("{} is the {}th element the fibonaci sequence".format(output,numeric))
    end_time = time.time() - start_time
    latency = str(end_time)[0:3]
    print(latency)
'''

lst = filter(lambda x : x % 2 == 1, range(1, 20)) 
print(lst)