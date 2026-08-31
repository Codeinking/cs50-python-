# takes user name and welcomes them

n = input ("what is your name: ")
print( "hello",n,"you are welcome")
print(f'hello,{n}')

candidates = ["alice" , "bob", "charlie"]

new = dict.fromkeys(candidates, "unlocked")
    
   
print(new)

new["alice"] = "locked"
print(new)