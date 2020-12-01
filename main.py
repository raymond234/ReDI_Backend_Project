from Game import Game
from User import User
from pantry import HANGMAN_PICS, user_greeting
from Displays import display_board_game


def get_guess(already_guessed):
    """
    Returns the letter the player entered.
    Ensures the player enters a single letter and nothing else.
    """
    while True:
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Only a single letter is allowed.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz*#':
            print('Please enter a letter from the alphabet.')
        else:
            return guess


def play_again():
    """
    Returns True if the player wants to play again, False otherwise.
    """
    print('Would you like to play again? (y)es or (n)o')
    return input().lower().startswith('y')


if __name__ == "__main__":
    user = User()
    user.create_user()
    username = user.username
    game = Game(username)
    print('|_H_A_N_G_M_A_N_|')
    special_char = list()
    special_char.append(game.update_special_char())


# Now for the game itself:
    while True:
        display_board_game(game.missed_letters, game.correct_letters, game.hint, special_char, game.secret_word)
    # Let the player enter a letter:n
        guess = get_guess(already_guessed=game.missed_letters + game.correct_letters)   # The sexiest thing I've ever done

        if guess in game.secret_word:
            game.correct_letters = game.correct_letters + guess
        # Check to see if the player has won:
            foundAllLetters = True
            string = game.secret_word.replace(" ", "")
            for i in range(len(string)):
                if string[i] not in game.correct_letters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('You guessed it!')
                print('The secret word is "' + game.secret_word + '"! You win!')
                game.is_done = True
                game.is_won = True
                game.update_game_score()

        elif guess == "#":
            game.get_hint()
            # game.get_hint()  # Somehow figure out how to make display board display hint.
            # This function call above persists the hint getting in the database by flipping self.got_hint
            # So that even if game is saved and retrieved. Hint continues getting displayed.
            if game.got_hint:
                special_char += "#"
            else:
                print("Good luck to you without that hint!")

        elif guess == "*":
            print("Print goodbye message. Exit.")
            print("Updating game.")
            game.update_fields_intermediate(game.got_hint, game.missed_letters, game.correct_letters, game.is_done)
            special_char += "*"
            exit()

        else:
            game.missed_letters = game.missed_letters + guess

        # Check if the player has guessed too many times and lost.
            if len(game.missed_letters) == len(HANGMAN_PICS)-1:
                display_board_game(game.missed_letters, game.correct_letters, special_char, game.hint, game.secret_word)
                print('You have run out of guesses!\nAfter ' + str(len(game.missed_letters)) + ' missed guesses and ' + str(len(game.correct_letters)) + ' correct guesses, the word was "' + game.secret_word + '"')
                game.is_done = True

    # If the game is done, ask the player to try again.
        if game.is_done:
            game.update_fields_end(game.got_hint, game.missed_letters, game.correct_letters, game.game_score, game.is_done, game.is_won)
            if play_again():
                print('|_H_A_N_G_M_A_N_|')
                game = Game(username)
                special_char = list()
                special_char.append(game.update_special_char())
            else:
                break
