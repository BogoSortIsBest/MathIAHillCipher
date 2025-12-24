import random
import enchant
import string

alphabet_string = (string.ascii_lowercase).upper()
alphabet_list = list(alphabet_string)


def start_game():
    anagramlist = []
    for num in range(10):
        letter = random.choice(alphabet_list)
        anagramlist.append(letter)
    print(anagramlist)
    input_word(anagramlist)


used_words = []
used_letters = []
points = 0
count = 0


def input_word(anagramlist):
    global used_words
    print("WELCOME TO ANAGRAMGAME\nTRY TO GET 10 HIGH POINT WORDS")
    play = True
    while play:
        inputted_word = input("enter a word using letters printed above: ").upper()
        print(" ")
        if inputted_word in used_words:
            print("you already used this word")
        if len(inputted_word) <= 2:
            print("word must be 3 letters or longer")
        elif (len(inputted_word) >= 3) and (inputted_word not in used_words):
            print(" ")
            anagramlist = anagramlist + used_letters
            used_letters.clear()
            print(anagramlist)
            check_letters(inputted_word, anagramlist, used_letters)


def check_letters(inputted_word, anagramlist, used_letters):
    not_in = False
    for letter in inputted_word:
        if letter not in anagramlist:
            print(letter + " is NOT in the list")
            not_in = True
            break
        elif letter in anagramlist:
            index = 0
            while index <= len(anagramlist):
                if anagramlist[index] == letter:
                    used_l = anagramlist.pop(index)
                    used_letters.append(used_l)
                    index += 1
                    break
                elif anagramlist[index] != letter:
                    index += 1
    if not_in != True:
        check_if_word(inputted_word)
        print(" ")
    else:
        print("INVALID WORD - you used letters that were not given")
        print(" ")
        print("points +0")
        print("TOTAL POINTS : " + str(points))


def check_if_word(inputted_word):
    global points
    global count
    d = enchant.Dict("en_US")
    if d.check(inputted_word) == False:
        print(str(inputted_word) + " is not a word :(")
        points += 0
        print("points +0")
        print("TOTAL POINTS : " + str(points))
    elif d.check(inputted_word) == True:
        print(str(inputted_word) + " is a word!!!")
        print(" ")
        used_words.append(inputted_word.upper())
        points += (len(inputted_word))
        print("points +" + str(len(inputted_word)))
        print("TOTAL POINTS : " + str(points))
        print(" ")
        count += 1
        if count == 10:
            print("CONGRATS YOU GOT 10 WORDS! FEEL FREE TO KEEP PLAYING")


start_game()