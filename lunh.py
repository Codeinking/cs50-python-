#input credit card 
credit_card = input("insert credit card number: ")

#varibales to check for which credit card the customer is using and what bank they belong to 
amex = ("34", "37")
mastercard = ("51", "52", "53", "54", "55")
visa = ("4")
card_status = False
b = 0
bank = ["amex", "mastercard","visa"]



#Checking the card number for which bank they belong to if they are valid 
if credit_card[0] == visa[0] and (len(credit_card)==13 or len(credit_card)==16):
    card_status = True
    b = 2
    
elif credit_card[0]+credit_card[1] in mastercard and len(credit_card)==16:
    card_status = True
    b = 1
        
elif credit_card[0]+credit_card[1] in amex and len(credit_card)==15:
    card_status = True
    b = 0
    
else:
    card_status = False
    
    
   
#using luhn's algorithm
if card_status== True:    

    #first step of luhn, making a list of the card number,reversed and in steps of two
    total_list_1 = []
    
    #each individual number in the list is to be multiplied by 2 and stored in this new list
    total_list = []
    
    #loop for getting the new lists
    for i in (reversed(credit_card[0::2])):
        total_list_1.append(i)
        total_list.append(str(int(i)*2))
        
    
        
    #varible to store sum of individual numbers of the total list 
    total_sum = 0
    
    #loop for doing so
    for i in total_list:
        if len(i)>1 :
            total_sum = total_sum + int(i[0]) + int(i[1])
        else:
            total_sum = total_sum + int(i)

    #a list of the numbers in the credit card that were not used in the first part of the equation 
    total_list_2 = []
    
    #loop to fill the list and get the sum of the numbers plus the total of the previous list
    for i in (reversed(credit_card[1::2])):
            total_list_2.append(i)
            total_sum = total_sum + int(i)
    
    
    # turned total_sum into a string so it could be iterated
    mod_number = str(total_sum)

    #checking if the total_sum is a module of 10
    if mod_number[-1] == "0":
        card_status = True
    else:
        card_status = False
        
else:
    card_status = False
    

#checking if the card is valid
if card_status == True:
    print(bank[b])
else:
    print("invalid")