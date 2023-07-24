#!/usr/bin/python3

"""This project output the way the pascal trangle is displayed """


def pascal_triangle(n):
    """ This function returns a list of lists of integers representing the 
        Pascal’s triangle of n.
    """
    pattern = []

    for i in range(n):
        tmp = []

        for j in range(i + 1):
            if j == 0 or i == 1:
                tmp.append(1)

            else:
                tmp.append(pattern[i - l][j - l] + pattern[i - 1][j])
        pattern.append(tmp)
       
        return pascal_triangle


