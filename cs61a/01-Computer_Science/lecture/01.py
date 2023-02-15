# Numeric expressions
2023
2000 + 23
1 + 2 * 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()    # shakes.read().split() 将文本默认空格分割赋值给 text 变量
len(text)
text[:25]                       # 从前向后25个单词
text.count('the')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count(',')

# Sets
words = set(text)               # 将列表转换为集合（删除重复项）
len(words)

# Combinations 
'draw'
'draw'[0]
{w[0] for w in words}           # ‘{}’的集合形式会去除重复项，得到每个单词的头一个字符的去重集合

# Data
'draw'[::-1]                    # 倒叙
{w for w in words if w == w[::-1] and len(w)>4}     # 如果单词的长度大于4且为回文单词，添加到集合中
{w for w in words if w[::-1] in words and len(w) == 4}  # 如果单词的长度等于4且其逆序形式的单词也在集合中，添加到集合中
{w for w in words if w[::-1] in words and len(w) > 6}   # 如果单词的长度等于6且其逆序形式的单词也在集合中，添加到集合中

