import random
class Hangman:
    def __init__(self) -> None:
        self.answer_list = ["blue", "case", "speaker", "mouse", "glass"]
        self.lives = 7
        self.guessed_letters = []
        self.answer = self.get_random_answer()
        self.answerletters = self.get_letters()
        self.game()

    def get_random_answer(self):
        answer = self.answer_list[random.randint(0,len(self.answer_list) - 1)]
        return answer

    def get_letters(self):
        answerletters = [*self.answer]
        answerletters = list(set(answerletters))
        return answerletters
    
    def is_correct_guess(self, guess):#All of the functions that start with is usally return a true or false
        if guess.isalpha():
            if len(guess) == 1:
                if guess in self.answerletters:
                    self.answerletters.remove(guess)
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
    def is_already_guessed(self, guess):
        """
        precondition:
        postcondition: Return true if guess in guessletters, false otherwise
        """
        if guess in self.guessed_letters:
            print("You already guessed this letter")
            return True
        else:
            self.guessed_letters.append(guess)
            return False

    def game(self):
        while self.lives > 0: #Make the while without using the true (Use a condition)
            guess = input("Make a guess: ")
            if guess == self.answer:
                print("You won!")
                print(f"You finished with {self.lives} lives")
                break
            if self.is_already_guessed(guess) == False:
                if self.is_correct_guess(guess) == True:
                    print(f"You currently have {self.lives} lives")
                else:
                    self.lives = self.lives - 1
                    print(f"You currently have {self.lives} lives")
            else:
                continue
            if self.answerletters == []:
                print("You won! The answer was " + self.answer)
                print(f"You finished with {self.lives} lives")
                break
        else:
            print("You ran out of lives :(")
Hangman()