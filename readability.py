#coleman liau index
#index = 0.0588 * L - 0.296 * S - 15.8
#where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

import math



#check for its number of letters which is per word, a word is group of letters without space or without "."this was the first code i wrote to check for words , the second is better and so i picked that , but i did not remove this one 
'''w = 0
i =0 

print(len(text))
if len(text) == 0:
    w = 0

elif len(text) > 0 and text != '.' :
    for i in range(len(text)-1) :
        if text[i] == " "  and  text[i+1] !="."   :
            w += 1
        elif text[i] == '.' and text[i+1] != " " :
            w += 1
    if text[-1] == ".":
            w += 1
            


print(w)
'''

#take input from user 
text_taken = str(input("text: "))
text= text_taken.lower()

#alphabets and signs that indicate the end of a sentence
alphabets = "abcdefghijklmnopqrstuvwxyz"
signs = '.!:;?'

#boolean value for confirming if its a word and counts for letters, words and sentences
word = False
letter = 0
word_count = 0
sentence_count = 0

# checking if a word was entered as text and how many letters it contains
for i in text:
    if i in alphabets:
        letter += 1
        word = True


#checking to get the number of words and sentences
if word == True:
    if len(text) == 0:
        word_count = 0
    elif len(text) > 0   :
        for i in range(len(text)):
            if text[i] != " " and text[i-1] == " ":
                word_count += 1
        if text[0] != ' ':
            word_count += 1
    for i in text:
        if i in signs:
            sentence_count += 1
            
# just added this to check if the logic was working
print(f'you have {word_count} word(s) and {sentence_count} sentences(s) and {letter} letters')

l = (letter / word_count) * 100
s = (sentence_count / word_count) * 100

#colemans index
index = 0.0588 * l - 0.296 * s - 15.8
print(index)

#logic for grading 
if round(index) < 1:
    print("Before Grade one ")
elif round(index) >= 16:
    print("Grade 16+")
else :
    print(f'Grade {round(index)}')
    
    
    
    
    
'''so i know you are probably saying this is a python code and it should be clean and brief, bare with me , i am restarting my journey with the goal of mastery, this code took longer than it was supposed to and while there was other factors, the major one is assumptions. read and understand what is really required of you before coding, check documentation for way to do it cleaner and in fewer codes. the first code was a different way i thought to count words , the second one is the better way. i also did not know what counted as a sentence or how it ends, shocking but a simple research would have saved me time, effort and embarrassment , but it is all part of the journey, see you in the next one '''