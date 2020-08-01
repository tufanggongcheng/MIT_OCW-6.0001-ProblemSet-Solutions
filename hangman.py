# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    i = 0
    secret_word_list = list(secret_word)
    for char in secret_word_list:
        if char in letters_guessed:
            i += 0
        else:
            i += 1
    return i == 0


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list = list(secret_word)
    for i in range(len(secret_word)):
        if secret_word_list[i] not in letters_guessed:
            secret_word_list[i] = "_ "
    return(''.join(secret_word_list))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list(string.ascii_lowercase)
    alphabet_copy = alphabet[:]
    for char in alphabet_copy:
        if char in letters_guessed:
            alphabet.remove(char)
    return(''.join(alphabet))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    letters_guessed = []
    m = 3
    n = 6
    secret_word_list = list(secret_word)
    vowels = ["a", "o", "e", "i", "u"]
    consonants = list(string.ascii_lowercase)
    for char in vowels:
        consonants.remove(char)
    while n > 0 :
        print("You have", n, "guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        new_letter = input("Please guess a letter: ").lower()[0]
        if new_letter in get_available_letters(letters_guessed):
            letters_guessed.append(new_letter)
            if letters_guessed[-1] in secret_word_list:
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            elif letters_guessed[-1] in vowels:
                n -= 2
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            else:
                n -= 1
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))

        elif new_letter in letters_guessed and m >= 0:
            if m > 0:
                m -= 1
                print("Oops! You've already guessed that letter. You now have", m , "warnings left:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + get_guessed_word(secret_word, letters_guessed))
                n -= 1

        else:
            if m > 0:
                m -= 1
                print("Oops! That is not a valid letter. You have", m , "warnings left:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + get_guessed_word(secret_word, letters_guessed))
                n -= 1
                
        print("-----------------------------------")
    if n <= 0 :
        print("Sorry, you ran out of guesses. The word was " + secret_word)

        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    my_word_list = list(my_word.replace(" ",""))
    other_word_list = list(other_word)
    i = 0
    forbit_list = []
    check_list = []
    if len(my_word_list) == len(other_word_list):
        for n in range(len(my_word_list)):
            if my_word_list[n] == other_word_list[n]:
                i += 0
                forbit_list.append(my_word_list[n])
                
            elif my_word_list[n] == "_" :
                check_list.append(other_word_list[n])
                i += 0
            else:
                i += 1

        for char in check_list:
            if char in forbit_list:
                i += 1
                    
        return i == 0
    
    else:
        return False    

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    match_list = []
    for n in range(len(wordlist)):
        if match_with_gaps(my_word, wordlist[n]):
            match_list.append(wordlist[n])
    if len(match_list) != 0:
        print(' '.join(match_list))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have 3 warnings left.")
    letters_guessed = []
    m = 3
    n = 6
    score_list = []
    secret_word_list = list(secret_word)
    for c in range(len(secret_word_list)):
        if secret_word_list[c] not in score_list:
            score_list.append(secret_word_list[c])
    vowels = ["a", "o", "e", "i", "u"]
    consonants = list(string.ascii_lowercase)
    for char in vowels:
        consonants.remove(char)
    while n > 0 and not is_word_guessed(secret_word, letters_guessed):

        print("You have", n, "guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        new_letter = input("Please guess a letter: ").lower()[0]
        if new_letter == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                
        elif new_letter in get_available_letters(letters_guessed):
            letters_guessed.append(new_letter)
            if letters_guessed[-1] in secret_word_list:
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            elif letters_guessed[-1] in vowels:
                n -= 2
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            else:
                n -= 1
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
    
        elif new_letter in letters_guessed and m >= 0:
            if m > 0:
                m -= 1
                print("Oops! You've already guessed that letter. You now have", m , "warnings left:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + get_guessed_word(secret_word, letters_guessed))
                n -= 1
    
        else:
            if m > 0:
                m -= 1
                print("Oops! That is not a valid letter. You have", m , "warnings left:" + get_guessed_word(secret_word, letters_guessed))
            else:
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + get_guessed_word(secret_word, letters_guessed))
                n -= 1
                    
        print("-----------------------------------")
    if n <= 0 :
        print("Sorry, you ran out of guesses. The word was " + secret_word)
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is: ", n*len(score_list))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

# if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
