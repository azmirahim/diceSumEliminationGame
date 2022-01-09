# Kaamil Quidwai & Azmi Rahim
# June 16, 2020
# The player and computer roll 3-5 dice and chose two numbers from the roll. The sum is eliminated from their set (2-12) and the first user to have a empty number set wins. 
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 999, -3, -100, "idk", "s", "R", "r", "i", "I", "ok", "wefefs", " "

import random

# Define roll rolls the dice for the user when the user inputs 'r' or 'R', and produces a list of numbers from the roll made. This is then returned and stored under
# a global variable in the main program.
def roll(turn, dicesRolled):
    dicelist = []
    print("")
    print(turn, "turn")
    roll = input("Press 'r' or 'R' to roll: ")
    while roll != 'r' and roll != "R":
        print("That is not a valid entry. Please try again.")
        roll = input("Press 'r' to re-roll: ")
    for p in range(dicesRolled):
        dice = random.randint(1,6)
        dicelist.append(dice)
    return dicelist

# Define checkRoll checks for all possible sums that can be made by the numbers which were rolled.
def checkRoll(loopPosition, numberOfDice, checkDicelist):
    t = numberOfDice - (loopPosition+1)
    index = loopPosition + 1
    sum_list = []
    for y in range (t):
        sums = checkDicelist[loopPosition] + checkDicelist[index]
        sum_list.append(sums)
        index += 1
    return sum_list

# Define search uses the list of possible sums and searches for a match between the list of sums and the number set.
def search(sumList, numberSet):
    found = False
    for i in range(len(sumList)):
        if sumList[i] in numberSet:
            found = True
            break
    return found

# Define skipTurn Check stores the sums returned by checkRoll and sumRoll is a list that stores all the possible sums from the roll made. 
def skipTurn(dices, currentDicelist, skip):
    sumRoll = [] 
    possibleSums = dices - 1
    for x in range (possibleSums):
        check = checkRoll(x, dices, currentDicelist)
        sumRoll.extend(check)
    listSearch = search(sumRoll, skip)
    return listSearch

# Define choose allows the user to choose which numbers they want to add from the roll they previously made. It error checks to ensure the user chooses a valid number
# from the list. The chose number is returns and stored as a global variable to the main program.
def choose(x, rolledNumbers):
    if x == "Player":
        while True:
            try:
                choose = int(input("Choose a dice: "))
                break
            except:
                print("Please enter a valid value. Try again.")
                print(rolledNumbers, "\n")
        while choose not in rolledNumbers:
            print("Sorry that was not a dice in the roll, please try again.")
            print(rolledNumbers, "\n")
            while True:
                try:
                    choose = int(input("Choose a dice: "))
                    break
                except:
                    print("Please enter a valid value. Try again.")
                    print(rolledNumbers, "\n")
        rolledNumbers.remove(choose)
        print(rolledNumbers)
        return choose, rolledNumbers
    elif x == "Computer":
        choose = random.choice(rolledNumbers)
        return choose, rolledNumbers

# Define remove replaces the sum with a blank space to show the user that the sum has been removed from the list.
def remove(removeSum, sumRoll):
    index = removeSum.index(sumRoll) # This was done in the player and computer set prior to printing to replace the sum in the list with a blank space.
    removeSum.remove(sumRoll)
    removeSum.insert(index, " ")
    return removeSum

# Define numberSet prints the updated number set after each number is removed from the set and at the beginning of the users turn.
def numberSet(playerSet, computerSet):
    print(" \nPlayer Set --------->   ", end = " ")
    for i in range(len(playerSet)):
        print(playerSet[i], end = " ")
    print(" \nComputer Set ------->   ", end = " ")
    for o in range(len(computerSet)):
        print(computerSet[o], end = " ")
    print("")

# Define numberCheck checks to see if there are numbers remaining in the number set.
def numberCheck(sets):
    value = 1
    for i in range(2, 13):
        if i in sets:
            value += 1
    return value

# Define instructions processes user input for instructions. If the user presses 'i' or 'I' as their turn, this function will take the input and output the game instructions. 
def instructions():
    instruction = input("Enter 'i' or 'I' for intructions. To continue, press any key: ")
    if instruction == 'i' or instruction == 'I':
        print("")
        print("Objective - First player to eliminate all the numbers in their Number Set wins\nA number is eliminated during a player’s turn by choosing two dice that add to\none of the numbers in the set.")

a_list = [2,3,4,5,6,7,8,9,10,11,12]
p_list = [2,3,4,5,6,7,8,9,10,11,12]
c_list = [2,3,4,5,6,7,8,9,10,11,12]
p_value = 1
c_value = 1

print("Welcome to Dice Number Set\nPlayer and user both start with the same number set: \n")
print(a_list, "\n ")
print("Objective - First player to eliminate all the numbers in their Number Set wins\nA number is eliminated during a player’s turn by choosing two dice that add to one of the numbers in the set. \n")

num_dice = 0

while num_dice != 3 and num_dice != 4 and num_dice != 5:
    while True:
        try:
            # Input - The user chooses the number of dice to work with for the whole game.
            num_dice = int(input("Choose how many dice to use for this game (3 - 5): "))
            break
    # Process - The program takes the number inputted by the user and uses it throughout the game to roll the specified number of dice.
    # Output - The program error checks to ensure its a valid entry between 3 and 5. If not, the program tells user they've made an invalid entry, and to try again.
        except:
            print("That is not a valid entry. Please try again.")
    if num_dice < 3 or num_dice > 5:
        print("That is not a valid entry. Please try again")

print("")       
print("Player Set          ", *p_list) # An asterisk was used several times to not print the square brackets and commas in the list.
print("Computer Set        ", *c_list)

while p_value >= 1 and c_value >= 1:
    
    # Player Turn
    user = "Player"
    # Input - The program asks the user to enter 'r' or 'R' to roll and pick two numbers from the roll made.
    new_dicelist = roll(user, num_dice)
    # Copy of the original list is made as when list is used in function, the global list is still altered.
    # This way we are able to refer back to the original list when needed.
    original_dicelist = new_dicelist.copy() 
    print(" \nRoll ---->   ", *new_dicelist, "\n")

    remaining_set = skipTurn(num_dice, new_dicelist, p_list)

    if remaining_set == False:
        print("Player has no move. Oh well better luck next time.")

    elif remaining_set == True:
        print("Player please choose 2 dice")
        print("Dice:", new_dicelist, "\n")
        choose_1, chosen_numbers = choose(user, new_dicelist)
        print("")
        choose_2, chosen_numbers = choose(user, chosen_numbers)
        print("")
        sum_dice = choose_1 + choose_2
        # Process & Output - If inputted correctly, the program tells the user the sum and removes that sum from the list. Several error checks are done throughout. 
        print("You chose:",choose_1, "+", choose_2, "=", sum_dice)

        while sum_dice not in p_list:
            print(sum_dice, "was not found in the list. \n")
            print("Player please choose 2 dice")
            print("Dice:", original_dicelist, "\n")
            # Another copy of the original list is made so it can be altered within the function without altering the original list.
            # This way if the user makes an error multiple times, the original list resets every time this part of the code is looped.
            new_dicelist = original_dicelist.copy() 
            choose_1, chosen_numbers = choose(user, new_dicelist)
            print("")
            choose_2, chosen_numbers = choose(user, chosen_numbers)
            sum_dice = choose_1 + choose_2
            print(" \nYou chose:", choose_1, "+", choose_2, "=", sum_dice)
            
        p_list = remove(p_list, sum_dice)
  
    numberSet(p_list, c_list)
        
    p_value = numberCheck(p_list)
    if p_value == 1:
        break
        
    print("")
    instructions()
    numberSet(p_list, c_list)

    # Computer Turn    
    user = "Computer"
    chosen_list = []
    # Input, Process & Output - Is the same as the players turn except it does not ask to chose two numbers in the roll and does not tell the user that the sum was not found.
    new_dicelist = roll(user, num_dice)
    original_dicelist = new_dicelist.copy()

    remaining_set = skipTurn(num_dice, new_dicelist, c_list)
    
    print(" \nRoll ---->   ", *new_dicelist)

    if remaining_set == False:
        print("Computer turn --> no move found.")

    elif remaining_set == True:
        choose_1, chosen_numbers = choose(user, new_dicelist)
        choose_2, chosen_numbers = choose(user, chosen_numbers)
        print("")
        sum_dice = choose_1 + choose_2
        
        while sum_dice not in c_list:
            new_dicelist = original_dicelist.copy()
            choose_1, chosen_numbers = choose(user, new_dicelist)
            choose_2, chosen_numbers = choose(user, chosen_numbers)
            sum_dice = choose_1 + choose_2
            
        print("Computer turn --> Computer chose:", choose_1, "+", choose_2, "=", sum_dice)
            
        c_list = remove(c_list, sum_dice)

    numberSet(p_list, c_list)

    c_value = numberCheck(c_list)
    if c_value == 1:
        break
    
    print("")
    instructions()
    numberSet(p_list, c_list)
    
# Output - The program announces the winner to the first user that has zero numbers left in their set.

print("")
if p_value == 1:
    print("Player won the game! Congratulations!")

if c_value == 1:
    print("Sorry, the computer won the game. Try again next time!")

print("Thanks for playing! Goodbye.")
