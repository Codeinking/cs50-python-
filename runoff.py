import sys
from collections import Counter
from statistics import mode

#function taking multiple arguments
def runoff(*candidates):
    #variables to store data as the code runs
    voters = []
    voters_first_choice = []
    voters_first_choice_count = []
    voters_last_choice = []
    winner = " "
    
    #quering for number of date and looping till the appropriate input is given
    no_of_voters = input("how many voters are participating: ")
    while not str(no_of_voters).isdigit() or int(no_of_voters) < 1:
        no_of_voters = input("put a valid number: ")
    
    #taking the voters top 3 choices and checking if they are part of the candidates running before adding the votes   
    for i in  range(int(no_of_voters)):
        first = input("First: ")
        second = input("Second: ")
        third = input("Third:  ")
        newline = print("\n")
        if first and second and third  in sys.argv[1:]:
            if first not in sys.argv[1:]:
                print("invalid ballot")
            elif second not in sys.argv[1:]:
                print("invalid ballot")
            elif third not in sys.argv[1:]:
                print("invalid ballot")
            else:
                votes=[]
                votes.extend([first,second,third])
                voters.append(votes)
        else:
            print("invalid ballot") 
            
    #taking into account the first and last choices of the voters
    for i in range(len(voters)):
        voters_first_choice.append(voters[i][0])
        voters_last_choice.append(voters[i][2])
    
    #taking the counts for the first choice
    for i  in reversed(sorted(Counter(voters_first_choice).values())):
        voters_first_choice_count.append(i)
    
    #checking for a winner is only one person voted 
    if len(voters_first_choice) == 1:
        winner = voters_first_choice[0]
        print("The winner is " + f'{winner}')

    #if multiple people voted  and the logics to declaring a winner
    elif len(voters_first_choice) > 1:
        
        # a clear winner with over 50% of the votes
        if voters_first_choice_count[0] > (sum(voters_first_choice_count)/2):
            winner = mode(voters_first_choice)
            print("The winner is " + f'{winner}')
        
        #if no clear winner, the runnoff elction where the least like candidate is deleted from the ballot and the new favourite is voted
        else: 
            voters_first_choice = []
            voters_first_choice_count = []
            for i in range(len(voters)):
                voters[i].remove(mode(voters_last_choice))
            for i in range(len(voters)):
                voters_first_choice.append(voters[i][0])  
                 
            for i  in reversed(sorted(Counter(voters_first_choice).values())):
                voters_first_choice_count.append(i)    
            
            if voters_first_choice_count[0] > (sum(voters_first_choice_count)/2):
                winner = mode(voters_first_choice)
                print("The winner is " + f'{winner}')    
        
     
#running the function
if __name__ == "__main__":
    runoff(sys.argv[1:])