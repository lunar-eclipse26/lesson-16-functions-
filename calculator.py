def add(p, q):
    return p+q

def sub(p, q):
    return p - q

def multi(p, q):
    return p * q

def div(p, q):
    return p / q

print("pwease select operation :3")
print("a. add :3")
print("b. subtract :3")
print("c. multiply :3")
print("d. divide :3")
choice = input("pwease enter a choice :3 (a/b/c/d):")
num1 = int(input("pwease enter the first number :3 :"))
num2 = int(input("pwease enter ur second number :3 :"))
if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 'b':
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multi(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", div(num1, num2))
else:
    print("erm critical error please reboot ur device completely")