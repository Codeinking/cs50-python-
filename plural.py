''''the code takes 3 argugments which are the names of the politcians which are running for the election, then the number of voters, which the voters are to be prompted who they want to vote and the candidate with the most number of votes wins 
'''


from py_compile import main
from collections import Counter
import sys
import statistics

#function taking multiple arguments and checking for the winner of an election 
def plural(*candidates):
    
    #variables for votes cast and the winners that were voted for
    votes = []
    winners = []
    
    
    #this was the previous code for taking the candidates for the ection as an input and logics to check for certain parameters. then i found out how to input multiple arguments in a function and did not need it again
    '''canditates = []
    
    
    
    no_of_candidates = input("Enter the number of candidates: ")
    while not str(no_of_candidates).isdigit() or int(no_of_candidates) <= 0 or int(no_of_candidates) > 9:
        if not str(no_of_candidates).isdigit():
            no_of_candidates = input("Please enter a valid digit number of candidates : ")
        elif int(no_of_candidates) <= 0:
            no_of_candidates = input("Please enter a valid positive number of candidates: ")
        elif int(no_of_candidates) > 9:
            no_of_candidates = input("Please enter a valid number of candidates (1-9): ")
    for i in range(int(no_of_candidates)):
        candidate = input("Enter the name of candidate: ")
        canditates.append(candidate)'''
        
       
    # quering for the number of people that are to vote
    no_of_voters = (input("Enter the number of voters: "))
    
    #ensuring the user is constantly being quered till a postive integer grater is inputed
    while not str(no_of_voters).isdigit() or int(no_of_voters) < 1:
        no_of_voters = (input("Please enter a valid number of voters: "))
    
    #loop and logic to cast vote, check validity of the vote and add it if valid
    for i in range(int(no_of_voters)):
        vote = str(input("Vote for your candidate: "))
        if vote not in sys.argv:
            print("invalid vote")
        else:
            votes.append(vote)
    
    
    #a list that is to hold just the names of the candidates that were voted for
    election_key = []
    for i in Counter(votes).keys(): 
        election_key.append(i)
    
    #a list to hold just the scores of the election
    election_value = []
    for i in Counter(votes).values():
        election_value.append(i)
     
    #logic and loop to check and declare the winner or winners as the case may be   
    for i in range(len(election_value)):
        if election_value[i] == max(election_value):
            winners.append(election_key[i])
        
    #printing the winners
    print( *winners, sep= "\n")


#function to run code and check for errors resulting from length of the argument 
if __name__ == "__main__":
    if len(sys.argv[1:]) < 2 or len(sys.argv) > 9 :
        print('number of candidates ranges from 2 to 9')
        sys.exit(1)
    else:
        plural(sys.argv[1:])
    
'''first thing i realized was the auto correct in vs code is doing the same thing with the keypads on our phone which offers you alot of advantages but also takes away somethings and in this case i think i would take it away and learn the codes properly cause not being able to solve the problems on my own is an issue for me. Now while i used it for this code going forward i would not use it, but it also helps with what cs50 are trying to introduce this week which is to improve your ability to analyze other peoples code and understand it, increasing your ability to work with other peoples code and contribute to a team. but as is always said the strongest team is based on the weekest link, so i am going to remove this training wheels and get my foundations solid before bringing them back in, i actually thought i had this underlock for a day next thing  i know day 3(avg 5 a day) but i eventually figured it out 
-asides the logic this problem had me learning more about dictionaries, functions and arguments, even printing style '''