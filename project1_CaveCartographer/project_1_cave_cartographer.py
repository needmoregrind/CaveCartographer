'''
Project 1: Cave Cartographer

Legend for the Text file: 
-----------------------------------------------------------------------------------------------
Symbol    Meaning     Can you walk through it?     Console
-----------------------------------------------------------------------------------------------
R         Rock        No                           N/A                                           
_         Empty       Yes                          None                                          
S         Start       Yes                          "Entrance to the cave."                          
E         E           Yes                          End the game if the cave has been explored.
-----------------------------------------------------------------------------------------------

What you have to do:
    Any comment of the form 
    TODO: Here is a task for you to do 
    indicates that there is something you have to do there. Use Ctrl/Cmd+F to find all the tasks you have to do.
'''

# Classes
class Cave :
    """
    Cave Class
    This contains information about the entirety of the cave. Needs to be passed a text file.
    """
    def __init__(self, file) :
        self.cave_file = file           # (string) file name containing 
        self.layout = [["S"], ["E"]]    # (2D list of int) default cave
        self.width  = 1                 # (int) default width
        self.height = 2                 # (int) default height
        self.starting_spot = [0, 0]     # (list of int) default starting position

    def create_cave(self) :
        """
        Creates a cave from the input text file. 
        """

        # TODO: Open cave file
        with open(self.cave_file, 'r') as file:

        # TODO: Read the cave file into a variable
            text = file.readlines()

        # TODO: Close Cave file
        # file.close()

        # TODO: Create the 2D list representing the cave 
        new_List = []
        for line in text:
            new_char = line.strip().split()
            new_List.append(new_char)
        self.layout =  new_List
        self.width = len(new_List[0])
        self.height = len(new_List)
        print(self.layout)

        # TODO: Check the following things about the provided cave file:
        # 1. The cave is a rectangle.
        width = len(new_List[0])
        for row in new_List:
            if len(row) != width:
                raise Exception('The cave is not a rectangle!')
            
        # 2. There is exactly one "S". (Hint: Assign the starting spot along the way!)
        # 3. There is exactly one "E".

        start_count = 0
        exit_count = 0
        for i, row in enumerate(new_List):
            for j, cell in enumerate(row):
                if cell == 'S':
                    start_count += 1
                    self.starting_spot =[i,j]
                elif cell == 'E':
                    exit_count += 1 
        if start_count != 1:
            raise Exception(f'Invalid number of starting points (S): {start_count}. There should be exactly one!')
        elif exit_count != 1:
            raise Exception(f'Invalid number of exit points (E): {exit_count}. There should be exactly one!')
        
        # 4. Check that the cave is surrounded by R.
        if any(cell != 'R' for cell in new_List[0]) or any(cell != 'R' for cell in new_List[-1]):
            raise Exception("The cave is not surrounded by 'R' at the top or bottom!")
        for row in new_List:
            if row[0] != 'R' or row[-1] != 'R':
                raise Exception("The cave is not surrounded by 'R' on the left or right side!")
        # Raise a generic Exception with a custom message if any of the checks fail. 
        print('Cave successfully created!')

    def get_starting_spot(self) :
        """Returns starting spot in cave."""
        return self.starting_spot

    def get_height(self) :
        """Returns height of underlying cave layout."""
        return self.height
    
    def get_width(self) :
        """Returns width of underlying cave layout."""
        return self.width

    def get_layout(self) :
        """Returns underlying cave layout."""
        return self.layout

    def __str__(self) :
        """
        Create full map of underlying cave layout and return as a string. 
        """
        return ""

class Adventure :
    """
    Adventure Class
    This contains all of the information about the current state of the adventure. Needs to be passed a Cave object. Has a DEFAULT_CAVE constant pointing to a default cave file.
    """

    DEFAULT_CAVE = "default_cave.txt"

    def __init__(self, cave:Cave) -> None:
        self.cave = cave                # adventure's cave is cave passed
        self.visited = [[1], [1]]       # at start, only visited square is (1,1) by default (changed in start_adventure())
        self.current_spot = [0, 0]      # current_spot in default cave begins at (0,0) by default (changed in start_adventure)

    def start_adventure(self) :
        """
        Creates the adventure out of the cave passed to it in the init method.
        1. TODO It creates the adventure's cave object. If it encounters an Exception, it proceeds to start the adventure with the default cave (make sure you have a valid default_cave.txt in the folder).
        2. TODO It retrieves the starting coordinates for the given cave object.
        3. It initializes the visited portion of the cave by illuminating the immediate surroundings of starting spot.
        """
        pass
        # Create Cave
        ## TODO: Run create_cave() on the passed cave.
        cave = Cave(self.cave)
        ### Catches exceptions using a try-except statement. In the case of an exception, creates the adventure from a valid default cave. (Not part of Part 2.)
        try:
            self.cave.create_cave()
        except Exception as e:
            print (e)
        ## TODO: Set current_spot to the starting coordinates from the cave object.
            self.cave = Cave(self.DEFAULT_CAVE)
            self.cave.create_cave()

        self.current_spot = self.cave.get_starting_spot()
        if self.current_spot is None:
            raise Exception('Starting spot could not be determined from the cave layout!')

        # Initialize Visited (not part of Part 2)
        self.visited = [[0 for _ in range(self.cave.get_width())] for _ in range(self.cave.get_height())]
        
        ## Use the set_visited method to set the visited area after indicating a starting position. (Not part of Part 2.)
        self.set_visited(self.current_spot[0], self.current_spot[1])

    def get_current_map(self) :
        """
        Returns a map of the portion of the cave that has been visited so far.
        (Not part of Part 2.)
        """
        map_string = ""

        for r in range(self.cave.height):
            row_string = []
            for c in range(self.cave.width):
                if self.visited[r][c] == 1:
                    if [r,c] == self.current_spot:
                        row_string.append('<')
                    else:
                    # If visited, use the character from the cave layout
                        row_string.append(self.cave.layout[r][c])
                else:
                    # If not visited, use '?'
                    row_string.append("?")
            
            # Join the row and add it to the map string
            map_string += " ".join(row_string) + "\n"

        return map_string.strip()  # Remove trailing newline

    def get_current_spot(self) :
        """
        Returns the coordinates of the current spot the cartographer is inhabiting.
        (Not part of Part 2.)
        """
        row, col = self.current_spot
        return self.cave.layout[row][col]
    
    def set_visited(self, row, col) :
        """
        Updates the area that the cartographer has visited using the current spot.
        (Not part of Part 2.)
        """
           # Loop through the 9 positions (current + 8 neighbors)
        for r in range(row - 1, row + 2):  # From row-1 to row+1 (inclusive)
            for c in range(col - 1, col + 2):  # From col-1 to col+1 (inclusive)
                # Check if (r, c) is within bounds
                if 0 <= r < self.cave.get_height() and 0 <= c < self.cave.get_width():
                    self.visited[r][c] = 1  # Mark as visited

    def can_move(self, direction) :
        """
        Returns True if cartographer can move in given direction and False otherwise.
        (Not part of Part 2.)
        """
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
    
    def move(self, direction) :
        """
        Moves cartographer in given direction and updates the area visited.
        (Not part of Part 2.)
        """
        if direction == 'up':
            self.current_spot[0] -= 1
        elif direction == 'down':
            self.current_spot[0] += 1
        elif direction == 'left':
            self.current_spot[1] -= 1
        elif direction == 'right':
            self.current_spot[1] += 1

        self.set_visited(self.current_spot[0], self.current_spot[1]) 

    def map_complete(self) :
        """
        Returns True if the map has been completely explored.
        (Not part of Part 2.)
        """
        for row in self.visited:
            if not all(value == 1 for value in row):
                return False
        return True

# Other functions
def clear_screen():
    """Clears the text in the console."""
    print("\n" * 1000)

def print_banner():
    """Prints the welcome banner for the adventure."""

    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~ You are in a cave! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Explore the cave by typing in commands. You can only exit the cave if the entire
cave has been explored. Good luck!
          """)

# ~ MAIN ~ #
if __name__ == "__main__" :
    # Let's Go 
    ## Begin the Adventure
    print_banner()
    input("Press Enter to start.")

    ## TODO: Create the Cave
    # input("Press Enter to start your cave exploration adventure!")
    cave_file = input("Enter the name of the cave file you'd like to explore:")
    if not cave_file:
        cave_file = Adventure.DEFAULT_CAVE
    try:
        cave = Cave(cave_file)
        cave.create_cave()
        print("Cave loaded successfully! Let the adventure begin.")

    ## TODO: Create the Adventure object and initialize it
        adventure = Adventure(cave)
        adventure.start_adventure()

    except FileNotFoundError:
        print(f"Error: The file '{cave_file}' does not exist. Please make sure the file name is correct.")
        try:
            cave = Cave(Adventure.DEFAULT_CAVE)
            cave.create_cave()
            adventure = Adventure(cave)
            adventure.start_adventure()  # Initialize the adventure with the default cave
            print("Loaded the default cave instead.")
        except FileNotFoundError:
            print(f"Error: The default cave file '{Adventure.DEFAULT_CAVE}' also does not exist. Exiting the game.")
            exit(1)

    ## GAME LOOP ##
    # (Not part of Part 2)
    while True:
        clear_screen()
        print_banner()
        print(adventure.get_current_map())

        direction = []
        if adventure.can_move('up'):
            direction.append('up') 
        if adventure.can_move('down'):
            direction.append('down')
        if adventure.can_move('right'):
            direction.append('right')
        if adventure.can_move('left'):
            direction.append('left')

        print(f"You can move in the following directions: {', '.join(direction)}")
        user_input = input("Enter a direction (up, down, left, right) or type 'quit' to leave the adventure: ").strip().lower()

        if user_input == 'quit':
            print("Exiting the game... Thanks for playing!")
            break

        if user_input in direction:
            adventure.move(user_input)
            # print(f'Moved {user_input}.')
        else: 
            print('Invalid direction! Please try again.')
            continue
        
        if adventure.get_current_spot() == 'E' and adventure.map_complete():
            print('Congraulation! You have successfully explored the entire cave and reached the exit.')
            break
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
