def get_word():
    word = 'fluster'
    return word.lower()

def game(word):

    guessed = False
    guessed_letters = []
    word_progress = '_' * len(word)
    tries = 5

#    print(type(guessed_letters))
#    print(type(guessed_words))
#    print(type(word))
    print('--------------Start--------------')
    print(f'Word to guess: {word_progress}')

    while not guessed and tries > 0:
        guess = input('Input a guess: ').lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f'Already guessed this letter {guess}', )
            elif guess not in word:
                print(f'-{guess}- not in the word')
                tries -= 1
                print(f'Tries left: {tries}')
            else:
                print(f'You guessed right!, -{guess}- is in the word!')
                word_to_list = list(word_progress)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_to_list[index] = guess
                word_progress = "".join(word_to_list)
                if "_" not in word_progress:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess not in word:
                print(f'{guess} is not the word.')
                tries -= 1
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