from questions import QUESTIONS
import random

def isAnswerCorrect(question, answer):
    return question["answer"] == answer

def fifty_fifty(question):
    answer = "option" + str(question["answer"])
    options = set(["option1", "option2", "option3", "option4"])
    options.remove(answer)
    delete1 = random.choice(list(options))
    options.remove(delete1)
    delete2 = random.choice(list(options))
    question[delete1] = ""
    question[delete2] = ""
    return question
    
def lifeline_menu(isLifeLineTaken: bool, current_round: int) -> None:
    if not isLifeLineTaken and current_round != 14:
        print("To use 50-50 lifeline please type lifeline")
    elif current_round == 14 and not isLifeLineTaken:
        print("Sorry you cannot use lifeline in the last round")
    else:
        print("You have already used your lifeline")
    return
    
def choice_menu(current_round: int, money_won: int, minimum_money_rewarded: int) -> None:
    print("1. Play Round", current_round + 1)
    print("2. Quit with", money_won)
    print("If you give wrong answer in this round you will take home Rs.", minimum_money_rewarded)
    if money_won > minimum_money_rewarded:
        print("You will loose: Rs.", money_won - minimum_money_rewarded)
    print("Please enter your choice")
    return

def print_question(current_question) -> None:
    print(current_question["name"])
    print("Your options are: ")
    print("1.", current_question["option1"])
    print("2.", current_question["option2"])
    print("3.", current_question["option3"])
    print("4.", current_question["option4"])
    return

def update_minimum_money(current_round: int, money_won: int, minimum_money_rewarded: int) -> int:
    
    if current_round == 4:
        print("Congratulations on passing Round 5.")
        print("Now you will surely take Rs.", money_won, "back home")
        minimum_money_rewarded = money_won
    
    elif current_round == 10:
        print("Congratulations on passing Round 11.")
        print("Now you will surely take Rs.", money_won, "back home")
        minimum_money_rewarded = money_won
        
    return minimum_money_rewarded
        
    
def kbc():

    isLifeLineTaken = False
    money_won = 0
    minimum_money_rewarded = 0
    quit = False
    choice = 0
    
    print("Welcome to Kaun Banega Crorepati")    
    for current_round in range(15):
        
        print("Welcome to Round", current_round + 1)
        choice_menu(current_round, money_won, minimum_money_rewarded)
        choice = int(input())
        if choice == 2:
            print("Congratulations! You have won: Rs.", minimum_money_rewarded)
            return
        current_question = QUESTIONS[current_round]
        print_question(current_question)
        print("Please press enter to answer the current Question")
        lifeline_menu(isLifeLineTaken, current_round)
        choice = input()
        if choice == "lifeline":
            isLifeLineTaken = True
            current_question = fifty_fifty(QUESTIONS[current_round])
            print("The Question after removing two incorrect options is: ")
            print_question(current_question)
        print("Please Enter the correct option")
        correct_option = QUESTIONS[current_round]["answer"]
        option = int(input())
        
        if correct_option == option:
            print("Congratulations! you have given the correct answer to the question")
            money_won = QUESTIONS[current_round]["money"]
            print("You have won: Rs.", money_won)
            minimum_money_rewarded = update_minimum_money(current_round, money_won, minimum_money_rewarded)
            
        else:
            print("Sorry! your answer is wrong")
            print("Thank you for playing Kaun Banega Crorepati")
            print("You have won: Rs. ", minimum_money_rewarded)
            return
    
    print("Congratulations on wining 1 crore rupees!!")
    return
            
kbc()