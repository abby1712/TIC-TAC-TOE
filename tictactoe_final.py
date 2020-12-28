print("Hey Nigga! \n welcome to tic tac toe")
print("who do you want to play with?\n")
mode=str(input("type - 'Human' or 'computer'\n ").upper())
def HumanvsHuman():
    theBoard = {"1": '1', "2": '2', "3": '3',
                "4": '4', "5": '5', "6": '6',
                "7": '7', "8": '8', "9": '9'}
    print("Now playing HUMAN vs HUMAN Tic Tac Toe")
    def gamecheck(count):
        if count < 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                a = theBoard['7']
                print("\nGame Over.\n")
                print(" **** " + a + " won. ****")
                playAgain()

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                b = theBoard['4']
                print("\nGame Over.\n")
                print(" **** " + b + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                c = theBoard['1']
                print("\nGame Over.\n")
                print(" **** " + c + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                d = theBoard['1']
                print("\nGame Over.\n")
                print(" **** " + d + " won. ****")
                playAgain()

            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                e = theBoard['2']
                print("\nGame Over.\n")
                print(" **** " + e + " won. ****")
                playAgain()

            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                f = theBoard['3']
                print("\nGame Over.\n")
                print(" **** " + f + " won. ****")
                playAgain()
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                g = theBoard['7']
                print("\nGame Over.\n")
                print(" **** " + g + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                h = theBoard['1']
                print("\nGame Over.\n")
                print(" **** " + h + " won. ****")
                playAgain()


        else:
            print("Draw the match")
            playAgain()
    def printboard():
        print(theBoard["1"], theBoard["2"], theBoard["3"])
        print(theBoard["4"], theBoard["5"], theBoard["6"])
        print(theBoard["7"], theBoard["8"], theBoard["9"])
    def gamePlay():
        """------------------------------------------------------------------------------------------------------------------"""
        print("Inorder to play this game , \n Enter the position you want to place X and O respectively")
        printboard()
        # firstMove
        xMove = str(input("hey X,Enter a position:\n").upper())
        theBoard.update({xMove: "X"})
        gamecheck(1)
        oMove = str(input("hey O, Enter a position:\n").upper())
        theBoard.update({oMove: "O"})
        gamecheck(1)
        printboard()
        gamecheck(1)
        count = 1
        """------------------------------------------------------------------------------------------------------------------"""
        # second Move
        xmove1 = xMove
        omove1 = oMove
        print("Positions are taken", xmove1, omove1)
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        if omove1 != oMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        else:
            print("choose some other positions", xmove1, "and", omove1, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            oMove = str(input("hey O, Enter a position:\n").upper())
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        count = 2
        """------------------------------------------------------------------------------------------------------------------"""
        # third Move
        xmove2 = xMove
        omove2 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        if omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(3)
            theBoard.update({oMove: "O"})
            gamecheck(3)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            gamecheck(3)
            oMove = str(input("hey O, Enter a position:\n").upper())
            gamecheck(3)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        gamecheck(3)
        count = 3
        """------------------------------------------------------------------------------------------------------------------"""
        # Fourth Move
        xmove3 = xMove
        omove3 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, omove3, xmove3, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        gamecheck(4)
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(4)
            theBoard.update({oMove: "O"})
            gamecheck(4)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            gamecheck(4)
            oMove = str(input("hey O, Enter a position:\n").upper())
            gamecheck(4)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        count = 4
        """------------------------------------------------------------------------------------------------------------------"""
        # fifth_move
        count = 5
        xmove = str(input("hey X,Enter a position:\n").upper())
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xmove: "X"})
            gamecheck(5)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            xmove4 = str(input("hey X,Enter a position").upper())
            theBoard.update({xmove4: "X"})
            gamecheck(5)
            printboard()
    def playAgain():
        print("Do you want to play again ?\n")
        print("yes or no ")
        sol = str(input("Enter yes or no:\n").upper())
        count = 0
        if sol == "YES":
            count = 0
            gamePlayagain()
        else:
            exit()
    def boardReset():
        theBoard.update({"1": '1'})
        theBoard.update({"2": '2'})
        theBoard.update({"3": '3'})
        theBoard.update({"4": '4'})
        theBoard.update({"5": '5'})
        theBoard.update({"6": '6'})
        theBoard.update({"7": '7'})
        theBoard.update({"8": '8'})
        theBoard.update({"9": '9'})
    def gamePlayagain():
        """------------------------------------------------------------------------------------------------------------------"""
        print(
            "Inorder to play this game  again once more , \n Enter the position you want to place X and O respectively")
        boardReset()
        printboard()
        # firstMove
        xMove = str(input("hey X,Enter a position:\n").upper())
        theBoard.update({xMove: "X"})
        gamecheck(1)
        oMove = str(input("hey O, Enter a position:\n").upper())
        theBoard.update({oMove: "O"})
        gamecheck(1)
        printboard()
        gamecheck(1)
        count = 1
        """------------------------------------------------------------------------------------------------------------------"""
        # second Move
        xmove1 = xMove
        omove1 = oMove
        print("Positions are taken", xmove1, omove1)
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        if omove1 != oMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        else:
            print("choose some other positions", xmove1, "and", omove1, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            oMove = str(input("hey O, Enter a position:\n").upper())
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        count = 2
        """------------------------------------------------------------------------------------------------------------------"""
        # third Move
        xmove2 = xMove
        omove2 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        if omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(3)
            theBoard.update({oMove: "O"})
            gamecheck(3)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            gamecheck(3)
            oMove = str(input("hey O, Enter a position:\n").upper())
            gamecheck(3)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        gamecheck(3)
        count = 3
        """------------------------------------------------------------------------------------------------------------------"""
        # Fourth Move
        xmove3 = xMove
        omove3 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, omove3, xmove3, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        oMove = str(input("hey O, Enter a position:\n").upper())
        gamecheck(4)
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(4)
            theBoard.update({oMove: "O"})
            gamecheck(4)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            gamecheck(4)
            oMove = str(input("hey O, Enter a position:\n").upper())
            gamecheck(4)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        count = 4

        """------------------------------------------------------------------------------------------------------------------"""
        # fifth_move
        count = 5
        xmove = str(input("hey X,Enter a position:\n").upper())
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xmove: "X"})
            gamecheck(5)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            xmove4 = str(input("hey X,Enter a position:\n").upper())
            theBoard.update({xmove4: "X"})
            gamecheck(5)

            printboard()
    gamePlay()
def HumanvsComputer():
    import random
    print("Now playing HUMAN vs Computer Tic Tac Toe")
    theBoard = {"1": '1', "2": '2', "3": '3',
                "4": '4', "5": '5', "6": '6',
                "7": '7', "8": '8', "9": '9'}
    def gamecheck(count):
        if count < 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top

                a = theBoard['7']
                printboard()
                print("bottom ")
                print("\nGame Over.\n")
                print(" **** " + a + " won. ****")
                playAgain()

            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                b = theBoard['4']
                printboard()
                print("across the middle")
                print("\nGame Over.\n")
                print(" **** " + b + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                c = theBoard['1']
                printboard()
                print("top line")
                print("\nGame Over.\n")
                print(" **** " + c + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                d = theBoard['1']
                printboard()
                print("left side")
                print("\nGame Over.\n")
                print(" **** " + d + " won. ****")
                playAgain()

            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                e = theBoard['2']
                printboard()
                print("down the middle")
                print("\nGame Over.\n")
                print(" **** " + e + " won. ****")
                playAgain()

            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                f = theBoard['3']
                printboard()
                print("down the right side")
                print("\nGame Over.\n")
                print(" **** " + f + " won. ****")
                playAgain()
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                g = theBoard['7']
                printboard()
                print("diagonal")
                print("\nGame Over.\n")
                print(" **** " + g + " won. ****")
                playAgain()

            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                h = theBoard['1']
                printboard()
                print("diagonal")
                print("\nGame Over.\n")
                print(" **** " + h + " won. ****")
                playAgain()


        else:
            printboard()
            print("Draw the match")
            playAgain()
    def printboard():
        print(theBoard["1"], theBoard["2"], theBoard["3"])
        print(theBoard["4"], theBoard["5"], theBoard["6"])
        print(theBoard["7"], theBoard["8"], theBoard["9"])
    def gamePlay():
        """------------------------------------------------------------------------------------------------------------------"""
        print("Inorder to play this game , \n Enter the position you want to place X and O respectively")
        printboard()
        # firstMove
        move_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        xMove = str(input("hey X,Enter a position:\n").upper())
        theBoard.update({xMove: "X"})
        gamecheck(1)
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        theBoard.update({oMove: "O"})
        move_list.remove(oMove)
        gamecheck(1)
        printboard()
        gamecheck(1)
        count = 1
        """------------------------------------------------------------------------------------------------------------------"""
        # second Move
        xmove1 = xMove
        omove1 = oMove
        print("Positions are taken", xmove1, omove1)
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        if omove1 != oMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        else:
            print("choose some other positions", xmove1, "and", omove1, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            oMove = random_num = random.choice(move_list)
            move_list.remove(xMove)
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        count = 2
        """------------------------------------------------------------------------------------------------------------------"""
        # third Move
        xmove2 = xMove
        omove2 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        if omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(3)
            theBoard.update({oMove: "O"})
            gamecheck(3)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            gamecheck(3)
            oMove = random_num = random.choice(move_list)
            move_list.remove(xMove)
            gamecheck(3)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        gamecheck(3)
        count = 3
        """------------------------------------------------------------------------------------------------------------------"""
        # Fourth Move
        xmove3 = xMove
        omove3 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, omove3, xmove3, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        gamecheck(4)
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(4)
            theBoard.update({oMove: "O"})
            gamecheck(4)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            gamecheck(4)
            oMove = random_num = random.choice(move_list)
            move_list.remove(oMove)
            gamecheck(4)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        count = 4
        """------------------------------------------------------------------------------------------------------------------"""
        # fifth_move
        count = 5
        xmove = str(input("hey X,Enter a position:\n").upper())

        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xmove: "X"})
            gamecheck(5)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            xmove4 = str(input("hey X,Enter a position").upper())

            theBoard.update({xmove4: "X"})
            gamecheck(5)
            printboard()
    def playAgain():
        print("Do you want to play again ?\n")
        print("yes or no ")
        sol = str(input("Enter yes or no:\n").upper())
        count = 0
        if sol == "YES":
            count = 0
            gamePlayagain()
        else:
            exit()
    def boardReset():
        theBoard.update({"1": '1'})
        theBoard.update({"2": '2'})
        theBoard.update({"3": '3'})
        theBoard.update({"4": '4'})
        theBoard.update({"5": '5'})
        theBoard.update({"6": '6'})
        theBoard.update({"7": '7'})
        theBoard.update({"8": '8'})
        theBoard.update({"9": '9'})
    def gamePlayagain():
        """------------------------------------------------------------------------------------------------------------------"""
        print(
            "Inorder to play this game  again once more , \n Enter the position you want to place X and O respectively")
        boardReset()
        printboard()

        # firstMove
        move_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        xMove = str(input("hey X,Enter a position:\n").upper())
        theBoard.update({xMove: "X"})
        gamecheck(1)
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        theBoard.update({oMove: "O"})
        move_list.remove(oMove)
        gamecheck(1)
        printboard()
        gamecheck(1)
        count = 1
        """------------------------------------------------------------------------------------------------------------------"""
        # second Move
        xmove1 = xMove
        omove1 = oMove
        print("Positions are taken", xmove1, omove1)
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        if omove1 != oMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        else:
            print("choose some other positions", xmove1, "and", omove1, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            oMove = random_num = random.choice(move_list)
            move_list.remove(xMove)
            theBoard.update({xMove: "X"})
            gamecheck(2)
            theBoard.update({oMove: "O"})
            gamecheck(2)
            printboard()
        count = 2
        """------------------------------------------------------------------------------------------------------------------"""
        # third Move
        xmove2 = xMove
        omove2 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        if omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(3)
            theBoard.update({oMove: "O"})
            gamecheck(3)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            gamecheck(3)
            oMove = random_num = random.choice(move_list)
            move_list.remove(xMove)
            gamecheck(3)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        gamecheck(3)
        count = 3
        """------------------------------------------------------------------------------------------------------------------"""
        # Fourth Move
        xmove3 = xMove
        omove3 = oMove
        print("choose some  positions", xmove2, xmove1, omove1, omove2, omove3, xmove3, "are taken")
        print("-------------------------------------------------------")
        xMove = str(input("hey X,Enter a position:\n").upper())
        move_list.remove(xMove)
        oMove = random_num = random.choice(move_list)
        move_list.remove(oMove)
        gamecheck(4)
        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xMove: "X"})
            gamecheck(4)
            theBoard.update({oMove: "O"})
            gamecheck(4)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            print("-------------------------------------------------------")
            xMove = str(input("hey X,Enter a position:\n").upper())
            move_list.remove(xMove)
            gamecheck(4)
            oMove = random_num = random.choice(move_list)
            move_list.remove(oMove)
            gamecheck(4)
            theBoard.update({xMove: "X"})
            theBoard.update({oMove: "O"})
            printboard()
        count = 4
        """------------------------------------------------------------------------------------------------------------------"""
        # fifth_move
        count = 5
        xmove = str(input("hey X,Enter a position:\n").upper())

        if xmove3 != xMove and omove3 != oMove and omove2 != oMove and omove1 != oMove and xmove2 != xMove and xmove1 != xMove:
            theBoard.update({xmove: "X"})
            gamecheck(5)
            printboard()
        else:
            print("choose some other positions", xmove2, xmove1, omove1, omove2, xmove3, omove3, "are taken")
            xmove4 = str(input("hey X,Enter a position").upper())

            theBoard.update({xmove4: "X"})
            gamecheck(5)
            printboard()
    gamePlay()
if mode=="HUMAN":
    HumanvsHuman()
elif mode=="COMPUTER":
    HumanvsComputer()
else:
    print(" hey Nigga, enter a valid Option!!")
    mode = str(input("type - 'Human' or 'computer' ").upper())
    if mode == "HUMAN":
        HumanvsHuman()
    elif mode == "COMPUTER":
        HumanvsComputer()
    else:
        print(" hey Nigga, Get lost!!")
        exit()



