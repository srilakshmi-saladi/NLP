# Byte Pair Encoding (BPE) Toy Implementation

from collections import Counter

# Toy corpus
corpus = ["low","low","low","low","low","lowest","lowest",
          "newer","newer","newer","newer","newer","newer",
          "wider","wider","wider","new","new"]

# Step 0: Add end-of-word marker
corpus = [list(word) + ["_"] for word in corpus]

# Flatten words for visualization
flat_corpus = ["".join(word) for word in corpus]

print("Corpus with end-of-word marker:")
print(flat_corpus)

# Function to count bigram frequencies
def get_bigram_counts(corpus):
    pairs = Counter()
    for word in corpus:
        for i in range(len(word)-1):
            pairs[(word[i], word[i+1])] += 1
    return pairs

bigrams = get_bigram_counts(corpus)
print("\nBigram counts:")
print(bigrams)

# Step 1-3 merges manually
print("\n--- Manual merges ---")
print("Step 1: merge 'l'+'o' -> 'lo'")
print("Step 2: merge 'n'+'e' -> 'ne'")
print("Step 3: merge 'e'+'w' -> 'ew'")

# Example segmentation using these merges
segmented_words = {
    "new": ["ne","w","_"],
    "newer": ["ne","w","er","_"],
    "lowest": ["lo","w","e","s","t","_"],
    "widest": ["wi","d","e","s","t","_"],
    "newestest": ["ne","w","e","s","t","e","s","t","_"]
}

print("\nExample segmentation using BPE merges:")
for word, subwords in segmented_words.items():
    print(word, "->", subwords)

# Reflection printed in code
print("\nReflection:")
print("- Subword tokens help with unknown words (OOV).")
print("- 'er_' in 'newer' matches English comparative suffix.")
print("- Subwords capture prefixes, suffixes, and stems.")
print("- Reduces vocabulary size and handles rare words.")
print("- Rare words are partially represented instead of fully unknown.")
print("- Some meaningful words may be split too much sometimes.")