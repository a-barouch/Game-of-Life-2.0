import board
import tkinter as tk
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    IS_GUI = True
    root = None
    if IS_GUI:  # show board on screen
        root = tk.Tk()
    my_board = board.Board(root=root, alive_prob=0.5, gui=IS_GUI, rows=50, cols=50, type_prob_list=(1, 0, 0),
                           move=False, age=False, lonely = True)
    i = 0
    sexual_list, asexual_list, predator_list = [], [], []
    while True:
        # if i % 10 == 0:
        print("Iteration " + str(i))
        sexual, asexual, predator = my_board.get_statistics()
        sexual_list.append(sexual)
        asexual_list.append(asexual)
        predator_list.append(predator)
        #time.sleep(0.5)
        my_board.update_board()
        i += 1
        if i % 100 == 0:
            plt.scatter(x=list(range(len(sexual_list))), y=sexual_list, color='black', label='sexual')
            plt.scatter(x=list(range(len(sexual_list))), y=asexual_list, color='blue', label='asexual')
            plt.scatter(x=list(range(len(sexual_list))), y=predator_list, color='red', label='predator')
            plt.xlabel("iteration")
            plt.ylabel("count")
            plt.legend()
            plt.show()

    my_board.root.mainloop()

    # for row in self.mat:
    #     for col in row:
    #         print("{:8.0f}".format(col.life_status), end=" ")
    #     print("")
    # self.mat[1][0].set_life_status(1, False)
    # self.mat[1][1].set_life_status(1, False)
    # self.mat[1][2].set_life_status(1, False)
