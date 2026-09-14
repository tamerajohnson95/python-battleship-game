import random

print("Welcome to Mini Battleship!") 
print()
    
# Difficulty level

print("Choose a difficulty level:") 
print("1 = Easy") 
print("2 = Medium") 
print("3 = Hard") 
difficulty = int(input("Enter 1, 2, or 3: "))

# Set grid size and attempts

if difficulty == 1: 
    grid_size = 4 
    attempts = 7 
elif difficulty == 2: 
    grid_size = 5 
    attempts = 5 
else: 
    grid_size = 6 
    attempts = 4 
    print() 
    print("Grid size:", grid_size, "x", grid_size) 
    print("Attempts:", attempts) 
 
# Randomly choose ship direction

# 1 = horizontal 
# 2 = vertical

direction = random.randint(1, 2) 
 
# Place ship

if direction == 1: 
    # Horizontal ship
    
    row1 = random.randint(1, grid_size) 
    col1 = random.randint(1, grid_size - 1) 
 
    row2 = row1 
    col2 = col1 + 1 
 
else: 
    # Vertical ship
    
    row1 = random.randint(1, grid_size - 1) 
    col1 = random.randint(1, grid_size) 
 
    row2 = row1 + 1 
    col2 = col1 
 
# Keep track of hits

hit1 = False 
hit2 = False 
 
# Start game

while attempts > 0 and not (hit1 and hit2): 
 
    print() 
    print("Attempts left:", attempts) 
 
    guess_row = int(input("Enter row: ")) 
    guess_col = int(input("Enter column: ")) 
 
    # Check if guess is outside the grid
    
    if guess_row < 1 or guess_row > grid_size or guess_col < 1 or guess_col > grid_size: 
        print("Invalid guess.") 
        print("Enter numbers from 1 to", grid_size) 
 
    else: 
 
        # Check first part of ship
        
        if guess_row == row1 and guess_col == col1: 
            print("HIT!") 
            hit1 = True 
 
        # Check second part of ship
        
        elif guess_row == row2 and guess_col == col2: 
            print("HIT!") 
            hit2 = True 
 
        else: 
            print("MISS!") 
 
        attempts = attempts - 1 
 
# Game over

print() 
print("GAME OVER") 
if hit1 and hit2: 
    print("You sank the ship!") 
    print("You win!") 
else: 
    print("You did not sink the ship.") 
    print("The computer wins.")
    
# Reveal ship

print() 
print("The ship was located at:") 
print("Row", row1, "Column", col1) 
print("Row", row2, "Column", col2) 
print() 
print("Thanks for playing Mini Battleship!")
