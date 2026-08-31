import string
import sys

# function of encrypting by replacing it with the letter in the same index of the alphabet as it is in the key
def main(key):
    # takes input and opens an empty list to store the cypher text
    plaintext = str(input("Plaintext:  "))
    Cyphertext = []
    
    #checking if the letter is a letter and then matching it with the conressponding letter in the key
    for i in range(len(plaintext)):
        if plaintext[i] in string.ascii_lowercase:
            Cyphertext.append(key[string.ascii_lowercase.index(plaintext[i])])
        elif plaintext[i] in string.ascii_uppercase:
            Cyphertext.append(key[string.ascii_uppercase.index(plaintext[i])].upper())
        else:
            Cyphertext.append(plaintext[i])
    print("Ciphertext: ", ''.join(Cyphertext))

#checking for length of argument(that is the key), if it contains all the alphabet and then runing it
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("function must take exactly one argument")
        sys.exit(1)
    elif sys.argv[1].isalpha() == False :
        print("Key must only contain alphabetic characters")
        sys.exit(1)
    elif not len(sys.argv[1]) == 26:
        print("Key must contain 26 characters")
        sys.exit(1)   
    elif len(sys.argv[1]) == 26:
        R = False
        for i in range(len(sys.argv[1])):
            for i in string.ascii_lowercase or string.ascii_uppercase:
                if i not in sys.argv[1].lower():
                    R = True
                    break
        if R == True:
            print("Key must contain each letter exactly once")
            sys.exit(1)       
        else:
            main(sys.argv[1])
            
            
'''due to the fact that the previous project was similar to this one, this code took me 2 hrs to write, faster and better and i am getting better at using the name ==  main function and sys too. so unto the next one i guess, we resume tommorrow.'''