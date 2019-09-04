# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

def histogram(word):
    count = {}
    
    for letter in word:
        if letter == ' ': return TypeError('word cannot contain spaces')
        count[letter] = 0

    for letter in word:
        count[letter] += 1

    return count

word = str(input('please enter a non-space-containing word to recieve letter histogram: '))

print(histogram(word))