team={ 
      "mahabad": 10,
      "tehran": 20,
      "kermansha": 5,
      "sanandag": 7
    
    }

def team_res(num):

    '''
    this function return a total Score, best_team, and those team will nex Competition
    and average
    '''

    total = 0 #considered the sum of the numbers to be zero
    max_persone= '' # i make a empty string for name max_presone
    ma = team["mahabad"]  # a considered the place holder is the first items in dic 
    count = 0 # a cna too use (len(num))
    
    for i, j in num.items(): # with useing by (items()) Set i equal to keys and j equal to value  (equal = مساوی)
        total += j 
        count += 1    # i use this (for), for Highest score 
         
        if j > ma:
            max_persone = i
            ma = j
            

    next_r = []       # i make a empty list for those team will to next game, and this line can't write under for
    
    for k, v in team.items(): # i use this (for) for that teams had more than 10 score 
        
        if 10 <= v:# i say  Print the teams that had more than 10 value

            next_r.append(k) # and i say in this line add or (for list) append name tht teams
            

        
    average = int (total / count) # i don't want my average is float for that i write a (int)
    
    return total, max_persone, next_r, average

total, max_person,  persone, average =team_res(team)

print(f' avreage teams : {average}')
print(f' total won : {total}')
print(f' best_team is {max_person}')
print(f' this teams go to next Competition {persone}')