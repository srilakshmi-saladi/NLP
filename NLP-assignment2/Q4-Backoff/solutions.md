Backoff Model
Training corpus
<s> I like cats </s>
<s> I like dogs </s>
<s> You like cats </s>

Counts

I like = 2
You like = 1
like cats = 2
like dogs = 1
cats </s> = 2
dogs </s> = 1
1. Compute P(cats | I, like)
Using trigram MLE:

[ P(\text{cats} \mid I, like) = \frac{\text{count}(I;like;cats)}{\text{count}(I;like)} ]

I like cats = 1
I like = 2
[ P(\text{cats} \mid I, like) = \frac{1}{2} = 0.5 ]

2. Compute P(dogs | You, like) using trigram → bigram backoff
The trigram You like dogs does not appear (count = 0), so we back off to the bigram like dogs.

[ P(\text{dogs} \mid like) = \frac{\text{count}(like;dogs)}{\sum_w \text{count}(like;w)} ]

like dogs = 1
like cats + like dogs = 2 + 1 = 3
[ P(\text{dogs} \mid You, like) \approx P(\text{dogs} \mid like) = \frac{1}{3} \approx 0.3333 ]

3. Why backoff is necessary
The training corpus is very small, so many trigrams are unseen.
If we only relied on trigram counts, unseen trigrams would get probability 0, and whole sentences containing them would also get probability 0.

Backoff avoids this by falling back to lower-order n-grams (bigram or unigram), ensuring non-zero probabilities and more reliable predictions under data sparsity.