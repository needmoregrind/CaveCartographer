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
        pass

    def get_height(self) :
        """Returns height of underlying cave layout."""
        pass
    
    def get_width(self) :
        """Returns width of underlying cave layout."""
        pass

    def get_layout(self) :
        """Returns underlying cave layout."""
        pass

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
            cave.create_cave()
        except Exception as e:
            print (e)
        ## TODO: Set current_spot to the starting coordinates from the cave object.
       
        
        self.current_spot = cave.get_starting_spot()

        # Initialize Visited (not part of Part 2)
        
        ## Use the set_visited method to set the visited area after indicating a starting position. (Not part of Part 2.)

    def get_current_map(self) :
        """
        Returns a map of the portion of the cave that has been visited so far.
        (Not part of Part 2.)
        """
        pass

    def get_current_spot(self) :
        """
        Returns the coordinates of the current spot the cartographer is inhabiting.
        (Not part of Part 2.)
        """
        pass
    
    def set_visited(self) :
        """
        Updates the area that the cartographer has visited using the current spot.
        (Not part of Part 2.)
        """
        pass

    def can_move(self, direction) :
        """
        Returns True if cartographer can move in given direction and False otherwise.
        (Not part of Part 2.)
        """
        pass    
    
    def move(self, direction) :
        """
        Moves cartographer in given direction and updates the area visited.
        (Not part of Part 2.)
        """
        pass 

    def map_complete(self) :
        """
        Returns True if the map has been completely explored.
        (Not part of Part 2.)
        """

# Other functions
def clear_screen() :
    """Clears the text in the console."""
    print("\n" * 1000)

def print_banner() :
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

    ## TODO: Create the Adventure object and initialize it
    
    ## GAME LOOP ##
    # (Not part of Part 2)
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
