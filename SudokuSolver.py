import numpy as np

matrix = np.array([[5,3,0, 0,7,0, 0,0,0],
                   [6,0,0, 1,9,5, 0,0,0],
                   [0,9,8, 0,0,0, 0,6,0],

                   [8,0,0, 0,6,0, 0,0,3],
                   [4,0,0, 8,0,3, 0,0,1],
                   [7,0,0, 0,2,0, 0,0,6],

                   [0,6,0, 0,0,0, 2,8,0],
                   [0,0,0, 4,1,9, 0,0,5],
                   [0,0,0, 0,8,0, 0,7,9]])


def row_column_contains_number(ix, iy, num):
    return (num in matrix[ix]) or (num in matrix[:, iy])


isChanged = True
position = None

while(isChanged == True):
    isChanged = False

    for mx in range(0, 3):
        for my in range(0, 3):
            s = matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

            for x in range(1, 10):
                if not x in s:
                    position = None

                    for xs, ys in np.ndindex(s.shape):
                        ix = mx * 3 + xs
                        iy = my * 3 + ys

                        if((matrix[ix, iy] == 0) and not row_column_contains_number(ix, iy, x)):
                            if not position:
                                position = (ix, iy)
                            else:
                                position = None
                                break

                    if position:
                        matrix[position[0], position[1]] = x
                        print(x)
                        print(position)
                        print(matrix)
                        isChanged = True
