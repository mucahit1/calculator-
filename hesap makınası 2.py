def add(a, b):
   return a + b
def subtract(a, b):
   return a - b
def multiply(a, b):
   return a * b
def divide(a, b):
 return a / b
print("İşlemi seçiniz.")
print("+")
print("-")
print("*")
print("/")
# User input
choice = input("Islemı onayla:")
A = int(input("Bırıncı rakam: "))
B = int(input("Ikıncı rakam: "))
if choice == '+':
   print(A,"+",B,"=", add(A,B))
elif choice == '-':
   print(A,"-",B,"=", subtract(A,B))
elif choice == '*':
   print(A,"*",B,"=", multiply(A,B))
elif choice == '/':
   print(A,"/",B,"=", divide(A,B))
else:
    print("Invalid input")