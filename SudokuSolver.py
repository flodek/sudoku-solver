from guizero import App, Window, Box, Text, PushButton
import numpy as np

initial_matrix = np.array([
                   [0,1,2, 8,6,0, 9,0,0],
                   [0,0,9, 0,0,0, 0,0,2],
                   [0,6,0, 0,0,2, 0,0,0],

                   [0,0,0, 9,0,0, 1,0,0],
                   [8,3,0, 0,0,0, 0,9,6],
                   [0,0,4, 0,0,3, 0,0,0],

                   [0,0,0, 1,0,0, 0,5,0],
                   [4,0,0, 0,0,0, 7,0,0],
                   [0,0,1, 0,2,7, 6,3,0]])

current_matrix = np.array(initial_matrix, copy=True)

app = App(title="Sudoky solver", layout="grid", height=500, width = 600)

b1 = Box(app, align="top", width="fill", border=True, grid=[0,0], layout="grid")
b2 = Box(app, align="top", width="fill", border=True, grid=[1,0], layout="grid")
b3 = Box(app, align="top", width="fill", border=True, grid=[2,0], layout="grid")
b4 = Box(app, align="top", width="fill", border=True, grid=[0,1], layout="grid")
b5 = Box(app, align="top", width="fill", border=True, grid=[1,1], layout="grid")
b6 = Box(app, align="top", width="fill", border=True, grid=[2,1], layout="grid")
b7 = Box(app, align="top", width="fill", border=True, grid=[0,2], layout="grid")
b8 = Box(app, align="top", width="fill", border=True, grid=[1,2], layout="grid")
b9 = Box(app, align="top", width="fill", border=True, grid=[2,2], layout="grid")
empty_box = Box(app, align="right", width="fill", border=False, grid=[3,0])
button_box = Box(app, align="right", width="fill", border=False, grid=[4,0], layout="grid")

boxes = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
buttons = [ [ None for y in range( 9 ) ] for x in range( 9 ) ]

def row_column_contains_number(ix, iy, num):
    return (num in current_matrix[ix]) or (num in current_matrix[:, iy])

def reset_sudoku():
    global current_matrix
    current_matrix = np.array(initial_matrix, copy=True)

    for mx in range(0, 3):
        for my in range(0, 3):
            s = current_matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

            for xs, ys in np.ndindex(s.shape):
                ix = mx * 3 + xs
                iy = my * 3 + ys

                buttons[ix][iy].text = str(current_matrix[ix,iy] if current_matrix[ix,iy] > 0 else " ")

def solve_sudoku(post_results=True):
    isChanged = True
    position = None
    while(isChanged == True):
        isChanged = False

        for mx in range(0, 3):
            for my in range(0, 3):
                s = current_matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

                for x in range(1, 10):
                    if not x in s:
                        position = None

                        for xs, ys in np.ndindex(s.shape):
                            ix = mx * 3 + xs
                            iy = my * 3 + ys

                            if((current_matrix[ix, iy] == 0) and not row_column_contains_number(ix, iy, x)):
                                if not position:
                                    position = (ix, iy)
                                else:
                                    position = None
                                    break

                        if position:
                            current_matrix[position[0], position[1]] = x
                            if(post_results == True):
                                buttons[position[0]][position[1]].text = x
                            print(x)
                            print(position)
                            print(current_matrix)
                            isChanged = True

def btn_function(ix,iy):
    solve_sudoku(False)
    buttons[ix][iy].text = str(current_matrix[ix,iy] if current_matrix[ix,iy] > 0 else " ")

ibox = 0
for mx in range(0, 3):
    for my in range(0, 3):
        s = current_matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

        for xs, ys in np.ndindex(s.shape):
            ix = mx * 3 + xs
            iy = my * 3 + ys
            buttons[ix][iy] = PushButton(boxes[ibox], text=str(current_matrix[ix,iy] if current_matrix[ix,iy] > 0 else " "), align="left", grid=[ys,xs], width=3, command=btn_function, args=[ix,iy])
            buttons[ix][iy].text_size = 11

        ibox = ibox + 1

Text(empty_box, text=" " * 3)
solve_button = PushButton(button_box, text="solve", align="right", command=solve_sudoku, grid=[0,0], width=8)
solve_button = PushButton(button_box, text="reset", align="right", command=reset_sudoku, grid=[0,1], width=8)

app.display()
