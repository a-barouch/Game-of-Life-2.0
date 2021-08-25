from cell import Cell
import random

DEAD = 0
ALIVE = 1


def flip_coin(rate):
    return 1 if random.random() < rate else 0


class Asex(Cell):

    def __init__(self, row, col):
        Cell.__init__(self, row, col)
        self.type = "ASEXUAL"
        self.reproduction_prob = 0.4
        self.is_preyed = False
        self.lonely = False

    def calc_updated_life_stat(self, board):
        self.new_status = self.life_status

        # count alive neighbors of all types
        total_alive, _ = self.count_live_neighbors(board)

        # death caused by overpopulation
        if total_alive > 3:
            self.new_status = DEAD
        if total_alive < 2 and self.lonely:
            self.new_status = DEAD
        # asexual reproduction if the cell is alive and by probability
        if self.get_life_status() == ALIVE and flip_coin(self.reproduction_prob):
            self.asexual_reproduction(board)
        return self.new_status

    def asexual_reproduction(self, board):
        dead_neighbors = []

        # find available cells to reproduction
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.col - 1, self.col + 2):
                if self.valid_indices(i, j, board):
                    cur_neighbor = board.mat[i][j]
                    if cur_neighbor.get_life_status() == DEAD:
                        dead_neighbors.append(cur_neighbor)

        # no available cells were found
        if len(dead_neighbors) == 0:
            return

        # create a child cell in the available cell
        child = random.choice(dead_neighbors)
        row = child.row
        col = child.col
        board.mat[row][col] = Asex(row, col)
        board.mat[row][col].new_status = ALIVE
        board.mat[row][col].is_preyed = False
        # print("Parent row: "+str(self.row)+" Parent col: "+str(self.col))
        # print("Child row: "+str(row)+" Child col: "+str(col)+"\n")
