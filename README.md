# Mini-Project
Sudoku Solver using Backtracking and Recursion to automatically solve 9×9 Sudoku puzzles. Developed in Python.
# Sudoku Solver Using Backtracking and Recursion

## Project Overview

The Sudoku Solver is a Python-based mini project that automatically solves a 9×9 Sudoku puzzle using the Backtracking Algorithm and Recursion. The program fills empty cells by checking valid numbers according to Sudoku rules and recursively explores possible solutions until the puzzle is completely solved.

---

## Problem Statement

Sudoku is a popular logic-based puzzle that can become difficult and time-consuming to solve manually. An automated Sudoku solver helps solve puzzles quickly and accurately while demonstrating the practical use of recursion and backtracking algorithms.

---

## Objectives

* Automatically solve a 9×9 Sudoku puzzle.
* Implement the Backtracking Algorithm.
* Demonstrate the use of Recursion.
* Validate Sudoku rules for every move.
* Produce the correct completed Sudoku grid.

---

## Technologies Used

* Python
* Backtracking Algorithm
* Recursion
* 2D Arrays

---

## Project Structure

```text
Mini-Project-Sudoku-Solver-Using-Backtracking-and-Recursion/
│
├── sudoku_solver.py
├── Project_Report.pdf
├── Presentation.pptx
└── README.md
```

---

## Methodology

1. Represent the Sudoku puzzle as a 9×9 matrix.
2. Find the next empty cell.
3. Try numbers from 1 to 9.
4. Check row, column, and 3×3 subgrid constraints.
5. Place the number if it is valid.
6. Recursively solve the remaining puzzle.
7. Backtrack whenever an invalid state is reached.
8. Continue until the puzzle is completely solved.

---

## Algorithm

1. Start
2. Find an empty cell.
3. Try numbers from 1 to 9.
4. Check Sudoku constraints.
5. If valid, place the number.
6. Recursively solve the puzzle.
7. If no valid number exists, remove the current number (Backtrack).
8. Repeat until all cells are filled.
9. Display the solved Sudoku puzzle.
10. End.

---

## Sample Input

```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

---

## Sample Output

```text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

## Features

* Automatic Sudoku solving
* Efficient Backtracking Algorithm
* Recursive implementation
* Validates all Sudoku rules
* Simple console-based interface
* Fast and accurate solution generation

---

## Advantages

* Eliminates manual solving effort
* Demonstrates recursion and backtracking concepts
* Produces accurate solutions
* Easy to understand and modify
* Suitable for educational purposes

---

## Future Enhancements

* Graphical User Interface (GUI)
* Sudoku puzzle generator
* Difficulty level selection
* Image-based Sudoku recognition using Computer Vision
* Mobile application support
* AI-assisted Sudoku solving

---

## Conclusion

The Sudoku Solver Using Backtracking and Recursion efficiently solves valid Sudoku puzzles by systematically exploring possible values and backtracking whenever necessary. This project demonstrates the practical application of recursion and constraint satisfaction algorithms in solving real-world logical problems.

---

## Team Members

* K. Arshiya
* K. Gayathri

---

## License

This project is developed for academic and educational purposes.
