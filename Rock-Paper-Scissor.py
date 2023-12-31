# Stone - Paper - Scissor 
import random
opt=["Stone","Paper","Scissor"]

results=[[0,1,-1],  #0=Draw
     [-1,0,1],      #1=Win
     [1,-1,0]]      #-1=Lose

while(True):
    print("\n1]Stone \t 2]Paper \t 3]Scissor")
    x=int(input("Choose any (1 or 2 or 3) : "))
    if(x>3):
        print("Wrong input !!")
    else:
        break

x=x-1 #for convinence
y=random.randrange(0,3)

print(f"You choose : {opt[x]}")
print(f"Oppents chooses : {opt[y]}")

res=results[y][x]

if(res==0):
    print("The game is draw")   
elif(res==1):
    print("Congrats You won the game")    
elif(res==-1):
    print("Hard Luck ! You Lose the game")
