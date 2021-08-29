import board
import tkinter as tk
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    STATISTIC_MODE = False

    # GAME PARAMETERS:
    root = None
    ALIVE_PROB = 0.25
    IS_GUI = True
    ROWS = 50
    COLUMNS = 50
    TYPE_PROB_LIST = (50, 50, 0.00)
    MOVE = False  # default False
    AGE = False  # default False
    LONELY = False  # default True
    NO_BOUNDARY = True  # default false

    if STATISTIC_MODE:
        IS_GUI = False
        NUM_ITERATIONS = 300
        NUM_PLAYS = 10
        sexual_wins, asexual_wins, extinction = 0, 0, 0
        for i in range(NUM_PLAYS):
            my_board = board.Board(root=root, alive_prob=ALIVE_PROB, gui=IS_GUI, rows=ROWS, cols=COLUMNS,
                                   type_prob_list=TYPE_PROB_LIST,
                                   move=MOVE, age=AGE, lonely=LONELY, no_boundary=NO_BOUNDARY)
            for j in range(NUM_ITERATIONS):
                my_board.update_board()
            sexual, asexual, predator = my_board.get_statistics()
            if sexual > asexual:
                sexual_wins += 1
            elif asexual > sexual:
                asexual_wins += 1
            elif asexual == sexual == 0:
                extinction += 1

        print("Total Sexual Wins: " + str(sexual_wins))
        print("Total Asexual Wins: " + str(asexual_wins))
        print("Extinctions: " + str(extinction))

    else:
        if IS_GUI:  # show board on screen
            root = tk.Tk()
        my_board = board.Board(root=root, alive_prob=ALIVE_PROB, gui=IS_GUI, rows=ROWS, cols=COLUMNS,
                               type_prob_list=TYPE_PROB_LIST,
                               move=MOVE, age=AGE, lonely=LONELY, no_boundary=NO_BOUNDARY)
        i = 0
        sexual_list, asexual_list, predator_list = [], [], []
        while True:
            # if i % 10 == 0:
            print("Iteration " + str(i))
            sexual, asexual, predator = my_board.get_statistics()
            sexual_list.append(sexual)
            asexual_list.append(asexual)
            predator_list.append(predator)
            # time.sleep(0.5)
            my_board.update_board()
            i += 1
            if i % 100 == 0:
                plt.scatter(x=list(range(len(sexual_list))), y=sexual_list, color='black', label='sexual')
                plt.scatter(x=list(range(len(sexual_list))), y=asexual_list, color='blue', label='asexual')
                plt.scatter(x=list(range(len(sexual_list))), y=predator_list, color='red', label='predator')
                plt.xlabel("iteration")
                plt.ylabel("count")
                plt.title("Run: Removed loneliness | Reproduction: 0.25")
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
