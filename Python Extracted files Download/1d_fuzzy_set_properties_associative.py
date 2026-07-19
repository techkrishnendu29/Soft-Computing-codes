# ---------------- ASSOCIATIVE PROPERTY ----------------
A = [0.2, 0.5, 0.7, 1.0]
B = [0.3, 0.4, 0.6, 0.8]
C = [0.1, 0.6, 0.9, 0.5]
union_AB = []
union_BA = []
# (A ∪ B) ∪ C
union_AB_C = []
for i in range(len(A)):
    union_AB_C.append(max(max(A[i], B[i]), C[i]))
# A ∪ (B ∪ C)
union_A_BC = []
for i in range(len(A)):
    union_A_BC.append(max(A[i], max(B[i], C[i])))
# (A ∩ B) ∩ C
intersection_AB_C = []
for i in range(len(A)):
    intersection_AB_C.append(min(min(A[i], B[i]), C[i]))
# A ∩ (B ∩ C)
intersection_A_BC = []
for i in range(len(A)):
    intersection_A_BC.append(min(A[i], min(B[i], C[i])))
# Step 4: Display associative property result
print("Associative Property:")
print("(A ∪ B) ∪ C =", union_AB_C)
print("A ∪ (B ∪ C) =", union_A_BC)
print("(A ∩ B) ∩ C =", intersection_AB_C)
print("A ∩ (B ∩ C) =", intersection_A_BC)
print()
