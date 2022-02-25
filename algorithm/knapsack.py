"""
fill backpack with most valuable items
"""

def knapsack(N, W, wt, val):
    # determin state: volume of knapsack; number of items stored in knapsack
    dp =[[0] * W] * N
    for n in range(N):
        for w in range(W):
            # choices: if knapsack has enough spaces, find the best between pack-it and not-pack;
            if w < wt[n]:
                dp[n][w] = dp[n-1][w]
            else:
                dp[n][w] = max(
                    dp[n-1][w],
                    dp[n-1][w-wt[n]] + val[n]
                )
    return dp[N-1][W-1]

N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

print(knapsack(N, W, wt, val))