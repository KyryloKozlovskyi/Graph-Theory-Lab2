import numpy as np

# Create two graphs G2 = (V2,E2) and G1 = (V1,E1)
V1 = ("a","b","c","d")
V2 = ("a","b","c","d","e","f")
E1 = ({"a","b"},{"c","d"},{"d","a"})
E2 = ({"a","b"},{"c","d"},{"a","d"},{"a","e"})

# Exercise 1
# Create a function which outputs the Adjacency Matrix of a Graph. The output should be
# a numpy matrix (so at the start use import numpy as np).
def outputAdjacencyMatrix(V, E):
    # Create an empty matrix
    m = np.zeros((len(V), len(V)))
    # Fill the matrix with 1s where there is an edge
    for e in E:
        # Find the index of the vertices in the edge
        i = V.index(list(e)[0])
        j = V.index(list(e)[1])
        # Fill the matrix with 1s
        m[i][j] = 1
        m[j][i] = 1
    # Return the matrix
    return np.matrix(m)

# Test the function outputAdjacencyMatrix
print(outputAdjacencyMatrix(V1, E1))