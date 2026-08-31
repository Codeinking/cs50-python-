
#function to check the grade of the person who wrote or read the text
def calculate_coleman_liau(text):
    
    #a variable with a logic that checks if it a letter and summing them up
    letters = sum(1 for char in text if char.isalpha())
    
    #a variable that takes the counts the number of words inputed in the argument by check for space
    words = len(text.split())
    
    # a variable that stores the number of sentences in the text
    sentences = sum(1 for char in text if char in ['.','!','?',';'])
    
    print(f'{words},{sentences},{letters}')
    
    #logic for the grading of the reader
    if words == 0:
        return "Before Grade 1"

    #the formula and variables for calulating the grades
    l = (letters / words) * 100
    s = (sentences / words) * 100
    
    index = round(0.0588 * l - 0.296 * s - 15.8)
    
    
    if index >= 16:
        return "Grade 16+"
    elif index < 1:
        return " Before Grade one "
    else:
        return f"grade{index}"
    


#taking the text from the users and printing the result
user_text = input("Text: ")
print(calculate_coleman_liau(user_text))