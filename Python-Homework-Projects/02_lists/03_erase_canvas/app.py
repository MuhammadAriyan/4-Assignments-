# Canvas eraser
"""Using Tkinter instead of graphics.py because it's built-in,
well-documented, and doesn't require external installation."""
import tkinter as tk

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
CELL_SIZE = 25
ERASER_SIZE = 10

def erase_objects(event):
    """Erase objects in contact with the eraser"""
    x, y = event.x, event.y  # Get the mouse coordinates

    # Find all overlapping objects at the eraser position
    overlapping_objects = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)

    # Change the color of overlapping objects to white (erase effect)
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

    # Check if all cells are erased
    check_all_erased()

def move_eraser(event):
    """Move eraser to follow the mouse"""
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(event)

def create_grid():
    """Creates the grid of blue cells"""
    global cells
    canvas.delete("all")  # Clear canvas before refilling
    cells.clear()  # Clear list to track cells

    # Recreate the eraser after clearing everything
    global eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink", outline="black")

    # Create the grid
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            cell = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
            cells.append(cell)  # Store cell reference

def check_all_erased():
    """Check if all cells are erased (turned white)"""
    all_erased = all(canvas.itemcget(cell, "fill") == "white" for cell in cells)
    if all_erased:
        canvas.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, text="Press 'R' to Refill", font=("Arial", 16, "bold"), fill="black", tags="refill_text")

def refill_grid(event):
    """Refill the grid when 'R' is pressed"""
    canvas.delete("refill_text")  # Remove refill message
    create_grid()  # Recreate the grid

def main():
    global canvas, eraser, cells
    cells = []  # Track all cells

    # Create main window
    root = tk.Tk()
    root.title("Eraser Game")

    # Create canvas
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    create_grid()  # Create initial grid

    # Bind mouse movement to eraser movement
    canvas.bind("<Motion>", move_eraser)

    # Bind "R" key to refill the grid
    root.bind("r", refill_grid)

    # Run the application
    root.mainloop()

if __name__ == '__main__':
    main()
