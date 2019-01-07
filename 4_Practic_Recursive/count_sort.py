
import random

A = []
for i in range(30):
    A.append(random.randint(0, 9))
print(A)
F = [0] * 10
for x in A:
    F[x] += 1
print(F)

B = [ i for i in range(len(F)) for j in range(F[i])]
# for i in range(len(F)):
#     for j in range(F[i]):
#         B.append(i)
print(B)