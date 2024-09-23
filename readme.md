# Robot Movement Program

## Description

This program simulates the movement of a robot on a 5x4 grid. The robot takes directional (N, E, S, W) and movement (M) commands and updates its position accordingly. The robot starts at (0, 0, S), meaning row 0, column 0, facing South.

## How to Run

1. Ensure Python is installed on your machine.
2. Save the `robot_movement.py` file to your local machine.
3. Run the program using the terminal/command line:
   
## Run the command: 
```python robot_movement.py ```

4. Input a sequence of commands when prompted (e.g., `MSMMEMM`).
5. The final position of the robot will be printed to the terminal.

## Example 1
Enter the command: MSMMEMM
Robot Location: (3,2,E)

## Example 2
Enter the command: MMEMWMEM
Robot Location: (2,1,E)


## Rules:
- The robot can move within the bounds of the 5x4 grid.
- The robot ignores redundant direction changes (e.g., if it's already facing North and receives another 'N' instruction).
- If the robot tries to move out of the grid, it stays in place.
