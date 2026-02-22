from collections import defaultdict

# Training corpus
corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "deep", "learning", "isfun", "</s>"]
]

# Count unigrams and bigrams
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

for sentence in corpus:
    for i, word in enumerate(sentence):
        unigram_counts[word] += 1
        if i < len(sentence) - 1:
            bigram = (word, sentence[i+1])
            bigram_counts[bigram] += 1

# Function to compute bigram probability (MLE)
def bigram_prob(w1, w2):
    return bigram_counts[(w1, w2)] / sum(
        bigram_counts[(w1, w)] for w in unigram_counts if (w1, w) in bigram_counts
    )

# Function to compute sentence probability
def sentence_prob(sentence):
    prob = 1.0
    for i in range(len(sentence) - 1):
        w1, w2 = sentence[i], sentence[i+1]
        prob *= bigram_prob(w1, w2)
    return prob

# Test sentences
s1 = ["<s>", "I", "love", "NLP", "</s>"]
s2 = ["<s>", "I", "love", "deep", "learning", "</s>"]

p1 = sentence_prob(s1)
p2 = sentence_prob(s2)

print("P(<s> I love NLP </s>) =", p1)
print("P(<s> I love deep learning </s>) =", p2)

if p1 > p2:
    print("The model prefers: <s> I love NLP </s>")
else:
    print("The model prefers: <s> I love deep learning </s>")