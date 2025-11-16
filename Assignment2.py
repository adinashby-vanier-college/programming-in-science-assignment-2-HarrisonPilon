# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    max1 = numbers[0]

    for n in numbers:
        if n > max1:
            max1 = n

    max2 = None
    for n in numbers:
        if n != max1:
            max2 = n
            break

    for n in numbers:
        if n != max1 and n > max2:
            max2 = n

    return max1, max2

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    unique = []

    for n in numbers:
        if n not in unique:
            unique.append(n)

    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if unique[j] < unique[i]:
                unique[i], unique[j] = unique[j], unique[i]

    return unique

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0

    for n in arr:
        total += n
        result.append(total)

    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    
    for c in range(cols):
        result.append([])
        for r in range(rows):
            result[c].append(matrix[r][c])

    return result

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    result = []

    for i in range(0, len(lst), step):
        result.append(lst[i])

    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    result = 0

    for i in range(len(list1)):
        result += list1[i] * list2[i]

    return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    cols2 = len(matrix2[0])

    result = []

    for i in range(rows1):
        result.append([0] * cols2)

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
