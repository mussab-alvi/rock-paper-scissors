import random
'''
1 for rock
2 for paper 
3 for scissor 
'''
com =random.choice([1,2,3])
youstr=input("Enter the choice (r/rock, p/paper, s/scissor)")
youdict = {"r":1, "rock":1, "p":2, "paper":2, "s":3, "scissor":3}
reverseddict = {1:"rock", 2:"paper", 3:"scissor"}

i=youdict[youstr]

print(f"your choice is: {reverseddict[i]}\ncomputer choose: {reverseddict[com]}" )

if (com==i):
    print("Its a draw !!! ")
else:
    if(com==1 and i==2):
        print("You won, Congratulations champ !!!")
    elif(com==1 and i==3):
        print("You lose, Try your luck next time !!!")
    elif(com==2 and i==3):
        print("You won, Congratulations champ !!! ")
    elif(com==2 and i==1):
        print("You lose, Try your luck next time !!! ")
    elif(com==3 and i==2):
        print("You lose, Try your luck next time !!!")
    elif(com==3 and i==1):
        print("You won, Congratulations champ !!! ")
    
    else:
        print("Something went wrong ....")