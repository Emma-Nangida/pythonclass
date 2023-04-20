def information(name,number):
    print(f"{name} have {number} children")

def details(name,county):
     print(f"Iam {name} from {county} county")
# keyword argument
def add(a,d):
     answer=a+d
     return answer
# position argument
def add(a,d):
     answer=a+d
     return answer
# function
def year_of_birth(name,age):
     year=2023-age
     print(f"my name is {name} Iam {age} years old")

def birth_year(name,age):
     year=2023-age
     print(f"{name} was born in {year}")

# default arguments
def my_nationality(nationality="Kenyan"):
     print(f"You are a {nationality}")


def greetings(*names):
     for name in names:
      print(f"greetings {name}")

def multiply(**nums):
    num=1
    for num in nums.values():
     answer*=nums

def sum_multiplication(sum,multiplication):
    return(f"The sum of 6 and 2 is {sum} and their product is {multiplication}")
# positional arguments
print(sum_multiplication(8,12))

def sum_multiplication(sum,multiplication):
    return(f"The sum is {sum} and the product is {multiplication}")
# positional arguments
print(sum_multiplication(8+3+2*8,12*8*2))

#defaults arguments
def names(firstname="a",secondname="b"):
    return(f"my name is {firstname} {secondname}")
print(names())
print(names(firstname="Emma"))
print(names(firstname="Emma",secondname="Nangida"))

def my_nationality(nationality="Kenyan"):
     return(f"You are a {nationality}")
print(my_nationality())

def firstname(*names):
    for name in names:
     print(f"my name is {firstname}")



def even_numbers():
    x=range(10)
    for i in x:
        if i %2==0:
            print()
     


     
     