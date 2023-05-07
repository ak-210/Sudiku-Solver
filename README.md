# Sudiku-Solver

#What is Backtracking
Backtracking is an algorithmic technique that is used to find all possible solutions to a problem by incrementally building and exploring a decision space while maintaining a mechanism to backtrack and undo decisions that lead to invalid solutions. It is commonly used in problems that involve searching for all possible solutions or finding paths in a maze.![image](https://user-images.githubusercontent.com/106259041/236660673-bdf4db57-be0b-42aa-9c95-71004752cba9.png)

#Working of the Algorithm
Starting with an incomplete board:
	1. Find some empty space
	2. Attempt to place the digits 1-9 in that space
	3. Check if that digit is valid in the current spot based on the current board
		a. If the digit is valid, recursively attempt to fill the board using steps 1-3.
		b. If it is not valid, reset the square you just filled and go back to the previous step.
Once the board is full by the definition of this algorithm we have found a solution.![image](https://user-images.githubusercontent.com/106259041/236660718-d72edd9e-31f3-491f-b1e1-f5bcd5c36761.png)
