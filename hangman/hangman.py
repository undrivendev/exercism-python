# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.word_guess = [None for i in range(0, len(word))]

    def guess(self, char):
        if self.status == STATUS_LOSE or self.status == STATUS_WIN:
            raise ValueError("Game over")

        found = False
        for i in range(0, len(self.word)):
            if self.word[i] == char and not self.word_guess[i]:
                self.word_guess[i] = char
                found = True
        
        if all(self.word_guess):
            self.status = STATUS_WIN
            return
        elif self.remaining_guesses == 0:
            self.status = STATUS_LOSE
            return

        if not found:
            self.remaining_guesses -= 1

        

    def get_masked_word(self):
        return "".join([i if i else "_" for i in self.word_guess])

    def get_status(self):
        return self.status
