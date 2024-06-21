# Othello_game
1.	Introduction:
Othello, also known as Reversi, is a classic board game played on an 8x8 grid. The game involves two players who take turns placing their discs on the board, with the goal of having the majority of discs of their color by the end of the game. The game ends when neither player can make a valid move, and the player with the most discs on the board wins.

2.	Game Setup:

1.	Board Initialization:
o	The board is an 8x8 grid.
o	Each cell in the grid can be empty, contain a black disc (represented as 'X'), or contain a white disc (represented as 'O').
o	The initial setup places two black discs and two white discs in the center of the board in a diagonal pattern.

3.	Basic Rules:
1.	Starting the Game:
o	The game begins with the black player making the first move.
o	Players alternate turns throughout the game.

2.	Making a Move:
o	On a player's turn, they must place a disc of their color on the board.
o	A valid move is one where the newly placed disc outflanks one or more of the opponent's discs in any direction (horizontally, vertically, or diagonally).
o	Outflanking means there are one or more continuous lines of the opponent's discs between the newly placed disc and another disc of the current player's color.

3.	Flipping Discs:
o	After placing a disc, all outflanked discs are flipped to the current player's color.
o	For example, if a black disc is placed such that it outflanks white discs, those white discs are flipped to black.

4.	Valid Moves:
o	If a player has no valid moves, they must pass their turn to the opponent.
o	If neither player has a valid move, the game ends.

4.	 Game End and Scoring:
1.	Game End Conditions:
o	The game ends when neither player can make a valid move.
o	The board is filled, or no further moves are possible.

2.	Determining the Winner:
o	The player with the majority of discs on the board at the end of the game is the winner.
o	If both players have an equal number of discs, the game is a tie.

Playing the Game:
1.	Turn-Based Play:
o	Players take turns making their moves.
o	The current state of the board is displayed after each move.

