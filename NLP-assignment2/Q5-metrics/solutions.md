 Evaluation Metrics from a Multi-Class Confusion Matrix
Confusion Matrix (System \ Gold)
Cat	Dog	Rabbit
Cat	5	10	5
Dog	15	20	10
Rabbit	0	15	10
Total animals = 90

1. Per-Class Precision and Recall
Cat

TP = 5
FP = 15 (from Dog) + 0 (from Rabbit) = 15
FN = 10 (from Dog) + 5 (from Rabbit) = 15
Precision = 5 / (5 + 15) = 5 / 20 = 0.25
Recall = 5 / (5 + 15) = 5 / 20 = 0.25
Dog

TP = 20
FP = 10 (from Cat) + 15 (from Rabbit) = 25
FN = 15 (from Cat) + 10 (from Rabbit) = 25
Precision = 20 / (20 + 25) = 20 / 45 ≈ 0.444
Recall = 20 / (20 + 25) = 20 / 45 ≈ 0.444
Rabbit

TP = 10
FP = 5 (from Cat) + 10 (from Dog) = 15
FN = 5 (from Cat) + 10 (from Dog) = 15
Precision = 10 / (10 + 15) = 10 / 25 = 0.40
Recall = 10 / (10 + 15) = 10 / 25 = 0.40
2. Macro vs Micro Averaging
Macro-averaged Precision = (0.25 + 0.444 + 0.40) / 3 ≈ 0.365
Macro-averaged Recall = (0.25 + 0.444 + 0.40) / 3 ≈ 0.365

Micro-averaged Precision = total TP / (total TP + total FP)

Total TP = 5 + 20 + 10 = 35
Total FP = 15 + 25 + 15 = 55
Micro Precision = 35 / (35 + 55) = 35 / 90 ≈ 0.389
Micro-averaged Recall = total TP / (total TP + total FN)

Total FN = 15 + 25 + 15 = 55
Micro Recall = 35 / (35 + 55) = 35 / 90 ≈ 0.389
3. Difference between Macro and Micro
Macro averaging: treats all classes equally. Each class gets the same weight, no matter how many samples it has.
Micro averaging: counts all decisions together. Bigger classes influence the score more.
So macro is fairer across classes, while micro reflects overall accuracy across all data.