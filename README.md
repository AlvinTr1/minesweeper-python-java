# minesweeper-python-java
Classic Minesweeper on a 9x9 grid with 10 bombs. The goal of the game is to type in coordinates of a square, e.g A1. without hitting a bomb. 
A sqaure that doesn't have a bomb behind it, and adjacent squares with # equal to 0 will reveal several other squares.
Pay attention to the number after unlocking a square, they provide hints to how many bombs are surrounding that particular square
You are able to mark squares that you think may be bombs by typing 'M' followed by the coordinates of that square. e.g. MD4
You may also deselect a square you have marked by typing in the same coordinates that you marked the square with.
This will reset the total marker count you've used by however many you've deselected.
Be aware of your markers because it won't adjust if squares that you marked are unlock.
This adds a bit of a challenge so you're actively rationalizing where the next bomb will be, as long with being more attentive with your markers.
Once you open all the squares without hitting a bomb, you win!
