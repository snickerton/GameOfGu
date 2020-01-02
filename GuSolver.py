import random
import copy

def checkOE(st):
    # print("\t\tCheckingOE")
    total = sum(st)    
    stNum = len(st)
    cnt = 0
    for x in st:
        if x != 0:
            cnt += 1
    stNum = cnt
    # returns a tuple total odd, total even
    return (total%2, stNum%2)

def cleanST(st):
    # print("\t\tCleaning stack from zeros")
    # print("\t\tOld stack: ", st)
    newStack = copy.deepcopy(st)
    newStack = [x for x in st if x != 0]
    
    # print("new stack: ", newStack)
    return newStack

def player(st):
    state = checkOE(st)

    if(len(st) == 1 and st[0] == 1):
        print("\tPLAYER LOSES, ONLY ONE CHIP LEFT")
        return st
    
    # for i in range(len(st)):
    #     print("in stack: ", i, st[i])
    #     # you can remove n number of chips or 1 chip, but not zero
    # for j in range(1,sum(st)):
    #     testStacks[0] -= 1
    #     testStacks = cleanST(testStacks)
    #     newState = checkOE(testStacks)
    
    # Removing things from array causes there to be an issue with things not existing
    for i in range(len(st)):
        for j in range(1,st[i]+1):
            # print("\tNow doing stack number: ", i, "minusing x things: ", j)
            testStacks = copy.deepcopy(st)
            testStacks[i] -= j
            # testStacks = cleanST(testStacks)
            newState = checkOE(testStacks)
            # print("testStack: " + str(testStacks))
            if newState[1] == 1 and newState[0] == 1:
                # print("\tRemoval found: ")
                # print("\tOld stack", st)
                # print("\tNew stack", testStacks)
                # print("\tReturning...")
                return testStacks
    
    # if not possible to get a result (2,1,2) then just return
    print("Unable to find good move, taking off one chip from top")
    asdf = copy.deepcopy(st)
    asdf[0] -= 1
    return asdf
# while(True):
# def GenerateStack():
#     numOfStacks = random.randint(3,4)
#     stacks = []
#     for i in range(numOfStacks):
#         numOfChips = random.randint(1,6)
#         stacks.append(numOfChips)

#     print(stacks)
#     return stacks

# stacks = GenerateStack

numOfGames = 999
scoreboard = [{},{}]

for i in range(numOfGames):
    print("**************\n Game Number: ", i+1, "\n************")
    numOfStacks = random.randint(3,4)
    stacks = []
    for i in range(numOfStacks):
        numOfChips = random.randint(1,6)
        stacks.append(numOfChips)

    print(stacks)

    originalStack = copy.deepcopy(stacks)


    # p1 and p2
    while len(stacks) != 0:
        # print("CURRENT STACK STATE: ", stacks)
        print("P1 move")
        stacks = player(stacks)
        stacks = cleanST(stacks)
        if(len(stacks) == 1 and stacks[0] == 1):
            print("NEXT PLAYER (2) LOSES, ONLY ONE CHIP LEFT")
            key = checkOE(originalStack)
            scoreboard[0][key] = scoreboard[0].get(key, 0) + 1     
            print("Original Stack: ", originalStack)
            break;
        # print("New stack: ", stacks)
        print("P2 move")
        stacks = player(stacks)
        stacks = cleanST(stacks)
        if(len(stacks) == 1 and stacks[0] == 1):
            print("NEXT PLAYER (1) LOSES, ONLY ONE CHIP LEFT")   
            key = checkOE(originalStack)
            scoreboard[1][key] = scoreboard[1].get(key, 0) + 1     
            print("Original Stack: ", originalStack)
            break;
        # print("New stack: ", stacks)
        # win condition

p1Score = 0
p2Score = 0
for key in scoreboard[0].keys():
    p1Score += scoreboard[0][key]
for key in scoreboard[1].keys():
    p2Score += scoreboard[1][key]


print("Final Score | P1: " + str(p1Score) + " P2: " + str(p2Score))
print(scoreboard)
print("End program")