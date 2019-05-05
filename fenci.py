# encoding=utf-8
import jieba
from click._compat import raw_input

#  for stopWords<br># stopwords = []<br># for word in open("stopwords.txt", "r"):<br>#     stopwords.append(word.strip())
stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]
#  add extra stopword
stopwords.append('');
stopwords.append('    ')
stopwords.append('')
stopwords.append('  ')
stopwords.append(' ')

# tongyici
combine_dict = {}
for line in open("dict.txt", "r"):
    seperate_word = line.strip().split("\t")
    num = len(seperate_word)
    for i in range(1, num):
        combine_dict[seperate_word[i]] = seperate_word[0]

# read need analyse file
article = open("test.txt", "r",encoding="utf-8").read()
words = jieba.cut(article, cut_all=False)
#  count word freq
word_freq = {}
for word in words:
    if (word in stopwords):
        continue
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
#  sorted    
freq_word = []
for word, freq in word_freq.items():
    freq_word.append((word, freq))
freq_word.sort(key=lambda x: x[1], reverse=True)
max_number = int(raw_input("需要前多少位高频词？ "))
# display
for word, freq in freq_word[:max_number]:
    print(word, freq)