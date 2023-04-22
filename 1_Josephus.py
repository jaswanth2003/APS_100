def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k-1) % n + 1


n = 7 # number of people
k = 3 # every 3rd person is eliminated
print(josephus(n, k)) # output: 4
