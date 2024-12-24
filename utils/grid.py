"""
grid.py

This module generates multiple random setups for a 5x5 grid for a game. Each grid setup includes:
- 8 or 9 red squares
- 8 or 9 blue squares
- 1 black square
- 7 white squares

The program ensures that the total number of squares is exactly 25 and randomizes their positions
in the grid. It then prints multiple random setups of the grid.

Functions:
- generate_grid(): Generates a random 5x5 grid with the specified conditions.
- print_grid(grid): Prints the 5x5 grid in a readable format.
"""

import random

def generate_grid():
    """
    Generates a random 5x5 grid with the specified number of red, blue, black, and white squares.

    Returns:
        list: A 5x5 grid represented as a list of lists.
    """
    # Randomly choose between 9 red and 8 blue, or 8 red and 9 blue
    if random.choice([True, False]):
        red_squares = 9
        blue_squares = 8
    else:
        red_squares = 8
        blue_squares = 9
        
    black_squares = 1
    white_squares = 7

    # Create a list with the required number of each type of square
    squares = ['R'] * red_squares + ['B'] * blue_squares + ['K'] * black_squares + ['W'] * white_squares

    # Ensure the list has exactly 25 elements
    assert len(squares) == 25, "The total number of squares must be 25."

    # Shuffle the list to randomize the positions
    random.shuffle(squares)

    # Reshape the list into a 5x5 grid
    grid = [squares[i:i+5] for i in range(0, 25, 5)]

    return grid

def print_grid(grid):
    """
    Prints the 5x5 grid in a readable format.

    Args:
        grid (list): A 5x5 grid represented as a list of lists.
    """
    for row in grid:
        print(' '.join(row))

# Generate and print multiple random setups
if __name__ == "__main__":
    for _ in range(5):  # Generate 5 random setups
        grid = generate_grid()
        print_grid(grid)
        print()  # Print a blank line between grids