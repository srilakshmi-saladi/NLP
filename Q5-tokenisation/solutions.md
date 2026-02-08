# Q5 – Tokenization

This file contains answers for the tokenization task.

---

## 1. Tokenize a paragraph
**Paragraph (example, 3–4 sentences):**

"India is a diverse country. It has many languages, cultures, and traditions. People celebrate festivals like Diwali, Holi, and Eid."

**Naïve space-based tokenization:**
['India', 'is', 'a', 'diverse', 'country.', 'It', 'has', 'many', 'languages,', 'cultures,', 'and', 'traditions.', 'People', 'celebrate', 'festivals', 'like', 'Diwali,', 'Holi,', 'and', 'Eid.']

**Manual correction (handling punctuation properly):**
['India', 'is', 'a', 'diverse', 'country', '.', 'It', 'has', 'many', 'languages', ',', 'cultures', ',', 'and', 'traditions', '.', 'People', 'celebrate', 'festivals', 'like', 'Diwali', ',', 'Holi', ',', 'and', 'Eid', '.']

**Main difference:** In the naive method, punctuation (.,) got attached to words. In the corrected version, punctuation is separated.

---

## 2. Compare with a Tool (spaCy)

**Tool output (spaCy):**  
['India', 'is', 'a', 'diverse', 'country', '.', 'It', 'has', 'many', 'languages', ',', 'cultures', ',', 'and', 'traditions', '.', 'People', 'celebrate', 'festivals', 'like', 'Diwali', ',', 'Holi', ',', 'and', 'Eid', '.']

**Comparison:**  
- spaCy output is very close to my manual correction.  
- Punctuation like `,` and `.` is separated correctly.  
- The naïve method kept punctuation attached to words.

**Tokens that differ between spaCy and manual correction:** []  
**Reason:** spaCy separated punctuation correctly, so it matches manual tokens exactly.


---

## 3. Multiword Expressions (MWEs)
Examples of MWEs in English:
1. **New York** → place name, should be treated as one token.  
2. **kick the bucket** → idiom, means "to die", not just words separately.  
3. **machine learning** → fixed phrase in CS, better as one token.

Reason: MWEs carry one meaning, so splitting them may lose context.

---

## 4. Reflection
- The hardest part of tokenization in my language (English here) was separating punctuation and handling MWEs.  
- Compared to English, some other languages (like Hindi) have more complex word forms, so tokenization is harder.  
- Punctuation and clitics often make simple space-based tokenization fail.  
- MWEs also add difficulty because meaning is lost if words are split.  
- Tools like spaCy do a better job since they are trained on large corpora.  