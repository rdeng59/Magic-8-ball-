# importing the libraries
import random
import pyfiglet
import time

# defining function magic8ball()
def magic8ball():
    # print aestheic text design
    print(pyfiglet.figlet_format("Magic 8 ball"))
    # asking for players name
    name = input('I am THE MAGIC 8 BALL, State your name here>')
    # greeting the player
    print('Hello ' + name + '!')
    # calling the magic_questions() function to ask for question and give magic response
    magic_questions()

# defining the function magic_questions()
def magic_questions():
    answers = ["It is certain", "It is decidely so", "Without a doubt", "Yes", "Definitely", "You may rely on it", "As I see it, yes",
               "Most likely", "outlook good", "Yes", "Sign point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
               "My reply is no", "My sources say no",
               "Outlook not so good", "Very Doubtful"]
    input('Ask me a question ')
    # Simulating the thinking process
    print("Thinking....")
    time.sleep(1)
    print("Having a Brain fart...")
    time.sleep(2)
    # printing out a random answer from the list above of possible answers
    print(answers[random.randint(0, len(answers) - 1)])
    time.sleep(3)
    # calling the reply to check if the player wants to play again
    Replay()


# defining the replay function
def Replay():
    #asking the players interest in playing again
    print("Do you have another question? [Yes/No] ")
    #converting the response to lower case to avoid capitalization issues
    reply = input().lower()
    # if yes, resume the game again from the question-answer part
    if reply == 'yes':
        magic_questions()
    # if no, stop the execution of the program
    elif reply == 'no':
        exit()
    # in case of an invalid response, ask the player to enter a valid choice
    else:
     print('Apologies, Please enter Yes or a No.')
     Replay()

# calling the magic8ball() function to recursively activate the other functions too
magic8ball()

