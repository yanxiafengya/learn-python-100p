word_count = {}

with open('./beginner guide to python.txt',encoding="utf8") as fin:
    for line in fin:
        line = line[:-1]
        words = line.split()
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word]+=1

# print(word_count)

print(sorted(
    word_count.items(),
    key = lambda x:x[1],
    reverse=True
)[:10])