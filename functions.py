def num (a,b):
    sum=a+b
    return sum #returning holds the answer if you dont print out

print(num(1,2))
# print("today")
# print(num(1,2))
# print("")
# num(1,2)
# print(num())
def check(a,c):
    b=a is "A"
    print(b)

    d="a" in c
    print(d)
check("a","laice")

def numbers(x):
    d=range(x[0],x[-1])
    for i in d:
        return i * 2
    print(numbers([1,2,3,9,4,5,6,8,7]))

#for loop
#4.Write a python function named divisible_by_seven that;using
#  the range function and a for loop return a list containing all 
# nummbers between 100 and 200 that are divisible by 7
def divisible_by_seven():
    empty=[]
    for i in range(100,200):
        if (i %7==0):
            empty.append(i)
    return empty
print(divisible_by_seven())

#another way
def divisible_by_seven():
    x=range(100,200)
    empty=[i for i in x if i % 7==0]#initialisation takes place(i)
    return empty
print(divisible_by_seven())

#Using for loop calculate the average of a list in a range of(55:100)
#to get average we say sum/number of elements
def average():
    sum=0
    x=range(55,100)
    for i in x:
        sum+=i
        avg=sum/len(x)
    return avg
print(average())

#for while-takes in the condition and the conditions inside it 
# keeps on running untill the condition is false.it has break and continue
    
    
  #using a while loop print a function to print prime numbers from 1-10
# start=2
# while(start<=10):
#     print(start)
#     start+=1


# def isPrime(num):
#     return all(num % i for i in range(2, int(num ** 0.5) + 1)) and num > 1

# for i in range(2, 10):
#     print(isPrime(i))

def primeNumbers(num):
    if num<2:
        return False
    
    for i in range(2,num):
        if(num%i==0):
            return False
            
    return True
num=0
while(num<10):
    if primeNumbers(num):
        print(num)
    num+=1



#write a function that takes one argument as list a=[2,4,6,8]
# and remove the second last item from that list without the removed item

# def list p=[2,4,6,8]
# list b=(lista[-2])
# print(list a.remove(list b))







   


  


