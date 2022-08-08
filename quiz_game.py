
import shelve

from sklearn.metrics import SCORERS
d = shelve.open("hisc")
d["hisc"] = 56 
d.close()


print('-----------')

print("Welcome to the Wikipedia quiz show! So many useless facts.")
print("Please input your username and password to continue. ")




playing = input("Join the game? (Yes/No) ")


if playing.lower() != "yes":
    print("Quitting Game")
    quit()



correct_score = 0
incorrect_score = 0

def quizgame():
    print(" Welcome! Welcome! Come on in ")
    

    def wikipedia_question():
        answer = input(str("Test Question "))
        
        global correct_score
        global incorrect_score
    
        print(incorrect_score)
        print(correct_score)

        if answer ==  (str(45)):
            print("Correct! ")
            correct_score += 1
            wikipedia_question()
        else:
            print("Oops, that wasn't the right answer ")
            incorrect_score += 1

            if incorrect_score > 3:
                print("Game over!")
                print("You got " + str(correct_score) + " questions correct.")
            else:
                wikipedia_question()
                
        

    wikipedia_question()    


quizgame()
