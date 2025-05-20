n = int(input())
s = [0] * (n + 1)

s[1] = 1
if n >= 2:
    s[2] = 3

for i in range(3, n + 1):
    s[i] = (s[i-1] + 2 * s[i-2]) % 10007

print(s[n])
