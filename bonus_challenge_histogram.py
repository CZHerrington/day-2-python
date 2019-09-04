sentence_list = str(input('please enter a sentence: ')).split(' ')

def generate_histogram(sentence):
    word_hist_dict = {}

    for word in sentence_list:
        try:
            word_hist_dict[word]
        except:
            word_hist_dict[word] = 0
        finally:
            word_hist_dict[word] += 1
    return word_hist_dict

# only return top 3 words
def process_histogram(histogram):
    res = {}
    i = 0

    while i < 3:
        ref = 0
        for word in histogram:
            if histogram[word] > ref:
                ref = histogram[word]

        for word in histogram:
            if histogram[word] == ref:
                res[word] = ref
                histogram[word] = 0
                break

        i += 1
    return res

print(
    "top 3 most common words:\n",
    process_histogram(
        generate_histogram(sentence_list)
    )
)