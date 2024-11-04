def solve_knapsack():
    val = [15, 14, 10, 45, 30]  # Value array
    wt = [2, 5, 1, 3, 4]  # Weight array
    W = 7
    n = len(val) - 1

    def knapsack(W, n):  # (Remaining Weight, Number of items checked)
        # Base case
        if n < 0 or W <= 0:
            return 0

        # Higher weight than available
        if wt[n] > W:
            return knapsack(W, n - 1)

        else:
            return max(val[n] + knapsack(W - wt[n], n - 1), knapsack(W, n - 1))
            # max(including , not including)

    print(knapsack(W, n))


if __name__ == "__main__":
    solve_knapsack()
