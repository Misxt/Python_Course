import random
answer_list = ["blue", "case", "speaker", "mouse", "glass"]
def get_random_answer():
    answer = answer_list[random.randint(0,len(answer_list) - 1)]
    return answer
def get_letters(answer):
    answerletters = [*answer]
    answerletters = list(set(answerletters))
    return answerletters
def is_correct_guess(guess, answerletters):#All of the functions that start with is usally return a true or false
    if guess.isalpha():
        if len(guess) == 1:
            if guess in answerletters:
                answerletters.remove(guess)
                print("Correct!")
                return True
            else:
                print("Wrong")
                return False
        else: 
            print("Input 1 letter or the correct answer - nothing else") 
            return False
    else:
        print("Input only letters")
        return False
def is_already_guessed(guess, guessed_letters):
    """
    precondition:
    postcondition: Return true if guess in guessletters, false otherwise
    """
    if guess in guessed_letters:
        print("You already guessed this letter")
        return True
    else:
        guessed_letters.append(guess)
        return False
def game():
    lives = 7
    guessed_letters = []
    answer = get_random_answer()
    answerletters = get_letters(answer)
    while lives > 0: #Make the while without using the true (Use a condition)
        guess = input("Make a guess: ")
        if guess == answer:
            print("You won!")
            print(f"You finished with {lives} lives")
            break
        if is_already_guessed(guess, guessed_letters) == False:
            if is_correct_guess(guess, answerletters) == True:
                print(f"You currently have {lives} lives")
            else:
                lives = lives - 1
                print(f"You currently have {lives} lives")
        else:
            continue
        if answerletters == []:
            print("You won! The answer was " + answer)
            print(f"You finished with {lives} lives")
            break
    else:
        print("You ran out of lives :(")
game()