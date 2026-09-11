import getpass

active_game = True


def setup_hangman(phrase):
    hangman = ""

    for char in phrase:
        if char == " ":
            hangman += "   "
        else:
            hangman += "_ "

    return hangman


while active_game:

    # Get player input for word to guess
    phrase = getpass.getpass("Choose a word to guess: ").lower()

    # Make sure a word was actually entered
    while not phrase:
        print("You must enter a word.")
        phrase = getpass.getpass("Choose a word to guess: ").lower()

    phrase_len = len(phrase)

    # Set up game variables
    guesses_left = 9
    guessed_letters = []

    print("\n" * 3)
    print("=== HANGMAN ===")
    print(f"You have {guesses_left} guesses.")
    print(setup_hangman(phrase))

    # Game loop
    while guesses_left > 0:

        # Display current state of the word
        display_word = ""

        for char in phrase:
            if char == " ":
                display_word += "   "
            elif char in guessed_letters:
                display_word += char + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Guessed letters:", " ".join(guessed_letters))
        print("Guesses remaining:", guesses_left)

        # Check if the player has guessed the entire word
        word_complete = True

        for char in phrase:
            if char != " " and char not in guessed_letters:
                word_complete = False
                break

        if word_complete:
            print("\nCongratulations! You guessed the word!")
            print("The word was:", phrase)
            break

        # Get a guess
        guess = input("\nGuess a letter: ").lower()

        # Make sure only one character was entered
        if len(guess) != 1:
            print("Please enter one letter at a time.")
            continue

        # Make sure the guess is a letter
        if not guess.isalpha():
            print("Please enter a letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        # Add the guess to the list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in phrase:
            print("Correct!")
        else:
            guesses_left -= 1
            print("Incorrect!")

    # Check if the player ran out of guesses
    if guesses_left == 0:

        display_word = ""

        for char in phrase:
            if char == " ":
                display_word += "   "
            else:
                display_word += char + " "

        print("\nYou ran out of guesses!")
        print("The word was:", phrase)

    # Ask whether to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()

        if play_again == "y":
            break

        elif play_again == "n":
            active_game = False
            print("\nThanks for playing!")
            break

        else:
            print("Please enter y or n.")
