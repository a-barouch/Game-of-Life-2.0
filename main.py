import board
import tkinter as tk
import time

if __name__ == '__main__':
    IS_GUI = True
    root = None
    if IS_GUI:
        root = tk.Tk()
    my_board = board.Board(root=root, alive_prob=0.5, gui=IS_GUI, rows=50, cols=50,type_prob_list=(0,0.9,0.1))
    i = 0
    while True:
        if i%10 ==0:
            print("Iteration "+str(i))
            my_board.get_statistics()
        time.sleep(0.5)
        my_board.update_board()
        i += 1
    my_board.root.mainloop()

    # for row in self.mat:
    #     for col in row:
    #         print("{:8.0f}".format(col.life_status), end=" ")
    #     print("")
    # self.mat[1][0].set_life_status(1, False)
    # self.mat[1][1].set_life_status(1, False)
    # self.mat[1][2].set_life_status(1, False)
