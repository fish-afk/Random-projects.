import random
import ipaddress as ippt  # ipaddress just for fun. not really important
import time
from colorama import *
import os

''' you can build something similar with lesser lines of code, but i wanted to try out everything i had so yeah...'''

# r       p         s
# 0       1         2
#   testing phase

# -------------------Global Variables---------------------

score = 0
computer_score = 0
outcomes = ("rock", "paper", "scissors")
initial = 5
error = "please check your input -__- "

list_of_lucks = []

# ---------------------------------------------------------


print("STARTING..." + Fore.WHITE)

try:

    for i in range(1, 100):
        time.sleep(0.01)
        print('%d%%\r' % i, end="")

except SystemError:

    os.system("cls")

else:
    os.system("cls")
    print('''
    
    
    ''')


class StArt:

    def __init__(self, desc, manual, art):
        self.desc = desc
        self.manual = manual
        self.art = art

    def colorize(self):
        output = self.desc
        output2 = self.manual

        print(Fore.CYAN + output + Fore.WHITE)
        print(Fore.CYAN + output2 + Fore.WHITE)


i = StArt("                       "
          "----------------- THE ROCK PAPER SCISSORS GAME-------------------", "the games results will be in file.txt",
          "-------------\n"
          "|  -    -   |\n"
          "|   ----    |\n"
          "|-----------|\n")

print(i.art)
i.colorize()


# kinda over engineered here but i like it that way so that i learn more...


def random_gen():
    for att in range(initial):  # att describing attempt

        random_outcome = random.choice(outcomes)

        list_of_lucks.append(random_outcome)

    return list_of_lucks


def input_checker(inputi):
    mylist = random_gen()
    random.shuffle(mylist)

    randomstuff = mylist.pop()

    statement = str(f" the computer had input {randomstuff}")

    win = f"You Scored!,\n {statement}\n"

    lose = f"You Lost:( ,\n {statement}\n"

    tie = f"Its a tie!,\n the computer also had input {randomstuff}\n"

    global outcomes
    global score
    global computer_score
    global initial

    design = "-,-,-,-,-,-,-,-,-,-,-,,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-"

    if inputi == randomstuff:

        score += 0
        computer_score += 0
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return tie

    elif inputi == "rock" and randomstuff == "paper":

        score += 0
        computer_score += 1
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return lose

    elif inputi == "paper" and randomstuff == "scissors":

        score += 0
        computer_score += 1
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return lose

    elif inputi == "scissors" and randomstuff == "rock":

        score += 0
        computer_score += 1
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return lose

    elif inputi == "scissors" and randomstuff == "paper":

        score += 1
        computer_score += 0
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return win

    elif inputi == "rock" and randomstuff == "scissors":

        score += 1
        computer_score += 0
        print(design)

        print(f"You: {score} Computer: {computer_score}")

        return win

    elif inputi == "paper" and randomstuff == "rock":

        score += 1
        computer_score += 0

        print(design)
        print(f"You: {score} Computer: {computer_score}")  # for all these the score or computer score will be added by1

        return win

    elif inputi not in outcomes:

        return error


cmd = "You are playing with the Computer \n Please Type : \n  Rock or \n  Paper or \n  Scissors,  \nAnd hit enter -"

print(cmd.center(125))

if __name__ == "__main__":

    for tries in range(initial):

        var1 = input_checker(str(input().lower()))

        for i in range(1, 100):
            time.sleep(0.008)
        print("" + '%d%%\r' % i, end="")

        initial -= 1

        print(Fore.CYAN + Back.BLACK + var1)

        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + f"{initial} attempts left")

        if initial > 0:
            print("Enter Rock Paper or Scissors again please...")

        if initial == 0:
            break

print("")

print("Writing results to file.txt...")

for i in range(1, 100):
    time.sleep(0.01)
    print("" + '%d%%\r' % i, end="")

print("-----Thanks for playing, now go.......")

list3 = [";", ".", ",", "-", "_", "?", "/", "|"]
fin = ""

for i in range(50):
    q = random.choice(list3)
    designer = " ".join(q)

    fin += designer

final_score = f"         ---FINAL SCORE---\n          YOU: {score}  | computer: {computer_score}\n {fin}"

with open("../file.txt", "w") as file:
    try:
        if computer_score == 0 and score == 0:

            file.write("Please check your spellings when playing...")

        else:

            file.write(final_score)

    except FileNotFoundError as e:

        print(e)

    except FileExistsError as f:

        with open("File1234897302892358", "w") as file2:

            if computer_score == 0 and score == 0:
                file2.write("Please check your spellings when playing...")

            else:
                file2.write(final_score)

    finally:

        file.close() and file2.close()

print(f"{final_score}\n\n\n")
print(ippt)

time.sleep(5)

# endl
# end program....

#                                            -----Made by: a fish..-----
