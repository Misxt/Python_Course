import random
answer_list = ["Blue", "Case", "Speaker", "Mouse", "Glass"]
answer = answer_list[random.randint(0,len(answer_list) - 1)]
answerletters = [*answer]
answerletters = list(set(answerletters))
guessed_letters = []

def game():
    lives = 7
    while lives > 0: #Make the while without using the true (Use a condition)
        letter = input("Guess a letter: ")
        if letter.isalpha():
            if len(letter) == 1:
                if letter in guessed_letters:
                    print("You already guessed this letter")
                    continue
                else:
                    if letter in answer:
                        answerletters.remove(letter)
                        guessed_letters.append(letter)
                        print("Correct!")
                        print(f"You currently have {lives} lives")
                        if answerletters == []:
                            print("You won! The answer was " + answer)
                            print(f"You finished with {lives} lives")
                            break
                    else:
                        lives = lives - 1
                        print("Wrong")
                        print(f"You currently have {lives} lives")
            elif letter == answer:
                print("You won!")
                print(f"You finished with {lives} lives")
                break
            else: 
                print("Input 1 letter or the correct answer - nothing else") 
                continue
        else:
            print("Input only letters")
    else:
        print("You ran out of lives :(")
game()