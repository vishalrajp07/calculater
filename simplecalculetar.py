# simple calculetar

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y



print("option")
print('1: add')
print('2: subtract')
print('3: multiply')
print('4: divide')

option = input("choose option 1/2/3/4 : ")
x = int(input("value 1 :"))
y = int(input("value 2 :"))

if option == '1':
    print(x, "+", y, "=", add(x, y))
elif option == '2':
    print(x, "-", y, "=", subtract(x, y))
elif option == '3':
    print(x, "*", y, "=", multiply(x, y))
elif option == '4':
    print(x, "/", y, "=", divide(x, y))
else:
    print("Invalid input")
# simple calculetar

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y



print("option")
print('1: add')
print('2: subtract')
print('3: multiply')
print('4: divide')

option = input("choose option 1/2/3/4 : ")
x = int(input("value 1 :"))
y = int(input("value 2 :"))

if option == '1':
    print(x, "+", y, "=", add(x, y))
elif option == '2':
    print(x, "-", y, "=", subtract(x, y))
elif option == '3':
    print(x, "*", y, "=", multiply(x, y))
elif option == '4':
    print(x, "/", y, "=", divide(x, y))
else:
    print("Invalid input")
