def even_numbers():
    x=range(10)  #range gives you a sequence of values
    for i in x:
        if i %2==0:
            print(x)

def divisible_by_five():
    x=range(50)
    for i in x:
        if i%5==0:
             print(f"{i}is divisible_by_5")
        else:
            print(f"{i}is not divisible_by_5")
def multiple_comparison():
    x=range(50)
    for i in x:
        if i %5==0:
            print(f"{i}is divisible_by_7")
            
        else:
            print(f"{i}is not divisible_by_7")

def odd_or_even():
    x=range(20)
    for i in x:
        if i %2==0 and i%3==0:
            print(f"{i}is divisible_by both 2 and 3")
        elif i%2==0 or i %3==0:
            print(f"{i}is divisible_by either 2 or 3")
        else:
            print(f"{i}is not divisible by eithe 2 or 3")

def while_loop():
    x=1
    while x<10:
        print("hello")
        x+=1

def break_statement():
    x=1
    while x<10:
        print("Hello")
        x+=1
        if x==5:
            break  

def continue_statement():
    x=0
    while x<=20:
        x+=1
        if x%3==0:
            continue
        print(x)
def less_than():
        i = 20
        if (i <= 15):
         print("i is smaller than 15")
         print("i'm in if Block")
        else:
         print("i is greater than 15")
         print("i'm in else Block")
        print("i'm not in if and not in else Block")

#3.write a python function named smallest that accepts
#  a list of unsorted integers and returns the smallest number 
# in the list.example:
#a.smallest([3,6,8,2,4,1,5,7])

#4.write a python function named di







                