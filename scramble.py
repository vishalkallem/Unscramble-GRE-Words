__author__ = 'Vishal'

import random
from collections import Counter


def process(line):
    return line.split(":")[1].strip()


def get_level(line):
    return int(line.split(":")[0].strip()[-1])


def shuffle(word_to_jumble):
    jumbled_word = list(word_to_jumble)
    random.shuffle(jumbled_word)
    return "".join(jumbled_word)


def generate_level_words(level):
    level_words = []
    with open("Membean_words.txt", mode='rt') as file:
        for line in file:
            if get_level(line=line) == level:
                level_words.append(process(line=line))
    return level_words


def meaning(line):
    return line.split(":")[2].strip()


def get_meanings(words_list):
    meanings = {}
    with open("Membean_words.txt", mode='rt') as file:
        for line in file:
            level = get_level(line=line)
            word = process(line=line)
            if word in words_list:
                meanings[word] = [meaning(line=line), level]
                if len(meanings) == len(words_list):
                    return meanings
    return None


def is_unscrambled_word(orig, candidate, n):
    if len(candidate) == n:
        given_word_counter = Counter(orig)
        word_counter = Counter(candidate)
        given_word_counter.subtract(word_counter)
        if not any([c < 0 for c in given_word_counter.values()]):
            return True
    return False


def get_unscrambled_words_main(input_word, n, level):
    unscrambled_words = []
    with open("Membean_words.txt", mode='rt') as infile:
        for line in infile:
            if get_level(line) <= level:
                word = process(line)
                if is_unscrambled_word(orig=input_word, candidate=word, n=n):
                    unscrambled_words.append(word)
    return unscrambled_words


def get_all_possible_words(word, level):
    all_words = []
    for i in range(4, len(word) + 1):
        all_words.extend(get_unscrambled_words_main(input_word=word, n=i, level=level))
    return all_words


def generate_word(level):
    word = random.choice(generate_level_words(level=level))
    solution = get_all_possible_words(word=word, level=level)
    return word, shuffle(word_to_jumble=word), solution


def print_guessed_words_meanings(guessed_words, meanings):
    if not guessed_words:
        print("No words were guessed correctly")
    for word in guessed_words:
        if word in meanings.keys():
            print(f"Level: {meanings[word][1]}")
            print(f"{word.title()}: {meanings[word][0].capitalize()}")
            print(f"For detailed meaning you can visit: https://vocabulary.com/dictionary/{word}")


def main():
    print("Enter the level you want to play: ")
    level, play = int(input()), True
    session_words = []

    while play:

        word_to_jumble, jumbled_word, all_possible_words = generate_word(level=level)

        while jumbled_word in session_words:
            word_to_jumble, jumbled_word, all_possible_words = generate_word(level=level)

        session_words.append(word_to_jumble)

        correct_answers, attempts = 0, 0
        meanings = get_meanings(all_possible_words)

        print("Press G to give up\nS to shuffle the letters\nM to know the meaning of the guessed word")

        guessed_words = []

        while correct_answers != len(all_possible_words):
            print("   ".join(list(jumbled_word)))
            print('Enter your answer: ')
            guess = input()
            attempts += 1

            if guess in ['G', 'g']:
                print(all_possible_words)
                break

            elif guess in ['M', 'm']:
                print_guessed_words_meanings(guessed_words=guessed_words, meanings=meanings)

            elif guess in ['S', 's']:
                jumbled_word = shuffle(word_to_jumble=jumbled_word)

            elif guess in all_possible_words:
                guessed_words.append(guess)
                correct_answers += 1

            else:
                print("Wrong Guess!")
                if attempts > 10:
                    hint_word = random.choice(all_possible_words)
                    while hint_word in guessed_words:
                        hint_word = random.choice(all_possible_words)
                    print(f"Hint {attempts//10}: The starting letters of one of the words is: {hint_word[:attempts//10]}")

        print_guessed_words_meanings(guessed_words=all_possible_words, meanings=meanings)

        print("Do you wish to continue?[Y/N]")
        if input()[0] in ['N', 'n']:
            play = False


if __name__ == "__main__":
    main()
