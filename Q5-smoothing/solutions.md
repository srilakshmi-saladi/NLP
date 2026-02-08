# Q4 - smoothing

Add-1 (Laplace) Smoothing Example

Given

Priors: P(-) = 3/5, P(+) = 2/5

Vocabulary size: V = 20

Total tokens in negative documents: N- = 14

Add-1 smoothing formula:

P(word | class) = (count(word in class) + 1) / (total tokens in class + V)

Step 1: Compute the denominator for negative class

Denominator = total tokens in negative class + vocabulary size

N- + V = 14 + 20 = 34

✅ Denominator = 34

Step 2: Compute P(predictable | -)

Count of “predictable” in negative class = 2

P(predictable | -) = (2 + 1) / (14 + 20) = 3 / 34 ≈ 0.088

✅ Probability ≈ 0.088

Step 3: Compute P(fun | -)

Count of “fun” in negative class = 0

P(fun | -) = (0 + 1) / (14 + 20) = 1 / 34 ≈ 0.029

✅ Probability ≈ 0.029

Step 4: Summary Table

| Word         | Count in class | Probability P(word | -) |
|--------------|----------------|-------------------------|
| predictable  | 2              | 3 / 34 ≈ 0.088          |
| fun          | 0              | 1 / 34 ≈ 0.029          |