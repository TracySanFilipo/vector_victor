import math
class ShapeError(Exception):
    pass

def shape(vectors):
    #columns = [len(col) for col in vectors if type(vectors[0]) == type([])]
    row = len(vectors)
    tuple1 = (row,)
    return tuple1

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
    if len(many_args) == len(many_args):
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
