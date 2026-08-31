import sys 
import string
'''basically this is a code that takes two inputs from the user, the first is the key to which the second which is the plaintext is to be encripyted with (basically how many it would move by). there are other conditions like taking one argument in the function and printing the error, if more than one is given, the key has to be a positive integer and no matter how long it is , it is just supposed to wrap round the 26 alphabet '''



'''the function takes the key as an argument and then it takes the plaintext as an input from the user, then it checks if the character is in the alphabet or not, if it is then it adds the key to the index of that character and appends it to a list, if it is not then it just appends the character to the list, then it checks if the character is uppercase or not and if it is then it adds the index of that character to a list, then it checks if the character is a number or not and if it is then it just appends it to the list, then it checks if the character is a sign or not and if it is then it just appends it to the list, then it checks if the character is a space or not and if it is then it just appends it to the list, then it checks if the character is a letter or not and if it is then it just appends it to the list, then it checks if the character is a number or not and if it is then it just appends it to the list, then it checks if the character is a sign or not and if it is then it just appends it to the list, then it checks if the character is a space or not and if it is then it just appends it to the list, then finally it prints the cyphertext by joining all the characters in the list together.'''

#main function
def main(key):
    
    #variables to check for letters and words and sentences
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    signs = string.punctuation 
    numbers = string.digits
    text = str(input("Plaintext:  "))
        
    #empty list to store cypher, and the cyphertext and the letter to capitalize
    cypher = []
    cyphertext = []
    capital_index = []
    j = 0

    #loop and logic to convert the text to cypher text
    for i in  range(len(text)):
        if text[j] in alphabet or text[j] in alphabet_upper:
            if text[j].isupper():
                cypher.append(str((alphabet_upper.index(text [j]))+ key % 26))
                capital_index.append(j)
            else:
                cypher.append(str((alphabet.index(text [j]))+ key % 26))
            j +=  1
        elif text[j] in numbers:
            cypher.append(int(text[j]))
            j += 1
        elif text[j] in signs or text[j] not in alphabet :
            cypher.append(str(text[j]))
            j += 1
                        

    for i in range(len(cypher)):
        if str(cypher[i]) in signs or str(cypher[i]) == " " :
            cyphertext.append(cypher[i])
        elif cypher[i] is int:
            cyphertext.append(str(cypher[i]))
        else:
            m = int(cypher[i]) % 26
            cyphertext.append(alphabet[m])

    #loop and logic or capitilization
    for i in range(len(cyphertext)):
        if i in capital_index:
            cyphertext[i] = cyphertext[i].upper()
    
    #printing the words        
    print("CypherText: {}".format("".join(cyphertext)))
                

#logic to check for number of argument in the function, and if it is digit and then run the code 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python caesar.py key")
    elif not sys.argv[1].isdigit():
        print("Key must be a positive integer")
        sys.exit(1)
    else:
        main(int(sys.argv[1])) 
        
        
''' i do not know who invented auto complete in vscode, but may God continue to bless them, see the second comment up there, i didnt type that shit, explained my whole code, it also helps with ideas too like the name to main function under, helped with that. but as always computer can not replace the human mind, i still had to come up with all the logic. this code took 2 days(12 hrs  total) , i genuinely thought i would be faster but still got a long way to go. i used more models and libs which shows growth i guess '''