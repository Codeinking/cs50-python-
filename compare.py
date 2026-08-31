# asking for input to from the user and cconverting it from string to integer
x = int (input("choose the first number to be compared:  "))
y = int (input("choose the second number to be compared:  ")) 

#logic to check for greater than, less than or equal to.
if x < y :
    print(f"{x} is less than {y}")
elif x > y :
    print(f"{x} is greater than {y}")
else :
    print(f"{x} is equal to {y}")