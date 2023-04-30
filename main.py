import random
import time
import string


def higherorlower2():
    global guessnumber
    global randomnumber
    if int(guessnumber) >= randomnumber:
        print("The number is below " + guessnumber)
    if int(guessnumber) <= randomnumber:
        print("The number is above " + guessnumber)
    guessnumber = input("What do you think the number is? ")
    checknumber2()


def checknumber2():
    global randomnumber
    global guessnumber
    if int(guessnumber) == randomnumber:
        print("You got it correct!")
    if int(guessnumber) != randomnumber:
        higherorlower2()


def botpick3():
    global botchosen3
    global randomnumber
    if randomnumber == 3:
        botchosen3 = "rock"
    if randomnumber == 2:
        botchosen3 = "scissors"
    if randomnumber == 1:
        botchosen3 = "paper"


def transitions3():
    global playerpick
    global playerchosen3
    if playerpick == 3:
        playerchosen3 = "rock"
    if playerpick == 2:
        playerchosen3 = "scissors"
    if playerpick == 1:
        playerchosen3 = "paper"


def outcome3():
    if playerpick == randomnumber:
        print("It's a draw!")
    else:
        if playerpick == 1 and randomnumber == 2 or playerpick == 2 and randomnumber == 3 or playerpick == 3 and randomnumber == 1:
            print("You lost!")
        if playerpick == 1 and randomnumber == 3 or playerpick == 2 and randomnumber == 1 or playerpick == 3 and randomnumber == 2:
            print("You won!")


def encrypt4(text, shift):
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    encrypted = text.translate(table)
    print("The encoded message is: " + encrypted)
def decrypt5(text, shift):
    shift = shift - shift * 2
    alphabet = string.ascii_lowercase
    shifted = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted)
    decrypted = text.translate(table)
    print("The decoded message is: " + decrypted)

gamenumber = input("What game would you like to play?(Dice Rolling = 1, Guess a number = 2, Rock Paper Scissors = 3, \nEncryption = 4, Decryption = 5) ")
if gamenumber == "1":
    twentycharacters = 12345678901234567890
    number_of_rolls = input("How many times would you like this process to repeat?(Up to 20) ")
    for x in range(int(number_of_rolls)):
        time.sleep(2)
        randomnumber = random.randint(1, 6)
        print("Your number is " + str(randomnumber))
    input("Press any key to end program")


if gamenumber == "2":
    print("The random number is between 1 to 100 (includes 1 and 100)")
    randomnumber = random.randint(1, 100)
    if randomnumber >= 50:
        print("The random number is above 50.")
    if randomnumber <= 50:
        print("The random number is below 50.")
    guessnumber = input("What do you think the number is? ")
    checknumber2()
    input("Press any key to end program")


if gamenumber == "3":
    randomnumber = random.randint(1, 3)
    botpick3()
    playerpick = int(input("What is your pick? 1 = paper, 2 = scissors and 3 = rock "))
    transitions3()
    print("You chose " + playerchosen3 + " And the bot chose " + botchosen3 + "!")
    if playerpick == randomnumber:
        print("It's a draw!")
    else:
        if playerpick == 1 and randomnumber == 2 or playerpick == 2 and randomnumber == 3 or playerpick == 3 and randomnumber == 1:
            print("You lost!")
        if playerpick == 1 and randomnumber == 3 or playerpick == 2 and randomnumber == 1 or playerpick == 3 and randomnumber == 2:
            print("You won!")
    input("Press any key to end program")


if gamenumber == "4":
    text = input("What is your text? Type in lowercase. ")
    shift = input("What is the increase in letters? ")
    encrypt4(text, int(shift))
    input("Press any key to end program")

if gamenumber == "5":
    text = input("What is the encoded message? Should be in lowercase. ")
    shift = input("What is the shift? ")
    decrypt5(text, int(shift))
    input("Press any key to end program")
