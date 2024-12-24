"""
main.py

This script uses the grid module to generate and print a specified number of random 5x5 grids.
"""

from utils.grid import generate_grid, print_grid

def main():
    """
    Main function to generate and print random grids.
    """
    num_grids = int(input("Enter the number of grids to generate: "))
    
    for _ in range(num_grids):
        grid = generate_grid()
        print_grid(grid)
        print()  # Print a blank line between grids

if __name__ == "__main__":
    main()