from nltk import FreqDist
from nltk import Text
from nltk.book import text6

from nltk import ngrams

# 前十个的频率
# fdist = FreqDist(text6)
# print(fdist.most_common(10))


# 'Sir', 'Robin'出现的次数
fourgrms = ngrams(text6, 2)
fourgrmsDist = FreqDist(fourgrms)
print(fourgrmsDist['Sir', 'Robin'])