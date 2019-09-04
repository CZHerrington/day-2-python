#Write a word_histogram program that asks the user for a sentence as its input,
# and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text.

sentence_list = str(input('please enter a sentence: ')).split(' ')
word_hist_dict = {}

for word in sentence_list:
    try:
        word_hist_dict[word]
    except:
        word_hist_dict[word] = 0
    finally:
        word_hist_dict[word] += 1

print(word_hist_dict)