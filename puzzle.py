import math

class puzzle_state:
    def __init__(self, data: list) -> None:
        self.current_state = tuple(data)
        self.n = int(math.sqrt(len(self.current_state))) # n in NxN board
        self.id = "".join([str(x) for x in data])
        self.f=float('inf')
        # generate goal state:
        temp = []
        for i in range(len(self.current_state)):
            temp.append(i + 1)
        temp[-1] = 0
        self.goal_state = tuple(temp)        

        # for path tracking:
        self.parent = None
        self.moveFromParent = None

        
    def isGoal(self) -> bool:
        return self.current_state == self.goal_state
    
    def new_state_with_swaps(self, index_a, index_b):
        temp_lst = list(self.current_state)
        # swapping the values in indices a and b
        temp_lst[index_a], temp_lst[index_b] = temp_lst[index_b], temp_lst[index_a]
        return puzzle_state(temp_lst)

    def get_possible_moves(self) -> list:
        """return list of possible moves as a tuple of new state and move R/L/U/D
        Order by: UP->DOWN->LEFT->RIGHT

        EXAMPLES FOR MOVES:
        
        R - RIGHT:
        1 2 3       1 2 3
        4 0 5   =>  0 4 5
        6 7 8       6 7 8
        
        L - LEFT:
        1 2 3       1 2 3
        4 0 5   =>  4 5 0
        6 7 8       6 7 8

        U - UP:
        1 2 3       1 2 3
        4 0 5   =>  4 7 5
        6 7 8       6 0 8
        
        D - DOWN:
        1 2 3       1 0 3
        4 0 5   =>  4 2 5
        6 7 8       6 7 8
        """

        moves = []
        zero_index = self.current_state.index(0)
        
        if zero_index < len(self.current_state) - self.n:
            # UP
            moves.append((self.new_state_with_swaps(zero_index, zero_index + self.n), 'U'))
        
        if zero_index >= self.n:
            # DOWN
            moves.append((self.new_state_with_swaps(zero_index, zero_index - self.n), 'D'))

        if zero_index % self.n != self.n - 1:
            # LEFT
            moves.append((self.new_state_with_swaps(zero_index, zero_index + 1),'L'))

        if zero_index % self.n != 0:
            # RIGHT
            moves.append((self.new_state_with_swaps(zero_index, zero_index - 1),'R'))

        return moves

    def toString(self) -> str:
        i = 0
        s = ''
        for _ in range(self.n):
            for _ in range(self.n):
                s += str(self.current_state[i]) + ' '
                i += 1
            s += '\n'
        return s

    def __lt__(self, other):
        return self.f < other.f