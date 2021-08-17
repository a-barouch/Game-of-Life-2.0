
DEAD = 0
ALIVE = 1


class Cell:
    life_status = DEAD

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = "SEXUAL"
        self.new_status = DEAD
        self.is_preyed = False

    def valid_indices(self, i, j, board):
        if i >= 0 and j >= 0:  # non negative index
            if i != self.row or j != self.col:  # not current cell
                if i < board.num_rows and j < board.num_cols:  # not exceeding board boundaries
                    return True
        return False

    def calc_updated_life_stat(self, board):
        self.new_status = self.life_status
        total_alive, total_alive_for_repr = self.count_live_neighbors(board)
        if total_alive > 3 or total_alive < 2:
            self.new_status = DEAD
        if total_alive_for_repr == 3 and self.get_life_status() == 0:
            self.new_status = ALIVE
            self.is_preyed = False
        return self.new_status


    def count_live_neighbors(self, board):
        total_alive,total_alive_for_repr = 0,0
        for i in range(self.row - 1, self.row + 2):
            for j in range(self.col - 1, self.col + 2):
                if self.valid_indices(i, j, board):
                    cur = board.mat[i][j]
                    if cur.type == self.type:
                        total_alive_for_repr += cur.get_life_status()
                    total_alive += cur.get_life_status()
        return total_alive,total_alive_for_repr

    def get_life_status(self):
        return self.life_status

    def set_life_status(self, use_calculated_status, status_to_set=None, board=None):
        if use_calculated_status:
            self.life_status = self.new_status
            if self.life_status==DEAD or self.is_preyed==True:
                self.life_status=DEAD
                row = self.row
                col = self.col
                board.mat[row][col] = Cell(row, col)
                board.mat[row][col].life_status = DEAD
        else:
            self.life_status = status_to_set
