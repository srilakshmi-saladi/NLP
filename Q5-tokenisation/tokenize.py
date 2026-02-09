"""
Q5. Tokenization Programming Question

This program demonstrates:
1. Naive space-based tokenization
2. Manual token correction (handling punctuation)
3. Tokenization using an NLP tool (spaCy)
4. Comparison of outputs
5. Identification of Multiword Expressions (MWEs)
6. Reflection on tokenization challenges
"""

import spacy

# --------------------------------------------------
# STEP 1: Input paragraph (3 sentences)
# --------------------------------------------------
# This is the paragraph we want to tokenize.
# It contains punctuation and proper nouns.
text = (
    "India is a diverse country. "
    "It has many languages, cultures, and traditions. "
    "People celebrate festivals like Diwali, Holi, and Eid."
)

print("Original Paragraph:")
print(text)
print("-" * 60)


# --------------------------------------------------
# STEP 2: Naive space-based tokenization
# --------------------------------------------------
# This method simply splits the text using spaces.
# It does NOT handle punctuation correctly.
naive_tokens = text.split()

print("Naive Space-Based Tokens:")
print(naive_tokens)
print("-" * 60)


# --------------------------------------------------
# STEP 3: Manual token correction
# --------------------------------------------------
# Here we manually correct the tokens by:
# - Separating punctuation marks
# - Keeping words and punctuation as separate tokens
manual_tokens = [
    'India', 'is', 'a', 'diverse', 'country', '.',
    'It', 'has', 'many', 'languages', ',', 'cultures', ',', 'and', 'traditions', '.',
    'People', 'celebrate', 'festivals', 'like',
    'Diwali', ',', 'Holi', ',', 'and', 'Eid', '.'
]

print("Manually Corrected Tokens:")
print(manual_tokens)
print("-" * 60)


# --------------------------------------------------
# STEP 4: Highlight differences between naive and manual tokens
# --------------------------------------------------
# This shows which tokens were incorrectly handled
# by naive tokenization.
diff_naive_manual = (
    [token for token in naive_tokens if token not in manual_tokens] +
    [token for token in manual_tokens if token not in naive_tokens]
)

print("Differences between Naive and Manual Tokens:")
print(diff_naive_manual)
print("-" * 60)


# --------------------------------------------------
# STEP 5: Tokenization using spaCy (NLP tool)
# --------------------------------------------------
# spaCy automatically handles punctuation and token rules.
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

spacy_tokens = [token.text for token in doc]

print("spaCy Tokenizer Output:")
print(spacy_tokens)
print("-" * 60)


# --------------------------------------------------
# STEP 6: Compare spaCy tokens with manual tokens
# --------------------------------------------------
# Ideally, spaCy tokens should match manual correction.
diff_manual_spacy = (
    [token for token in spacy_tokens if token not in manual_tokens] +
    [token for token in manual_tokens if token not in spacy_tokens]
)

print("Differences between Manual and spaCy Tokens:")
print(diff_manual_spacy)
print("-" * 60)


# --------------------------------------------------
# STEP 7: Multiword Expressions (MWEs)
# --------------------------------------------------
# MWEs are phrases that should be treated as a single unit.
mwes = [
    "New York",
    "kick the bucket",
    "according to"
]

print("Multiword Expressions (MWEs):")
for mwe in mwes:
    print("-", mwe)

print(
    "\nReason: These expressions have a single meaning and "
    "splitting them into separate words would lose that meaning."
)
print("-" * 60)


# --------------------------------------------------
# STEP 8: Reflection
# --------------------------------------------------
# Reflection on the challenges of tokenization.
print("Reflection:")
print(
    "The hardest part of tokenization is handling punctuation and fixed expressions.\n"
    "Naive space-based tokenization fails because it attaches punctuation to words.\n"
    "Compared to English, tokenization in morphologically rich languages is more complex.\n"
    "Punctuation, suffixes, and MWEs make tokenization difficult.\n"
    "NLP tools like spaCy handle most cases well, but manual review is still important.\n"
    "Accurate tokenization is essential for reliable NLP performance."
)
print("-" * 60)
