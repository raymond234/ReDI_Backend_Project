class Score:
    def trial_score(self, game):
        perfectGuess = 7
        trial_score = perfectGuess - len(game.missedLetters())
        return trial_score

    def length_score(self, game):
        return len(game.secretWord)

    def total_score(self, gameScore):
        total_score = gameScore.trial_score(self.game) + gameScore.length_score(self.game)
        return total_score
