# Experiment 3: Properties of Fuzzy Sets
# This program verifies commutative, associative, and idempotent properties
# Step 1: Define fuzzy sets (membership values only)
A = [0.2, 0.5, 0.7, 1.0]
B = [0.3, 0.4, 0.6, 0.8]
C = [0.1, 0.6, 0.9, 0.5]
union_AB = []
union_BA = []
# ---------------- COMMUTATIVE PROPERTY ----------------
# Union: A ∪ B and B ∪ A
for i in range(len(A)):
    # Maximum membership value represents union
    union_AB.append(max(A[i], B[i]))
    union_BA.append(max(B[i], A[i]))
union_AB,union_BA
