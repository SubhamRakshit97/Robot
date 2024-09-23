class Robot:
    def __init__(self, grid_rows, grid_cols, start_position=(0, 0), start_direction="S"):
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.position = list(start_position)  # (row, column)
        self.direction = start_direction  # All the direction North, South, East West
        self.directions = ['N', 'E', 'S', 'W']  # Clockwise order for direction

    def move(self):
        """Move robot one step in the direction it's facing."""
        if self.direction == 'N':
            if self.position[0] > 0:
                self.position[0] -= 1
        elif self.direction == 'S':
            if self.position[0] < self.grid_rows - 1:
                self.position[0] += 1
        elif self.direction == 'E':
            if self.position[1] < self.grid_cols - 1:
                self.position[1] += 1
        elif self.direction == 'W':
            if self.position[1] > 0:
                self.position[1] -= 1

    def change_direction(self, new_direction):
        """Change the robot's direction if the new direction is different."""
        if new_direction != self.direction:
            self.direction = new_direction

    def process_command(self, command):
        """Process a series of commands for the robot."""
        for c in command:
            if c == 'M':  # Move in the current direction
                self.move()
            elif c in ['N', 'E', 'S', 'W']:  # Change direction
                self.change_direction(c)

    def get_position(self):
        """Return the robot's current position and direction."""
        return self.position[0], self.position[1], self.direction


if __name__ == "__main__":
    # Create a robot on a 5x4 grid starting at (0, 0) facing South
    robot = Robot(5, 4, start_position=(0, 0), start_direction="S")
    command = input("Enter the command: ")
    robot.process_command(command)
    # Output 
    row, col, direction = robot.get_position()
    print(f"Robot Location: ({row},{col},{direction})")
