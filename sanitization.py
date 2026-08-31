import re
#takes input and the function removes non degit from the input
credit_card =str(input(""))
def sanitize(credit_card):
    pattern = r'["0123456789"]'
    san_credit_card = re.sub(pattern,credit_card)
    print(san_credit_card)
    return san_credit_card   

sanitize(credit_card)