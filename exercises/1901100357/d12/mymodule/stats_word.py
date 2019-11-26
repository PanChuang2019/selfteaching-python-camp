# encoding=utf-8
from collections import Counter 
import jieba

# 统计参数中每个英文单词出现的次数
def stats_text_en(text, count):
	elements = text.split()
	words = []
	symbols = ',.*-!?'
	for element in elements:
		for symbol in symbols:
			element = element.replace(symbol, '')
		if len(element) and element.isascii():
			words.append(element)
	return Counter(words).most_common(int(count))


# 统计参数中每个中文汉字出现的次数
def stats_text_cn(text, count):
	words = jieba.cut(text)
	tmp = []
	for i in words:
		if len(i) > 1:
			tmp.append(i)
	return Counter(tmp).most_common(count)
	


def stats_text(text, count):

	return stats_text_en(text, count) + stats_text_cn(text,count)

# if __name__ == "__main__":
# 	text = "他来到了网易杭研大厦,网易杭研大厦,网易杭研"
# 	stats_text_cn(text, 10)
