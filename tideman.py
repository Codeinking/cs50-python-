'''The Tideman voting method (also known as "ranked pairs") is a rannked-choice voting method that's guaranteed to produce the condorcet winner of the elction if one exists. '''

'''the first solution to this method is finding the "source" that is a candidate that goes head to head with other candidates and wins making that candidate the condrcet winner'''

'''the last method which does not make the algorithm fair is that the head to head is to be represented by a graph with lines flowing in a circular motion from the winner of the head to head, to the loser. now because every candidate loses at least one of this head to head a closed cycle or circuit is created once the graph is drawn and that would mean no winner, so to ensure it remain open the head to head with the least margin is not added to the graph and the candidate that does not have an arrow pointing to him/her (i.e the person without any losses recorded ) is the winner of the election'''
import sys
from collections import Counter
from statistics import mode
from operator import itemgetter

def tideman(*candidates):
   
    u = 0
    len_of_candidate = len(sys.argv[1: ])
    candidates_pair = []
    for k in range(len(sys.argv[1: ])):
        j = u + 1
        for i in range(len_of_candidate-1):
            candidates_pair.append([sys.argv[1:][u],sys.argv[1: ][j]]) 
            if j+1 < int(len(sys.argv[1: ])):
                j += 1
            
                    
        u += 1
        len_of_candidate -= 1
       
        
  
    voters = input("how many voters are ready: ")
    ballot_paper = []
    ballot_box = []

    for i in  range(int(voters)):
        first  = input("1. ")
        second = input("2. ")
        third  = input("3. ")
        newline= print("\n")
        
        if first and second and third  in sys.argv[1:]:
                if first not in sys.argv[1:] :
                    print("invalid ballot")
                elif second not in sys.argv[1:] :
                    print("invalid ballot")
                elif third not in sys.argv[1:]  :
                    print("invalid ballot")
                elif first == second or first == third or third == second:
                    print("invalid ballot")
                    
                else:
                    ballot_paper.append([first,second,third])
        else:
            print("invalid ballot") 
    
    
    
    found = [] 
    found_count = []
    a = 0

    for a in range(len(candidates_pair)):
    
        for sublist in ballot_paper:
            temp_result = []
            temp_result_2= []
            for item in sublist:
                if item.startswith(candidates_pair[a][0]) or item.startswith(candidates_pair[a][1]):
                    temp_result.append(item)
            if len(temp_result) > 1 :        
                found.append(temp_result) 
    
        a += 1
    b = 0
    for _ in range(len(candidates_pair)):
        temp_result_2 = []   
        for sublist in found:
            temp_result = None
            if candidates_pair[b][0] in sublist and candidates_pair[b][1] in sublist:
                temp_result = sublist[0]
            if  temp_result != None:    
                temp_result_2.append(temp_result)
        found_count.append(temp_result_2)
        b +=1  
    
    
    a = 0
    for i in found_count:
        for items in Counter(i).items():
            candidates_pair[a].append(items)
        candidates_pair[a].append(mode(i))
        candidates_pair[a].append(max(Counter(i).values()) - min(Counter(i).values()))
        
        a+= 1
    
    
    sorted_new_candidate_pair = sorted(candidates_pair, key=itemgetter(-1), reverse=True)
    
    
    
    winner_chart = dict.fromkeys(sys.argv[1: ], "unlocked")
    
    
    for p in sorted_new_candidate_pair[:-1]:
        if p[-2] == p[0] :
            winner_chart[p[1]] = "locked"
        elif p[-2] == p[1]:
            winner_chart[p[0]] = "locked"

    a = 0
    for i,j in winner_chart.items():
        if j == "unlocked" :
            print(f'and your winner for this election is {i}')      
    
          
if __name__ == "__main__":
    if len(sys.argv) < 10:
        tideman(sys.argv[1: ])
    else:
        sys.exit(1)

'''this took me over a month and i did not even follow the project based on the instructions as the assignment was about completing a lot of already written code and i had to code all of mine using my idea of what the end result of the code is to look like, final touches and addidtion of comments and i would move on to the next, it also took me time cause i had to prepare for interviews that i had , prayers still being made, i need the job, then from there i can draw a map and find the balance to continue coding, programming would play a critical role in  my journey to the top. well i did not label or ccomment on the code as usual, exhausted at this point, there are thing i would like to type here but i can not ,cause it would mean accepting a fate that does not feel like the truth, non the less i have to keep pushing, see you in the next task.'''