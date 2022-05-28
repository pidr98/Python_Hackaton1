
def get_word():
    word = 'fluster'
    return word.lower()

def game(word):

    word_progress = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print(type(guessed_letters))
    print(type(guessed_words))
    print('--------------Start--------------')
    print('Word to guess: ',word_progress)

    while not guessed and tries > 0:
        guess = input('Input a guess: ').lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Already guessed this letter', guess)

            elif guess not in word:
                print(f'-{guess}- not in the word')
                tries -= 1
                print(f'Tries left: {tries}')
                guessed_letters.append(guess)

            else:
                print(f'You guessed right!, -{guess}- is in the word!')

                guessed_letters.append(guess)
                word_to_list = list(word_progress)
                indexes = [i for i, letter in enumerate(word) if letter == guess]

                for index in indexes:
                    word_to_list[index] = guess
                word_progress = "".join(word_to_list)
                if "_" not in word_progress:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                print(f'Tries left: {tries}')

            else:
                guessed = True
                word_progress = word
        else:
            print('Wrong input')

        print(word_progress)


    if guessed:
        print('You found the word!')
    else:
        print(f'You lost, the word was:{word}')



def main():
    word = get_word()
    game(word)

main()