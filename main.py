import random
from tkinter import *
from tkinter import messagebox

class Cell:
    def __init__(self):
        self.has_mine = False
        self.revealed = False
        self.flagged = False
        self.adjacent_mines = 0

class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.first_click = True
        self.game_over = False

        # Set up Tkinter window
        self.root = Tk()
        self.root.title("Minesweeper")

        # Title label
        title_label = Label(self.root, text="Minesweeper", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=self.cols + 1)

        # Column numbers
        for c in range(self.cols):
            label = Label(self.root, text=str(c + 1))
            label.grid(row=1, column=c + 1)

        # Row numbers
        for r in range(self.rows):
            label = Label(self.root, text=str(r + 1))
            label.grid(row=r + 2, column=0)

        # Create grid of buttons with initial gray background
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                button = Button(self.root, width=3, height=1, font=("Arial", 12), bg='gray')
                button.grid(row=r + 2, column=c + 1)
                button.bind("<Button-1>", lambda event, r=r, c=c: self.reveal_cell(r, c))
                button.bind("<Button-3>", lambda event, r=r, c=c: self.toggle_flag(r, c))
                self.buttons[r][c] = button

        # Remaining mines label
        self.remaining_label = Label(self.root, text=f"Remaining: {self.num_mines}")
        self.remaining_label.grid(row=self.rows + 2, column=0, columnspan=self.cols + 1)

        # Hint button
        self.hint_button = Button(self.root, text="Hint", command=self.show_hint)
        self.hint_button.grid(row=self.rows + 3, column=0, columnspan=self.cols + 1)

    def generate_mines(self, exclude=None):
        """Generate mines randomly, excluding the first clicked cell."""
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols) if (r, c) != exclude]
        random.shuffle(positions)
        for i in range(self.num_mines):
            r, c = positions[i]
            self.grid[r][c].has_mine = True

    def calculate_adjacent_mines(self):
        """Calculate the number of adjacent mines for each cell."""
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[r][c].has_mine:
                    count = 0
                    for nr, nc in self.get_neighbors(r, c):
                        if self.grid[nr][nc].has_mine:
                            count += 1
                    self.grid[r][c].adjacent_mines = count

    def get_neighbors(self, r, c):
        """Return valid neighboring cell coordinates."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr = r + dr
                nc = c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))
        return neighbors

    def reveal_cell(self, r, c):
        """Handle revealing a cell on left-click."""
        if self.game_over:
            return
        if self.first_click:
            self.generate_mines(exclude=(r, c))
            self.calculate_adjacent_mines()
            self.first_click = False

        cell = self.grid[r][c]
        if cell.flagged or cell.revealed:
            return
        cell.revealed = True

        if cell.has_mine:
            self.game_over = True
            self.show_all_mines()
            messagebox.showinfo("Minesweeper", "You lost!")
        else:
            num = cell.adjacent_mines
            colors = {1: 'blue', 2: 'green', 3: 'red', 4: 'purple', 5: 'maroon', 6: 'turquoise', 7: 'black', 8: 'gray'}
            self.buttons[r][c].config(text=str(num) if num > 0 else "", fg=colors.get(num, 'black'), bg='white')
            if num == 0:
                for nr, nc in self.get_neighbors(r, c):
                    self.reveal_cell(nr, nc)
            if self.check_win():
                self.game_over = True
                messagebox.showinfo("Minesweeper", "You won!")

    def toggle_flag(self, r, c):
        """Toggle a flag on right-click."""
        if self.game_over:
            return
        cell = self.grid[r][c]
        if cell.revealed:
            return
        if cell.flagged:
            cell.flagged = False
            self.buttons[r][c].config(text="", bg='gray')
        else:
            cell.flagged = True
            self.buttons[r][c].config(text="F", bg='red')
        remaining = self.num_mines - self.count_flags()
        self.remaining_label.config(text=f"Remaining: {remaining}")

    def show_all_mines(self):
        """Reveal all mines when the game is lost."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c].has_mine:
                    self.buttons[r][c].config(text="M", bg='black', fg='white')

    def check_win(self):
        """Check if all non-mine cells are revealed."""
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if not cell.has_mine and not cell.revealed:
                    return False
        return True

    def count_flags(self):
        """Count the number of flagged cells."""
        return sum(1 for row in self.grid for cell in row if cell.flagged)

    def get_hint(self):
        """Find a safe cell to suggest as a hint."""
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]
                if cell.revealed and not cell.has_mine:
                    neighbors = self.get_neighbors(r, c)
                    flagged_neighbors = [n for n in neighbors if self.grid[n[0]][n[1]].flagged]
                    hidden_neighbors = [n for n in neighbors if not self.grid[n[0]][n[1]].revealed and not self.grid[n[0]][n[1]].flagged]
                    if len(flagged_neighbors) == cell.adjacent_mines and hidden_neighbors:
                        return hidden_neighbors[0]
        return None

    def show_hint(self):
        """Display a hint to the player."""
        if self.game_over:
            return
        hint = self.get_hint()
        if hint:
            r, c = hint
            messagebox.showinfo("Hint", f"Try clicking on row {r+1}, column {c+1}")
        else:
            messagebox.showinfo("Hint", "No hint available")

if __name__ == "__main__":
    game = Minesweeper(20, 20, 10)
    game.root.mainloop()