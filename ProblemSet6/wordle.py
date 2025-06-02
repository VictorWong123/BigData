import random

word_list = ['tests','extras','towel','tweak']

word = random.choice(word_list)
guess_word = '_____'
#hello
guess = 0
while guess<6: 
    user_word = input("Enter a 5 letter word: ")
    if user_word == word:
        print("You guessed it!")
        break
    for let in word: 
        for i, letter in enumerate(user_word):
            if user_word[i] == word[i]:
                guess_word = guess_word[:i] + user_word[i] + guess_word[i+1:]
            elif letter == let: 
                print(f'{letter} in word but not right place.')
    print(guess_word)
    guess+=1


