from guizero import App, Window, Box, Text, PushButton
import numpy as np

initial_matrix = np.array([
                   [5,3,0, 0,7,0, 0,0,0],
                   [6,0,0, 1,9,5, 0,0,0],
                   [0,9,8, 0,0,0, 0,6,0],

                   [8,0,0, 0,6,0, 0,0,3],
                   [4,0,0, 8,0,3, 0,0,1],
                   [7,0,0, 0,2,0, 0,0,6],

                   [0,6,0, 0,0,0, 2,8,0],
                   [0,0,0, 4,1,9, 0,0,5],
                   [0,0,0, 0,8,0, 0,7,9]])

current_matrix = np.array(initial_matrix, copy=True)
boxes = []
buttons = [[None for y in range(9)] for x in range(9)]

app = App(title="Sudoky solver", layout="grid", height=500, width = 600)

for mx in range(0, 3):
    for my in range(0, 3):
        boxes.append(Box(app, align="top", width="fill", border=True, grid=[my,mx], layout="grid"))

empty_box = Box(app, align="right", width="fill", border=False, grid=[3, 0])
button_box = Box(app, align="right", width="fill",
                 border=False, grid=[4, 0], layout="grid")

def row_column_contains_number(ix, iy, num):
    return (num in current_matrix[ix]) or (num in current_matrix[:, iy])

def show_current_matrix():
    for mx in range(0, 3):
        for my in range(0, 3):
            s = current_matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

            for xs, ys in np.ndindex(s.shape):
                ix = mx * 3 + xs
                iy = my * 3 + ys

                buttons[ix][iy].text = str(
                    current_matrix[ix, iy] if current_matrix[ix, iy] > 0 else " ")

def reset_sudoku():
    global current_matrix
    current_matrix = np.array(initial_matrix, copy=True)
    show_current_matrix()

def solve_sudoku(post_results=True):
    isChanged = True
    position = None

    if(post_results == True):
        show_current_matrix()

    while(isChanged == True):
        isChanged = False

        for mx in range(0, 3):
            for my in range(0, 3):
                s = current_matrix[(mx * 3):(mx * 3) + 3,
                                   (my * 3):(my * 3) + 3]

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


def btn_function(ix, iy):
    solve_sudoku(False)
    buttons[ix][iy].text = str(
        current_matrix[ix, iy] if current_matrix[ix, iy] > 0 else " ")


ibox = 0
for mx in range(0, 3):
    for my in range(0, 3):
        s = current_matrix[(mx * 3):(mx * 3) + 3, (my * 3):(my * 3) + 3]

        for xs, ys in np.ndindex(s.shape):
            ix = mx * 3 + xs
            iy = my * 3 + ys
            buttons[ix][iy] = PushButton(boxes[ibox], text=str(current_matrix[ix, iy] if current_matrix[ix, iy] > 0 else " "),
                align="left", grid=[ys, xs], width=3, command=btn_function, args=[ix, iy])
            buttons[ix][iy].text_size = 11

        ibox = ibox + 1

Text(empty_box, text=" " * 3)
solve_button = PushButton(button_box, text="solve", align="right", command=solve_sudoku, grid=[0, 0], width=8)
solve_button = PushButton(button_box, text="reset", align="right", command=reset_sudoku, grid=[0, 1], width=8)

app.display()
