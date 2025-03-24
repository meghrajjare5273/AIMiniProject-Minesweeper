# 💣 Minesweeper Game 🏴‍☠️

A fun and interactive 💻 Minesweeper game 🎮 implemented in 🐍 Python using 🖼️ Tkinter.

---

## ⭐ Features
- **Classic Minesweeper gameplay 🎯** with a fully customizable 🔧 grid size 📏 and mine count 💣.
- **🖱️ Left-click to reveal 📖 cells**, 🖱️ Right-click to place 🚩 flags.
- **🎯 First-click safety** ensures the first move 🏁 is always safe 🛡️.
- **🔄 Recursive reveal** for empty 🏳️ cells, making gameplay smoother.
- **💡 Hint system** to suggest the next safe move 👣.
- **🏆 Win/Loss detection** with pop-up messages 📩 to notify the player.

---

## 📦 Requirements
- 🐍 Python 3.x
- 🖼️ Tkinter (pre-installed with Python)

---

## ⚙️ Installation
1. 📥 Clone the repository or download the script:
   ```sh
   git clone https://github.com/yourusername/minesweeper.git
   cd minesweeper
   ```
2. ▶️ Run the game:
   ```sh
   python minesweeper.py
   ```

---

## 🎮 How to Play
1. **🏁 Start the game** by running `minesweeper.py`.
2. **🖱️ Left-click** on a cell to reveal it 🔍.
3. **🖱️ Right-click** to place a 🚩 flag on a suspected mine 💣.
4. **💡 Use the hint button** to get a suggestion for a safe move 👣.
5. **🏆 Win by revealing all non-mine cells** or ❌ lose by clicking on a mine 💥.

---

## 🛠️ Customization
You can adjust the 📏 grid size and the 💣 number of mines by modifying the following line:
```python
if __name__ == "__main__":
    game = Minesweeper(20, 20, 10)  # (🟦 rows, 🟩 columns, 💣 number_of_mines)
    game.root.mainloop()
```

---

## 📸 Screenshots
(Include screenshots of the game here to showcase gameplay.)

---

## 📜 License
This project is open-source 🌍 and available under the [MIT License](LICENSE).

---

## 🤝 Contribution
Contributions are welcome! 🍴 Fork the project and submit 📩 pull requests to improve the game.

---

## 👨‍💻 Author
[Your Name] - [Your GitHub Profile]

