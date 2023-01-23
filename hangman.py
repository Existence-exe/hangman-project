import random
from stages import stages
wordlist = []

with open('words.txt', 'r') as f:
    for i in f.read().split():
        wordlist.append(i)


def gword():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
    full_word = '_'*len(word)
    counter = False
    gl = []
    gw = []
    tries = 6
    print('Hangman')
    print(display(tries))
    print(full_word + '\n')
    while not counter and tries > 0:
        n = input('Guess : ').upper()
        if len(n) == 1 and n.isalpha():
            if n in gl:
                print('Already guessed', n)
            elif n not in word:
                print(n, 'is not in the word')
                tries -= 1
                gl.append(n)
            else:
                print("Good job,", n, "is in the word!")
                gl.append(n)
                wal = list(full_word)
                indices = [i for i, letter in enumerate(word) if letter == n]
                for i in indices:
                    wal[i] = n
                    full_word = ''.join(wal)
                    if '_' not in full_word:
                        counter = True
        elif len(n) == len(word) and n.isalpha():
            if n in gw:
                print('Already guessed word', n)
            elif n != word:
                print(n, "is not the word")
                tries -= 1
                gw.append(n)
            else:
                counter = True
                full_word = word
        else:
            print('Yoo guess something better')
        print(display(tries))
        print(full_word + '\n')
    if counter:
        print('winner winner, Jeff Bezoz dinner')
    else:
        print('Lmao ran out of tries, SKILL ISSU' + f'\nThe word was {word}')


def display(tries):
    return stages[tries]


def ayoo():
    word = 'HELLO'
    play(word)
    while input("Play Again? (Y/N)").upper() in ['YES', 'Y', 'YEA']:
        word = gword()
        play(word)


if __name__ == "__main__":
    ayoo()
