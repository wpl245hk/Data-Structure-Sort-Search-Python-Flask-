import timeit

start = timeit.default_timer()

def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(min(weights), capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]   #"\n".join([str(y) for y in results])

print(knapsack_dp(165, [31, 23, 29, 44, 53, 38, 63, 85, 89, 82], [57, 92, 49, 68, 60, 43, 67, 84, 87, 72]))

print(timeit.default_timer() - start )



