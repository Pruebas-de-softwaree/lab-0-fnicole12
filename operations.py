def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    #Suma
    print(add(2,5))
    print(add(-10,4))
    print(add('a','b'))

    #Subract
    print(subtract(10, 5))
    print(subtract(-5, 5))

    #Multiply
    print(multiply(7, 2))
    print(multiply(-10, 4))

    #Divide
    # print(divide(2, 0))
    print(divide(10, 5))
    print(divide(5, 3))

    #Power
    print(power(2, 2))

    print("end test")

