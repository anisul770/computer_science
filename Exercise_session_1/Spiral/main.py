def build_ring(matrix, ring, start):
    n = len(matrix)
    for col in range(ring, n-ring):
        matrix[ring][col] = start
        start += 1
    for row in range(ring+1, n-ring):
        matrix[row][n-ring-1] = start
        start += 1
    for col in range(n-ring-2, ring-1, -1):
        matrix[n-ring-1][col] = start
        start += 1
    for row in range(n-ring-2, ring, -1):
        matrix[row][ring] = start
        start += 1
    return start


def main():

    n = int(input('What is the size of the table? '))
    matrix = list()
    for i in range(0, n):
        matrix.append([0]*n)

    start = 1
    for ring in range(n//2):
        start = build_ring(matrix, ring, start)

    if n % 2 == 1:
        matrix[n//2][n//2] = start

    for row in matrix:
        for col in row:
            print(col, end='\t')
        print('')


main()
