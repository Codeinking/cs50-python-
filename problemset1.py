
#introduction
print("Welcome to problem set one of cs50 as done by patrick Kingsley")

#prompt for user name 
name = input("What is your name: ")


#greeting user fucntion
def greet():
    
    print(f"hello, {name}")
    
    
#Calling the greet function    
greet()


#Prompting user for height of pyramid required , used a global vairiable so i can use it in multiple functions
n = int(input(f"{name}, How tall do you want your pyramid, Ranging from 1-8 blocks:  "))

#left sided pyramid 
def pyramid():    
    if 0<n<9:
        p ="#"
        for i in range(n+1):
            k = p * i
            #printing the pyramid with the iteration and range number 
            print(f'{k} {i} {n}')
            
        #Two left sided pyramid      
        for i in range(n+1):
            k = p *i
            print(f' {k}  {k} ')
            
    else :
        print("the number you picked is out of range")

          
          
#function for right sided and left sided pyramid         
def pyramid2():
    
    block=(' ',"#")
    if 0<n<9:
        i=1
        for i in range(0,n+1,1):
            space = block[0]*(n-i)
            hashb = block[1]*i
            print(space + hashb + block[0] + hashb)
        
        
    else:
        print("number you picked is out of range ")
            

          
#calling the function for creating the pyramids
pyramid()
pyramid2()