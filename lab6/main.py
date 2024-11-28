class Matrix:
    @staticmethod
    def sort_columns(matrix):
        n = len(matrix)
        m = len(matrix[0])

        for col in range(m):
            for i in range(n):
                min_idx = i

                for j in range(i + 1, n):
                    if matrix[j][col] < matrix[min_idx][col]:
                        min_idx = j

                matrix[i][col], matrix[min_idx][col] = matrix[min_idx][col], matrix[i][col]

        return matrix

    @staticmethod
    def calculate_products_and_sum(matrix):
        n = len(matrix)
        m = len(matrix[0])
        row_products = []

        for i in range(n):
            product = 1
            found_element = False

            for j in range(m - i, m):
                product *= matrix[i][j]
                found_element = True

            if not found_element:
                product = 0  

            row_products.append(product)

        total_sum = sum(row_products) 

        return row_products, total_sum

matrix = [
    [22, 41, 45, -45, -49],
    [5, 1, 3, -2, 0],
    [34, 97, 48, 72, -1],
    [0, -3, -57, 9, 1]
]

sorted_matrix = Matrix.sort_columns(matrix)

row_products, total_sum = Matrix.calculate_products_and_sum(sorted_matrix)

print('\nSorted Matrix:')
for row in sorted_matrix:
    print(row)

print('\nRow products:', row_products)
print('Sum of products:', total_sum)
