# CODEME_Hackaton1

### Hangman game
Program is designed to retrieve a letter or a whole word from the user (it must be the same length as the word to guess), and then
check if a predetermined word or one of its letters matches what the user has entered.
Length of the answer is shown to the player using underscores.

### Answer concept

In function def word() we create variable that will hold our word to guess. Also, it's letters are changed to lower for future.

Next is function def game(word) that gets word from function def word(), check length of this word
and show it to the player using underscores. After that, using while loop it check if the answer is already guessed or not or if player have any tries left.
If player have lives left and didn't find whole word, there is 'if else' statement: if, check if input length is 1 and is letter. If false, wrong input. If true:
* if guess were guessed earlier, try again
* elif input is not in word, print 'letter not in word', subtract 1 from varialbe 'tries' and print tries left.
* else, change word to list, get index and the letter at the index for each iteration, if letter = guess, replace underscore with guessed letter and convert it back to the string. Check if there is any '_' left.

If user write whole word, check if word length = input length and is a letter.
* if guess is not in word, tries - 1, tries left
* else change guessed to True and change word_progress to word. 

Then, if guessed is True, print 'found the word'
If guessed is False, print 'you lost, the word was "word"'

In main we put everything together and run.