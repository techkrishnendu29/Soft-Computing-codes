# Experiment 2: Fuzzy Set Operations (No x)
# Step 1: Define fuzzy sets
A = [0.2, 0.5, 0.7, 1.0]
B = [0.3, 0.4, 0.6, 0.8]
# Step 2: Initialize result lists
union = []
# Step 3: Union operation
for i in range(len(A)):
    if A[i] >= B[i]:
        union.append(A[i])
    else:
        union.append(B[i])
print(union)
