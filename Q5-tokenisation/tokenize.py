# Tokenization Implementation
import spacy

# Paragraph for tokenization
text = "India is a diverse country. It has many languages, cultures, and traditions. People celebrate festivals like Diwali, Holi, and Eid."

# Naive tokenization (space-based)
naive_tokens = text.split()
print("Naive tokens:")
print(naive_tokens)

# Manual correction
manual_tokens = ['India','is','a','diverse','country','.',
                 'It','has','many','languages',',','cultures',',',
                 'and','traditions','.',
                 'People','celebrate','festivals','like',
                 'Diwali',',','Holi',',','and','Eid','.']
print("\nManual corrected tokens:")
print(manual_tokens)

# spaCy tokenizer
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_tokens = [token.text for token in doc]
print("\nspaCy tokens:")
print(spacy_tokens)

# Compare spaCy vs manual tokens
diff_manual_vs_spacy = [t for t in spacy_tokens if t not in manual_tokens] + \
                       [t for t in manual_tokens if t not in spacy_tokens]

print("\nTokens that differ between spaCy and manual:")
print(diff_manual_vs_spacy)