import numpy as np

# Confusion matrix
# Rows = predicted, Cols = gold
confusion = np.array([
    [5, 10, 5],   # Predicted Cat
    [15, 20, 10], # Predicted Dog
    [0, 15, 10]   # Predicted Rabbit
])

classes = ["Cat", "Dog", "Rabbit"]

# Per-class precision and recall
precisions = []
recalls = []

for i, cls in enumerate(classes):
    TP = confusion[i, i]
    FP = confusion[i, :].sum() - TP
    FN = confusion[:, i].sum() - TP
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    precisions.append(precision)
    recalls.append(recall)
    print(f"{cls}: Precision = {precision:.3f}, Recall = {recall:.3f}")

# Macro averages
macro_precision = sum(precisions) / len(classes)
macro_recall = sum(recalls) / len(classes)
print(f"\nMacro-averaged Precision = {macro_precision:.3f}")
print(f"Macro-averaged Recall = {macro_recall:.3f}")

# Micro averages
TP_total = sum(confusion[i, i] for i in range(len(classes)))
FP_total = sum(confusion[i, :].sum() - confusion[i, i] for i in range(len(classes)))
FN_total = sum(confusion[:, i].sum() - confusion[i, i] for i in range(len(classes)))

micro_precision = TP_total / (TP_total + FP_total)
micro_recall = TP_total / (TP_total + FN_total)

print(f"Micro-averaged Precision = {micro_precision:.3f}")
print(f"Micro-averaged Recall = {micro_recall:.3f}")