# Sudoku-Solver
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective of the puzzle is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 sub-grids contains all of the digits from 1 to 9. The puzzle starts with some cells already filled with numbers, which serves as a constraint on the possible solutions. The difficulty of the puzzle depends on the number of pre-filled cells and the arrangement of these numbers.

## What is Backtracking
Backtracking is an algorithmic technique that is used to find all possible solutions to a problem by incrementally building and exploring a decision space while maintaining a mechanism to backtrack and undo decisions that lead to invalid solutions. It is commonly used in problems that involve searching for all possible solutions or finding paths in a maze.

## Working of the Algorithm
Starting with an incomplete board:
<ol>
	<li> Find some empty space </li>
	<li> Attempt to place the digits 1-9 in that space </li>
	<li> Check if that digit is valid in the current spot based on the current board
		<ol>
		<li> If the digit is valid, recursively attempt to fill the board using steps 1-3.</li>
		<li> If it is not valid, reset the square you just filled and go back to the previous step.</li>
		</ol>
	</li>
	<li> Once the board is full by the definition of this algorithm we have found a solution.</li>
</ol>
