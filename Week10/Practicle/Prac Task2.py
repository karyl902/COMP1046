from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my',
    'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_3 = word_counts.most_common(3)

for word, count in top_3:
    print ("Word:" + word + ",count:" + str(count))