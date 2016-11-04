import math
class ShapeError(Exception):
    pass

def shape(vectors):
    if type(vectors[0]) == type([]):
        columns = len(vectors[0])
        row = len(vectors)
        tuple1 = (row, columns)
        return tuple1
    else:
        row = len(vectors)
        return (row,)

def vector_add(vector1, vector2):
    if shape(vector1) == shape(vector2):
        combined_vectors = [item + thing for item, thing in zip(vector1, vector2)]
        return combined_vectors
    else:
        raise ShapeError

def vector_sub(vector1, vector2):
    if shape(vector1) == shape(vector2):
        combined_vectors = [item - thing for item, thing in zip(vector1, vector2)]
        return combined_vectors
    else:
        raise ShapeError

def vector_sum(*many_args):
    list_to_count = [*many_args]
    arg1 = len(list_to_count[0])
    number = len(list_to_count)
    list_of_number = range(number)
    list_of_length = [len(list_to_count[n]) for n in list_of_number]
    list_of_0s = [(l - arg1) for l in list_of_length]
    count_of_0s = sum(list_of_0s)
    if count_of_0s == 0:
        combo_vectors = [sum(item) for item in zip(*many_args)]
        return combo_vectors
    else:
        raise ShapeError

def dot(vector1, vector2):
    if shape(vector1) == shape(vector2):
        multiplied_list = [(item * thing) for item, thing in zip(vector1, vector2)]
        one_number = sum(multiplied_list)
        return one_number
    else:
        raise ShapeError

def vector_multiply(vector1, scalar1):
    multi_vector = [(item * scalar1) for item in vector1]
    return multi_vector

def vector_mean(*many_args):
    count_arguments = len([*many_args])
    top = vector_sum(*many_args)
    mean1 = vector_multiply(top, (1/count_arguments))
    return mean1

def magnitude(vector1):
    squares = [item**2 for item in vector1]
    roots = math.sqrt(sum(squares))
    return roots

def matrix_row(matrix1, index1):
    row_of_matrix = matrix1[index1]
    return row_of_matrix

def matrix_col(matrix2, index2):
    list_of_number_of_rows = range(len(matrix2))
    col_of_matrix = [matrix2[number2][index2] for number2 in list_of_number_of_rows]
    return col_of_matrix

def matrix_add(matrix1, matrix2):
    if shape(matrix1)[0] == shape(matrix2)[0] and shape(matrix1)[1] == shape(matrix2)[1]:
        combo = [vector_add(vec1, vec2) for vec1, vec2 in zip(matrix1, matrix2)]
        return combo
    else:
        raise ShapeError

def matrix_sub(matrix1, matrix2):
    if shape(matrix1)[0] == shape(matrix2)[0] and shape(matrix1)[1] == shape(matrix2)[1]:
        combo = [vector_sub(vec1, vec2) for vec1, vec2 in zip(matrix1, matrix2)]
        return combo
    else:
        raise ShapeError

def matrix_scalar_multiply(matrix1, scalar1):
    msm = [vector_multiply(row, scalar1) for row in matrix1]
    return msm

def matrix_vector_multiply(matrix1, vector1):
    if shape(matrix1)[1] == shape(vector1)[0]:
        combo = [sum([item * thing for item, thing in zip(row, vector1)]) for row in matrix1]
        return combo
    else:
        raise ShapeError

def matrix_matrix_multiply(matrix1, matrix2):
    if shape(matrix1)[1] == shape(matrix2)[0]:
        col_list = range(shape(matrix2)[1])
        combo = [[sum([item * thing[index3] for item, thing in zip(row, matrix2)]) for index3 in col_list] for row in matrix1]
        return combo
    else:
        raise ShapeError
