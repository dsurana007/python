import os
print(os.getcwd())
#os.chdir(r"C:\Users\DhirajSurana\Downloads")
os.chdir("C:\\Users\DhirajSurana\Downloads")

print(os.getcwd())

dict_words={}
with open('data.txt','r') as f:
    text = f.read()
    print(text)
    words=text.split()
    print(words)
for word in words:
    dict_words[word] = dict_words.get(word,0) + 1
print(dict_words.items())

sorted_words = sorted(dict_words.items(),key=lambda x: x[1],reverse=True)
print(sorted_words)
print(dict(sorted_words[:5]))
