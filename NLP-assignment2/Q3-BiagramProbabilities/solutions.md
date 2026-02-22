Bigram Probabilities and the Zero-Probability Problem
Given bigram counts (only non-zero entries shown).

1. Bigram sentence probabilities (MLE)
Recall: P(w_i | w_{i-1}) = count(w_{i-1}, w_i) / total_count(w_{i-1})

Totals used:

total(\<s\>) = 2 + 1 = 3
total(I) = 2
total(love) = 1 + 1 = 2
total(deep) = 2
total(learning) = 1 + 1 = 2
total(NLP) = 1
total(ate) = 6 + 3 + 2 + 1 = 12
S1: \<s\> I love NLP \</s\>
P(S1) = P(I | \<s\>) * P(love | I) * P(NLP | love) * P(\</s\> | NLP)
P(I | \<s\>) = 2/3
P(love | I) = 2/2 = 1
P(NLP | love) = 1/2
P(\</s\> | NLP) = 1/1 = 1
P(S1) = (2/3) * 1 * (1/2) * 1 = 1/3 ≈ 0.3333

S2: \<s\> I love deep learning \</s\>
P(S2) = P(I | \<s\>) * P(love | I) * P(deep | love) * P(learning | deep) * P(\</s\> | learning)
P(I | \<s\>) = 2/3
P(love | I) = 1
P(deep | love) = 1/2
P(learning | deep) = 2/2 = 1
P(\</s\> | learning) = 1/2
P(S2) = (2/3) * 1 * (1/2) * 1 * (1/2) = 1/6 ≈ 0.1667

Which is more probable?
S1 is more probable (0.3333 > 0.1667).

2. Zero-probability problem
a) MLE for P(noodle | ate)
count(noodle | ate) = 0, total after "ate" = 12
P(noodle | ate) = 0 / 12 = 0

b) Why this is a problem
If any conditional probability in a sentence is zero, the whole sentence probability (product of bigram probabilities) becomes zero. This makes sentence probability and perplexity unusable when unseen bigrams occur.

c) Laplace (add-1) smoothing
Given: V = 10, total after "ate" = 12.
P_smooth(noodle | ate) = (count + 1) / (total + V) = (0 + 1) / (12 + 10) = 1 / 22 ≈ 0.04545

This non-zero value avoids the zero-probability problem.