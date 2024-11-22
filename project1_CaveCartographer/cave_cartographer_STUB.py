'''
Project 1: Cave Cartographer STUB
'''

# Classes
"""
Cave Class
This contains information about the entirety of the underlying cave.
"""
class Cave :
    def __init__(self, file) :
        self.cave_file = file           # (string) file name containing 
        self.layout = [["S"], ["E"]]    # (2D list of int) default cave
        self.width  = 1                 # (int) default width
        self.height = 2                 # (int) default height
        self.starting_spot = [0, 0]     # (list of int) default starting position

    """
    create_cave
    Creates a cave from the input file. Returns True if successful, returns False otherwise.
    """
    def create_cave(self) :
        pass

    """
    Get information about the cave.
    """
    def get_starting_spot(self) :
        pass
    
    def get_height(self) :
        pass
    
    def get_width(self) :
        pass

    def get_layout(self) :
        pass

    """
    __str__
    Create full map of underlying cave layout and return as a string. 
    """
    def __str__(self) :
        pass

"""
Adventure Class
This contains all of the information about the current state of the adventure.
"""
class Adventure :
    DEFAULT_CAVE_FILE = "default_cave.txt"  # default cave file

    def __init__(self, cave) -> None:
        self.cave = cave                # adventure's cave is cave passed
        self.visited = [[1], [1]]       # at start, only visited square is (0, 0)
        self.current_spot = [0, 0]      # current_spot in default cave begins at (0,0)

    """
    NOTE: self.visited is a 2D list of 0s and 1s. The item self.visited[i][j] corresponds to the space in the cave at coordinates (j, i) (where the y-axis starts from the top instead of the bottom). The value of self.visited[i][j] is 1 if the space at coordinates (j, i) has been visited and 0 if it has not been visited.
    """

    """
    start_adventure
    """
    def start_adventure(self) :
        pass

    """
    Get information about the adventure
    """
    def get_current_map(self) :
        pass
    
    def get_current_spot(self) :
        row, col = self.current_spot
        return self.cave.layout[row][col]

    """
    Update the map of visited spaces.
    """
    def set_visited(self):
    # Loop through the 9 positions (current + 8 neighbors)
        for r in range(self.row - 1, self.row + 2):  # From row-1 to row+1 (inclusive)
            for c in range(self.col - 1, self.col + 2):  # From col-1 to col+1 (inclusive)
                # Check if (r, c) is within bounds
                if 0 <= r < self.cave.height and 0 <= c < self.cave.width:
                    self.visited[r][c] = 1  # Mark as visited
            
    """
    can_move
    Determine if the adventurer can move in given direction.
    TODO: This is one of the methods you are testing in this first assignment.
    """
    def can_move(self, direction) :
        row, col = self.current_spot

        if direction == 'up':
            next_row, next_col = row - 1, col
        elif direction == 'down':
            next_row, next_col = row + 1, col
        elif direction == 'left':
            next_row, next_col = row, col - 1
        elif direction == 'right':
            next_row, next_col = row, col + 1
        else:
            return False
        
        if next_row < 0 or next_row >= self.cave.height or next_col < 0 or next_col >= self.cave.width:
            return False
        if self.cave.layout[next_row][next_col] == 'R':
            return False
        return True
        
    """
    move
    Assuming the given direction is a valid move, move the adventurer in that direction and update the map of visited spaces.
    TODO: This is the other method you are testing.
    """
    def move(self, direction) :
        if direction == 'up':
            self.current_spot[0] -= 1
        elif direction == 'down':
            self.current_spot[0] += 1
        elif direction == 'left':
            self.current_spot[1] -= 1
        elif direction == 'right':
            self.current_spot[1] += 1

        self.set_visited(self.current_spot[0], self.current_spot[1])

    """
    map_complete
    Determine if the cave has been fully explored
    """
    def map_complete(self) :
        pass

# Other functions
def clear_screen() :
    print("\n" * 1000)

def print_banner() :
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~ You are in a cave! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Explore the cave by typing in commands. You can only exit the cave if the entire
cave has been explored. Good luck!
          """)

# ~ MAIN ~ #
if __name__ == "__main__" :
    ## Begin the Adventure
    print_banner()
    input("Press Enter to start.")

    # The game goes here

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")