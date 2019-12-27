import getpass
import Tkinter
import random

def hangman():

    try:

        word_list = []
        
        print("Hello, Welcome!")
        print(" ")
            
        name = raw_input("Please enter your name:")
        print("Hi.."+ str(name) + ". Let's play Hangman!")
        print("")

        while True:
            used_letters = []
            guessed_list = []
            secret = str(getpass.getpass("Please enter the secret word:"))
            print("")
            print("Let's play.. You need to guess the secret word given, by guessing one alphabet in every turn.!\n")
            print("")
            
            modified_secret = "".join((secret[0],"*"*(len(secret)-2),secret[-1]))
            print("The first and last character of secret word is :"+modified_secret)
            print("")

            count = len(secret)

            while count>0:
                print("")

                print("You have "+str(count)+ " tries left")
                print("")
                
                user_entry = raw_input("Player, please enter your guess: \t")
                used_letters.append(user_entry)

                if user_entry not in guessed_list:
                    guessed_list.append(user_entry)
                
                
                guessed_string = ''.join(letter if letter in used_letters else '*'  for letter in secret[1:-1])
                guessed_string = ''.join((secret[0],guessed_string,secret[-1]))

                if user_entry not in secret or user_entry not in secret[1:-1] :
                    
                    count-=1
                    
                print("")
                print("your guessed word :\t"+guessed_string)

                if str(guessed_string) == str(secret):
                    print("Congrats!.."+name + " You won the game!")
                    break
    
                    
                if user_entry not in secret:
                    print('Incorrect guess..."'+user_entry+'" is not in secret word')
                    print("")

                print("")
                guessed_list_string = ','.join(char for char in guessed_list)
                print("Alphabets guessed by you till now....:"+guessed_list_string)
                print("")

                if count == 0:
                    print("Oops, you are out of attempts....! You Lost!")
                    print("")
                    print("The secret word was '"+secret+"'")
                    print("")
                    break


            print("")
            play_again = raw_input("Do you want to play again (Y/N): ")

            if play_again.upper() == "Y":
                print("")
                continue
            else:
                break

    except:

        print("Exception occured...")
    

if __name__ == "__main__":

    hangman()
    
