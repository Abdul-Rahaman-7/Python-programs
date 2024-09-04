def most_frequent_words(filename, n):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

filename = input("enter the filename: ")
n = int(input("enter the number of most frequent words to find: "))
result = most_frequent_words(filename, n)
print(f"the {n} most frequent words are:")
for word, freq in result:
    print(f"{word}: {freq}")
