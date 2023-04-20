#Write a function that uses while, if and continue statements
#to print all the even numbers between 0 and 50. 
 
def continue_even():
    x=0
    while x<=50:
        x+=1
        if (x%2!=0):
         continue
        print(x)

#Write a function that takes an integer argument and prints "Prime"
#if the number is prime, and "Not prime" if the number is not prime.

def prime_not_prime(i=5):
    if(i%1==0 and i%5==0):
        print(f"{i} is a prime")
    else:
        print(f"{i} is not prime")




#Write a function that takes a list of integers as input and prints 
#the sum of all the even numbers in the list.
def even_numbers(*nums):
    sum=0
    for i in nums:
        if i %2==0:
            sum+=i
    print (sum)
    
       

#Write a function that takes any two integers as input, and prints the sum of 
#all the numbers between the two integers(inclusive) that are divisible by 3.
def divisible_by_3(num):
    sum=0
    for i in range(1,num+1):
        if i%3==0:
           sum+=i
    print(sum)       
    








  

