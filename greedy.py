#taking input for the cost of the production and how much the customer has to pay
cost = int(input("how much does the product you want to buy cost?:  "))
payment = int(input("how much have you got: "))

#the denominations the change comes in
change = [5, 10 , 25, 1]
sorted_change= tuple(sorted(change, reverse=True))


# number of Change to be given to the customer
noc = 0

#balance to be returned to customer
balc = payment - cost
oldc =  balc

# vairiables used in the loops and conditionals 
i = 0 
shit = [0,0,0,0]

#ensuring the code runs as long as the customers is being owed 
if balc >= 0:
    while balc >0:  
        while balc>= sorted_change[i]:
            balc = balc - sorted_change[i]
            noc = noc +1
            shit[i] += 1   
        i += 1
        
#informing the customer that they owe and not the other way around        
else:
    debt = -1 * balc
    print(f' you owe us {debt}')   

    
    #final output
print(f"{oldc} was customer's balance, the total number of coins given to the customer was {noc}, it came in {shit[0]}(25c's), {shit[1]}(10c's), {shit[2]}(5c's), {shit[3]}(1c's)")