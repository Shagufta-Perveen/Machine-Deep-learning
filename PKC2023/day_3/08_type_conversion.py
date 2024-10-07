x=10
y=10.2
z="Hello"

x=x*y

print(type(x))

#implicit type conversion
x=x+y
print(x,"type of x is:",type(x))


#explicit type conversion using int() and float() functions
age=input("What is your age")
print(type(int(age)))