
#function for the game of scrable, assigning points to each letter 
def scrable():
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    score = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]

    #taking the word from the user and converting to all upper case
    player_one = str(input("what is your word player: "))
    cap = player_one.upper()
    points_one = 0

    #summing up the points based on the letters in the word
    for i in cap:
        if i in alphabets:
            points_one = points_one + score[alphabets.index(i)]
     
    #propmpting the second user for same and doing the same   
    player_two = str(input("what is your word player_two: "))
    cap = player_two.upper()
    points_two = 0

    for i in cap:
        if i in alphabets:
            points_two = points_two + score[alphabets.index(i)]
            
    #checking for winner    
    if points_one > points_two:
        print("player one wins")
    elif points_two > points_one:
        print("player two wins")
    else:
        print("its a tie")

#running the function
scrable()

#need to add input sanitization 
#this should ensure words only contain letters and if they do not , reprompt user
#also try using range to create list rather than typing it 
#also check if it is possible to shorten the code especially the points calculation for both players