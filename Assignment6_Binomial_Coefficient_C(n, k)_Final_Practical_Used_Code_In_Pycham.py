def binomial_coefficient(n, k):
    # Create a 2D list C with dimensions (n+1) x (k+1)
    C = []
    for _ in range(n + 1):
        C.append([0] * (k + 1))

    # Calculate the binomial coefficients
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1  # Base case: C(n, 0) = C(n, n) = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]  # Recursive relation

    return C[n][k]  # Return the value of C(n, k)

if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    k = int(input("Enter value of k: "))
    print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")
