def spiral(n):
    matrix = [[0] * n for i in range(n)]
    count = 1
    for layer in range((n + 1) // 2):
        for i in range(layer, n - layer):
            matrix[layer][i] = count
            count += 1
        for i in range(layer + 1, n - layer):
            matrix[i][n - layer - 1] = count
            count += 1
        for i in range(layer + 1, n - layer):
            matrix[n - layer - 1][n - i - 1] = count
            count += 1
        for i in range(layer + 1, n - layer - 1):
            matrix[n - i - 1][layer] = count
            count += 1
    for row in matrix:
        print(" ".join(str(x).ljust(len(str(n*n))) for x in row))


m = int(input("Enter the number of spirals: "))
spiral(m)
