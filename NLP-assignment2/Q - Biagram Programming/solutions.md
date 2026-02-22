Bigram Language Model Implementation
Training corpus

<s> I love NLP </s>
<s> I love deep learning </s>
<s> deep learning isfun </s>

1. Unigram and Bigram Counts
Unigrams:

I = 2
love = 2
NLP = 1
deep = 2
learning = 2
isfun = 1
<s> = 3
</s> = 2
Bigrams:

<s> I = 2
<s> deep = 1
I love = 2
love NLP = 1
love deep = 1
deep learning = 2
learning </s> = 1
learning isfun = 1
NLP </s> = 1
isfun </s> = 1
2. Bigram Probabilities (MLE)
Formula:
[ P(w_i \mid w_{i-1}) = \frac{\text{count}(w_{i-1}, w_i)}{\sum_w \text{count}(w_{i-1}, w)} ]

Examples:

P(I | <s>) = 2/3
P(deep | <s>) = 1/3
P(love | I) = 2/2 = 1
P(NLP | love) = 1/2
P(deep | love) = 1/2
P(learning | deep) = 2/2 = 1
P( | NLP) = 1/1 = 1
P( | learning) = 1/2
P(isfun | learning) = 1/2
P( | isfun) = 1/1 = 1
3. Sentence Probabilities
Sentence 1: <s> I love NLP </s>
P = P(I | <s>) × P(love | I) × P(NLP | love) × P(</s> | NLP)
= (2/3) × 1 × (1/2) × 1
= 1/3 ≈ 0.3333

Sentence 2: <s> I love deep learning </s>
P = P(I | <s>) × P(love | I) × P(deep | love) × P(learning | deep) × P(</s> | learning)
= (2/3) × 1 × (1/2) × 1 × (1/2)
= 1/6 ≈ 0.1667

4. Preferred Sentence
The model assigns higher probability to <s> I love NLP </s> (0.3333 vs 0.1667).
Reason: after love, the continuation NLP is more likely (1/2) than the sequence leading to </s> through deep learning.
So the model prefers the shorter sentence with NLP.