Worked Example Document Classification
Test document: predictable no fun

Given (from Q2)
Priors: P(−) = 3/5 = 0.6 ; P(+) = 2/5 = 0.4
Vocabulary size V = 20
Negative class total tokens = 14 → denominator = 14 + 20 = 34
From Q2:
count(predictable | −) = 2 → P(predictable | −) = (2+1)/34 = 3/34 ≈ 0.0882353
count(fun | −) = 0 → P(fun | −) = (0+1)/34 = 1/34 ≈ 0.0294118
Note: The count for "no" in the negative class is not given in the assignment. A numeric score for the negative class requires count(no | −). The calculation below shows the result assuming count(no | −) = 1 only to demonstrate steps; if you have the true count replace it in the same formula.

Negative class score (showing multiplication steps)
Assume count(no | −) = 1 → P(no | −) = (1+1)/34 = 2/34 ≈ 0.0588235

Likelihood:

P(d | −) = P(predictable | −) × P(no | −) × P(fun | −)
= (3/34) × (2/34) × (1/34)
Step-by-step:

3/34 × 2/34 = 6 / 1156 ≈ 0.0051860
0.0051860 × 1/34 = 6 / 39224 ≈ 0.000152985
Multiply by prior:

Score(−) = P(−) × P(d | −) = 0.6 × (6 / 39224) = 3.6 / 39224 ≈ 0.000091791
(If count(no | −) is different, replace 2 in the numerator above with (count(no|−)+1) and recompute.)

Positive class score
Using add-1 smoothing, the positive-class score is:

Denominator for positive class = (total_positive_tokens + V) — not given.
For each word w in the document: P(w | +) = (count(w | +) + 1) / (total_positive_tokens + V)
Thus:

P(d | +) = Π_{w ∈ {predictable, no, fun}} (count(w | +) + 1) / (total_positive_tokens + V)
Score(+) = P(+) × P(d | +)
Numeric value for Score(+) cannot be computed here because count(predictable|+), count(no|+), count(fun|+), and total_positive_tokens are not provided.

Decision
Numeric Score(−) is computed above (using count(no|−)=1 as an example): ~0.00009179.
Numeric Score(+) cannot be computed from the information given.
Conclusion: A final class assignment cannot be determined without the positive-class token counts (and total positive tokens). To decide, compute Score(+) using the positive counts and compare Score(−) vs Score(+).