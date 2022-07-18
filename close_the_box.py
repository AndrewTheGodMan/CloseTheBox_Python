import random
import time

# - Game Variables. - #
main_anwser = 0
closed1 = False
closed2 = False
closed3 = False
closed4 = False
closed5 = False
closed6 = False
closed7 = False
closed8 = False
closed9 = False
closed10 = False
output1 = 0
output2 = 0
output3 = 0
hasnotwon = True

# - Makes it easier to type the time.sleep() command. - #
def wait(sec):
    time.sleep(sec)

# - This rolls the dice - #
def roll_dice():
    global main_anwser
    print('Your numbers are.')
    wait(0.5)
    answer1 = random.choice([1,2,3,4,5,6])
    print(answer1)
    answer2 = random.choice([1,2,3,4,5,6])
    print(answer2)
    main_anwser = answer1+answer2

# - Prints out all the boxes - #
def print_board():
    print("")
    if closed1 == False:
        print("1 open")
    elif closed1 == True:
        print("1 closed")
    if closed2 == False:
        print("2 open")
    elif closed2 == True:
        print("2 closed")
    if closed3 == False:
        print("3 open")
    elif closed3 == True:
        print("3 closed")
    if closed4 == False:
        print("4 open")
    elif closed4 == True:
        print("4 closed")
    if closed5 == False:
        print("5 open")
    elif closed5 == True:
        print("5 closed")
    if closed6 == False:
        print("6 open")
    elif closed6 == True:
        print("6 closed")
    if closed7 == False:
        print("7 open")
    elif closed7 == True:
        print("7 closed")
    if closed8 == False:
        print("8 open")
    elif closed8 == True:
        print("8 closed")
    if closed9 == False:
        print("9 open")
    elif closed9 == True:
        print("9 closed")
    if closed10 == False:
        print("10 open")
    elif closed10 == True:
        print("10 closed")
    
def game():
    
    # - Makes a command called closebox() so I can easily close a box. - #
    def closebox(First,Second,Third):
        global closed1
        global closed2
        global closed3
        global closed4
        global closed5
        global closed6
        global closed7
        global closed8
        global closed9
        global closed10
        global output1
        global output2
        global output3
        if First == 1:
            closed1 = True
        elif First == 2:
            closed2 = True
        elif First == 3:
            closed3 = True
        elif First == 4:
            closed4 = True
        elif First == 5:
            closed5 = True
        elif First == 6:
            closed6 = True
        elif First == 7:
            closed7 = True
        elif First == 8:
            closed8 = True
        elif First == 9:
            closed9 = True
        elif First == 10:
            closed10 = True
        if Second == 1:
            closed1 = True
        elif  Second == 2:
            closed2 = True
        elif Second == 3:
            closed3 = True
        elif Second == 4:
            closed4 = True
        elif Second == 5:
            closed5 = True
        elif Second == 6:
            closed6 = True
        elif Second == 7:
            closed7 = True
        elif Second == 8:
            closed8 = True
        elif Second == 9:
            closed9 = True
        elif Second == 10:
            closed10 = True
        if Third == 1:
            closed1 = True
        elif Third == 2:
            closed2 = True
        elif Third == 3:
            closed3 = True
        elif Third == 4:
            closed4 = True
        elif Third == 5:
            closed5 = True
        elif Third == 6:
            closed6 = True
        elif Third == 7:
            closed7 = True
        elif Third == 8:
            closed8 = True
        elif Third == 9:
            closed9 = True
        elif Third == 10:
            closed10 = True
    
    def Math():
        
        # - Gives inputs for the player. - #
        def repeat2():    
            global output1
            global output2
            global output3
            input1 = input("Enter the First box number you want to close. (Type close if you can't play your turn.) : ")
            if input1 == "close":
                print("Closed.")
                exit()
            output1 = int(input1)
            wait(0.5)
            input2 = input("Enter the Seccond box number you want to close. If you don't have a Second number type 0 : ")
            if input2 == "close":
                print("Closed.")
                exit()
            output2 = int(input2)
            wait(0.5)
            input3 = input("Enter the Third box number you want to close. If you don't have a Third number type 0 : ")
            if input3 == "close":
                print("Closed.")
                exit()
            output3 = int(input3)
            wait(0.2)
            
            if output1 == 1 and closed1 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 2 and closed2 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 3 and closed3 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 4 and closed4 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 5 and closed5 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 6 and closed6 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 7 and closed7 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 8 and closed8 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output1 == 9 and closed9 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 10 and closed10 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            if output2 == 1 and closed1 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 2 and closed2 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 3 and closed3 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 4 and closed4 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 5 and closed5 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 6 and closed6 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 7 and closed7 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 8 and closed8 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 9 and closed9 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output2 == 10 and closed10 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            if output3 == 1 and closed1 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 2 and closed2 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 3 and closed3 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 4 and closed4 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 5 and closed5 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 6 and closed6 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 7 and closed7 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 8 and closed8 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 9 and closed9 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            elif output3 == 10 and closed10 == True:
                print("Box already closed. ")
                wait(0.3)
                Math()
            

            if output1 + output2 + output3 == main_anwser:
                closebox(output1, output2, output3)
            else:
                print("incorrect math. ")
                wait(0.3)
                Math()

        repeat2()

    # - Checks to see if the game has been won. - #
    def win_check():
        global hasnotwon
        if closed1 == True and closed2 == True and closed3 == True and closed4 == True and closed5 == True and closed6 == True and closed7 == True and closed8 == True and closed9 == True and closed10 == True:
            hasnotwon = False
            print("You have closed all of the boxes.")
            exit()
        else:
            wait(0)


    # - Prints out the game. - #
    if hasnotwon == True:
        win_check()
        print_board()
        print("")
        roll_dice()
        print("")   
        Math()
        print("")
        win_check()
    
        
    


# - Loops the Program until won or closed. - #
jason = True
while jason == True:
    game()




