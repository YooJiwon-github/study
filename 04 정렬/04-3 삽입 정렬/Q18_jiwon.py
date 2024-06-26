N = int(input())
A= list(map(int, input()))
S = [0]*N

result = 0

for i in range(1, N):
    point = i
    value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            point = j + 1
            break
        if j == 0:
            point = 0
    for j in range(i, point, -1):
        A[j] = A[j-1]
    A[point] = value

S[0] = A[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]

print(sum(S))
