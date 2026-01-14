counts = {}

def count_words(sentence):
    # TODO: count each word in the sentence
    words = sentence.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

def run():
    sentence = "hello world hello data"
    count_words(sentence)
    print(counts)

if __name__ == "__main__":
    run()
