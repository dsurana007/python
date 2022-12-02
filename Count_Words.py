def count_words(n):
    d = {}

    with open('data.txt', 'r') as f:
        text = f.read()
        words = text.split()
        print(words)

        for word in words:
            d[word] = d.get(word, 0) + 1
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(sorted_d[:n+1])
        print(dict(sorted_d[:n+1]))

count_words(5)