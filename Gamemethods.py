import random
import numpy as np

brain=np.zeros((16,16))

Reward=np.array([[-1,-1,0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#0
                 [-1,-1,0,0,-1,0,-1,0,-1,-1,-1,-1,-1,-1,-1,-1],#1
                 [0,0,-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],#2
                 [0,0,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,-1],#3
                 [-1,-1,0,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1],#4
                 [-1,0,-1,-1,0,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1],#5
                 [-1,-1,-1,-1,-1,0,-1,0,-1,-1,-1,0,0,-1,-1,-1],#6
                 [-1,0,-1,-1,-1,-1,0,-1,0,-1,-1,-1,-1,0,-1,-1],#7
                 [-1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,-1],#8
                 [-1,-1,-1,-1,0,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1],#9
                 [-1,-1,-1,-1,-1,0,-1,-1,-1,0,-1,0,-1,-1,-1,-1],#10
                 [-1,-1,-1,-1,-1,-1,0,-1,-1,-1,0,-1,-1,-1,-1,100],#11
                 [-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1,0,-1,100],#12
                 [-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,0,-1], #13
                [-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,0,-1,-1],#14
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0,-1,-1,100]]#15
               )
def changeTreasureLocation(location):
    for i in range(len(Reward)):
        for j in range(len(Reward)):
            if Reward[i][j]==100:
                Reward[i][j]=0
    for k in range(len(Reward)):
        if Reward[k][location]!=-1:
            Reward[k][location]=100
    return location
def randomSearch(state,T):
    count=0
   
        
    while(state!=T):
            
        updateMapLocation(state)
        print(Tmap)
#pick a random action 
          #  print(state)
        A=[]
        for i in range(len(Reward)):
            if Reward[state][i]!=-1:
                A.append(i)
        Rnum=random.randint(0, len(A)-1)
        action=A[Rnum]
#find the next state where the action takes you
        nextstate=action
#get max value of all actions in the current state
        brainV=[]
        for i in range(len(brain)):
            brainV.append(brain[nextstate][i])
        maxV=max(brainV)

            
        state=nextstate
        count+=1
        nextstate=action
        
    return count
Tmap=np.array([[100,0,0,0], #1 is where you are 100 is treasure
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,1]
             
             
             ])

def updateTreasureMap(location):
    for item in Tmap:
        for i in range(len(Tmap)):
            if item[i] ==100:
                item[i]=0

    if location==0:
        Tmap[3][3]=100
    if location==1:
        Tmap[2][2]=100
    if location==2:
        Tmap[3][2]=100
    if location==3:
        Tmap[2][3]=100
    if location==4:
        Tmap[3][1]=100
        
    if location==5:
        Tmap[2][1]=100
    if location==6:
        Tmap[1][1]=100
    if location==7:
        Tmap[1][2]=100
    if location==8:
        Tmap[1][3]=100
    if location==9:
        Tmap[3][0]=100
    if location==10:
        Tmap[2][0]=100
    if location==11:
        Tmap[1][0]=100
    if location==12:
        Tmap[0][1]=100
    if location==13:
        Tmap[0][2]=100
    if location==14:
        Tmap[0][3]=100
    if location==15:
        Tmap[0][0]=100
def updateMapLocation(location):
    if location==0:
        Tmap[3][3]=1
    elif Tmap[3][3]!=100:
        Tmap[3][3]=0 
        
    if location==1:
        Tmap[2][2]=1
    elif Tmap[2][2]!=100:
        Tmap[2][2]=0
        
    if location==2:
        Tmap[3][2]=1    
    elif Tmap[3][2]!=100:
        Tmap[3][2]=0
        
    if location==3:
        Tmap[2][3]=1
    elif Tmap[2][3]!=100:
        Tmap[2][3]=0
        
        
    if location==4:
        Tmap[3][1]=1
    elif Tmap[3][1]!=100:
        Tmap[3][1]=0
        
    if location==5:
        Tmap[2][1]=1
        
    elif Tmap[2][1]!=100:
        Tmap[2][1]=0
        
    if location==6:
        Tmap[1][1]=1
    elif Tmap[1][1]!=100:
        Tmap[1][1]=0
        
    if location==7:
        Tmap[1][2]=1
        
    elif Tmap[1][2]!=100:
        Tmap[1][2]=0
        
    if location==8:
        Tmap[1][3]=1
    elif Tmap[1][3]!=100:
        Tmap[1][3]=0
        
    if location==9:
        Tmap[3][0]=1
    elif Tmap[3][0]!=100:
        Tmap[3][0]=0       


    if location==10:
        Tmap[2][0]=1
    elif Tmap[2][0]!=100:
        Tmap[2][0]=0 
        
    if location==11:
        Tmap[1][0]=1
    elif Tmap[1][0]!=100:
        Tmap[1][0]=0 
        
    if location==12:
        Tmap[0][1]=1
    elif Tmap[0][1]!=100:
        Tmap[0][1]=0 
    
    
    if location==13:
        Tmap[0][2]=1
    elif Tmap[0][2]!=100:
        Tmap[0][2]=0 
    if location==14:
        Tmap[0][3]=1
        
    elif Tmap[0][3]!=100:
        Tmap[0][3]=0 
        
    if location==15:
        Tmap[0][0]=1
    elif Tmap[0][0]!=100:
        Tmap[0][0]=0
def findTreasure(state,brain,location):
    while(state!=location):
        print(state)
        bestactionL=[]
        for i in range(len(brain)):
            bestactionL.append(brain[state][i])
        bestVal=max(bestactionL)
        for j in range(len(brain)):
            if bestVal==brain[state][j]:
                bestaction=j
        nextstate=bestaction
        updateMapLocation(state)
        print(Tmap)
        state=nextstate
        if(state==location):print("Found Treasure")
def makeBrain(state,gamma,episodes,T):
    count=0
    for i in range(episodes):
        maxV=0
        while(state!=T):
            
            updateMapLocation(state)
            print(Tmap)
#pick a random action 
          #  print(state)
            A=[]
            for i in range(len(Reward)):
                if Reward[state][i]!=-1:
                    A.append(i)
            Rnum=random.randint(0, len(A)-1)
            action=A[Rnum]
#find the next state where the action takes you
            nextstate=action
#get max value of all actions in the current state
            brainV=[]
            for i in range(len(brain)):
                brainV.append(brain[nextstate][i])
            maxV=max(brainV)
#calculate AI brain
            brain[state][action]=Reward[state][action]+gamma*maxV
            
            state=nextstate
            count+=1
            nextstate=action
            
    return brain
def updateUserMapLocation(location,Umap):
    if location==0:
        Umap[3][3]=1
    elif Umap[3][3]!=100:
        Umap[3][3]=0 
        
    if location==1:
        Umap[2][2]=1
    elif Umap[2][2]!=100:
        Umap[2][2]=0
        
    if location==2:
        Umap[3][2]=1    
    elif Umap[3][2]!=100:
        Umap[3][2]=0
        
    if location==3:
        Umap[2][3]=1
    elif Umap[2][3]!=100:
        Umap[2][3]=0
        
        
    if location==4:
        Umap[3][1]=1
    elif Umap[3][1]!=100:
        Umap[3][1]=0
        
    if location==5:
        Umap[2][1]=1
        
    elif Tmap[2][1]!=100:
        Umap[2][1]=0
        
    if location==6:
        Umap[1][1]=1
    elif Umap[1][1]!=100:
        Umap[1][1]=0
        
    if location==7:
        Umap[1][2]=1
        
    elif Tmap[1][2]!=100:
        Umap[1][2]=0
        
    if location==8:
        Umap[1][3]=1
    elif Umap[1][3]!=100:
        Umap[1][3]=0
        
    if location==9:
        Umap[3][0]=1
    elif Umap[3][0]!=100:
        Umap[3][0]=0       


    if location==10:
        Umap[2][0]=1
    elif Umap[2][0]!=100:
        Umap[2][0]=0 
        
    if location==11:
        Umap[1][0]=1
    elif Umap[1][0]!=100:
        Umap[1][0]=0 
        
    if location==12:
        Umap[0][1]=1
    elif Umap[0][1]!=100:
        Umap[0][1]=0 
    
    
    if location==13:
        Umap[0][2]=1
    elif Umap[0][2]!=100:
        Umap[0][2]=0 
    if location==14:
        Umap[0][3]=1
        
    elif Umap[0][3]!=100:
        Umap[0][3]=0 
        
    if location==15:
        Umap[0][0]=1
    elif Umap[0][0]!=100:
        Umap[0][0]=0 
def userFindTreasure(location,T):
    count=0
    Umap=np.zeros((4,4))
    updateUserMapLocation(location,Umap)
    print(Umap)
    while location!=T: 
        print("You can go to the following rooms")
        for i in range(len(Reward)):
            if Reward[location][i]!=-1:
                print(i)
        print("Which room would you like to explore next?")
        room=input()
        room=int(room)
        location=room
        updateUserMapLocation(location,Umap)
        print(Umap)
        count+=1
    print("you have found the treasure!!")
    return count

