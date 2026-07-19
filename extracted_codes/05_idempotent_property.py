# ---------------- IDEMPOTENT PROPERTY ----------------
A = [0.2, 0.5, 0.7, 1.0]
union_AA = []
intersection_AA = []
for i in range(len(A)):
    # Union and intersection of a set with itself
    union_AA.append(max(A[i], A[i]))
    intersection_AA.append(min(A[i], A[i]))
# Step 5: Display idempotent property result
print("Idempotent Property:")
print("A ∪ A =", union_AA)
print("A ∩ A =", intersection_AA)
