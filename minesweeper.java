import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class Minesweeper {
    // Declare global constants (name in ALL_CAPS)
    private static final String FILE_NAME = "instructions.txt";
    // Declare global markers
    public static int totalMarkers = 0;
    
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        try {
            introduction(FILE_NAME);
            // Call the replay function here
            replay(FILE_NAME);
        } catch (Exception sysMsg) {
            System.out.println(sysMsg.getMessage());
        }
    }

    public static void introduction(String fileName) throws IOException {
        String instructions;

        String line = "\nThere are 10 bombs placed randomly in a 9x9 grid.\n";
        String line1 = "The goal of the game is to type in coordinates of a square, e.g A1. without hitting a bomb.\n";
        String line2 = "A sqaure that doesn't have a bomb behind it, and adjacent squares with # equal to 0 will reveal several other squares.\n";
        String line3 = "Pay attention to the number after unlocking a square, ";
        line3 += "they provide hints to how many bombs are surrounding that particular square\n";
        String line4 = "You are able to mark squares that you think may be bombs";
        line4 += " by typing 'M' followed by the coordinates of that square. e.g. MD4\n";
        String line5 = "You may also deselect a square you have marked by typing in the same coordinates ";
        line5 += "that you marked the square with.\nThis will reset the total marker count you've used by however many you've deselected.\n";
        line5 += "Be aware of your markers because it won't adjust if squares that you marked are unlock.\n";
        line5 += "This adds a bit of a challenge so you're actively rationalizing where the next bomb will be, as long with being more attentive with your markers.\n";
        String line6 = "Once you open all the squares without hitting a bomb, you win!\n";

        instructions = line + line1 + line2 + line3 + line4 + line5 + line6;

        // Introduction
        System.out.println("Welcome to Minesweeper python v.2.0!");
        System.out.println("====================================");
        System.out.println("A game that involves a little bit of luck and skills using probability! \n");

        // Writes and saves a file called instructions as a text file
        FileWriter fileWriter = new FileWriter(FILE_NAME);
        fileWriter.write(instructions);
        fileWriter.close();
    }
    
    
    public static void play(int[][] m, int[][] e, long startTime) {
        String restart = "";

        int[] commandResult = commandInput(m, e, startTime);
        int c = commandResult[0];
        int r = commandResult[1];

        char value = (char) coordValue(r, c, m);

        if (value == -1) {
            displayBoard(e);
            System.out.println("Sorry, You Lose! You may try again!");

            System.out.println("Time: " + (System.currentTimeMillis() - startTime) / 1000 + "s");

            System.out.print("Play again? (Y/N): ");

            restart = sc.nextLine().toLowerCase();
            if (restart.equals("y")) {
                totalMarkers = 0;
                replay(FILE_NAME);
            } else {
                System.exit(0);
            }
        }

        e[r][c] = value;

        if (value == 0) {
            checkZeros(e, m, r, c);
        }

        displayBoard(e);

        int squaresLeft = 0;

        for (int x = 0; x < 9; x++) {
            int[] row = e[x];
            squaresLeft += countOccurrences(row, '?');
            squaresLeft += countOccurrences(row, 'M');
        }

        if (squaresLeft == 10) {
            displayBoard(m);
            System.out.println("Congratulations, You win!");

            System.out.println("You've finished in: " + (System.currentTimeMillis() - startTime) / 1000 + "s");

            System.out.print("Would you like to play again? (Y/N): ");
            restart = sc.nextLine().toLowerCase();

            if (restart.equals("y")) {
                totalMarkers = 0;
                replay(FILE_NAME);
            } else {
                System.exit(0);
            }
        }

        play(m, e, startTime);
    }

    
    public static int countOccurrences(int[] row, char target) {
        int count = 0;
        for (int c : row) {
            if (c == target) {
                count++;
            }
        }
        return count;
    }
    
    public static void replay(String fileName) {
   

        System.out.print("Do you want to read the instructions? Type 'n' if you don't, otherwise press anything: ");
        String askReadInstructions = sc.nextLine();

        if (!askReadInstructions.toLowerCase().equals("n")) {
            try {
                BufferedReader instructionsRead = new BufferedReader(new FileReader(fileName));
                String line;
                while ((line = instructionsRead.readLine()) != null) {
                    System.out.println(line);
                }
                instructionsRead.close();
            } catch (IOException e) {
                e.printStackTrace();
            }

            System.out.println("Press [Enter] to play: ");
            sc.nextLine();
        } else if (askReadInstructions.toLowerCase().equals("n")) {
            System.out.println("Press [Enter] to play: ");
            sc.nextLine();
        } else {
            replay(fileName);
        }

        int[][] m = new int[9][9];

        for (int i = 0; i < 10; i++) {
            placeMine(m);
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int value = coordValue(r, c, m);
                if (value == -1) {
                	 update_grid_values(r, c, m, value);
                }
            }
        }
        
       
        int[][] e = new int[9][9];
        for (int i = 0; i < e.length; i++) {
            for (int j = 0; j < e[i].length; j++) {
                e[i][j] = '?';
            }
        }

        displayBoard(e);

        long startTime = System.currentTimeMillis();

        play(m, e, startTime);
    }
    
    public static void displayBoard(int[][] m) {
    	// Clear console screen
    	System.out.print("\033[H\033[2]");
    	System.out.flush();
    	
    	// Print indentation
    	for (int indent = 0; indent < 35; indent++) {
            System.out.println();
        }

        System.out.println("    A   B   C   D   E   F   G   H   I");
        System.out.println("  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗");

        for (int r = 0; r < 9; r++) {
            System.out.print(r + "║");
            for (int c = 0; c < 9; c++) {
                System.out.print(" " + coordValueDisplay(r, c, m) + " ║");
            }
            System.out.println();

            if (r != 8) {
                System.out.println("  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣");
            }
        }
        System.out.println("  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝");

        // Replace total_markers with the appropriate variable or method call to get the number of markers used
        System.out.println("Total Markers Used: " + totalMarkers);
    }
    
    
    public static void placeMine(int[][] m) {
        Random rand = new Random();
        int r = rand.nextInt(9);
        int c = rand.nextInt(9);

        // Places a mine at a random location or at a different location if a mine is already at the current location
        int[] currentRow = m[r];
        if (currentRow[c] != -1) { // Assuming -1 represents a mine, adjust accordingly if using a different value
            currentRow[c] = -1;
        } else {
            placeMine(m);
        }
    }
    
    public static void marker(int r, int c, int[][] e) {
        if (coordValue(r, c, e) == '?') {
            e[r][c] = 'M';
            totalMarkers += 1;
        } else {
            removeMarker(r, c, e);
        }
        displayBoard(e);
    }
    
    
    public static void removeMarker(int r, int c, int[][] e) {
        if (coordValue(r, c, e) == 'M') {
            e[r][c] = '?';
            totalMarkers -= 1;
        }
    }
    
    
    public static boolean contains(String[] array, String value) {
        for (String element : array) {
            if (element.equals(value)) {
                return true;
            }
        }
        return false;
    }
    
    public static int coordValue(int r, int c, int[][] m) {
        return m[r][c];
    }
    
    public static String coordValueDisplay(int r, int c, int[][] m) {
        int value = m[r][c];

        if (value == 0) {
            return " ";
        }
        return Integer.toString(value);
    }
    
    public static void update_grid_values(int ri, int c, int[][] m, int value) {
        // Updates values of the row above
        if (ri - 1 > -1) {
            int[] r = m[ri - 1];
            if (c - 1 > -1) {
                if (r[c - 1] != -1) {
                    r[c - 1] += 1;
                }
            }

            if (r[c] != -1) {
                r[c] += 1;
            }

            if (9 > c + 1) {
                if (r[c + 1] != -1) {
                    r[c + 1] += 1;
                }
            }
        }

        // Updates values of the same row.
        int[] r = m[ri];

        if (c - 1 > -1) {
            if (r[c - 1] != -1) {
                r[c - 1] += 1;
            }
        }

        if (9 > c + 1) {
            if (r[c + 1] != -1) {
                r[c + 1] += 1;
            }
        }

        // Updates values of the row below.
        if (9 > ri + 1) {
            r = m[ri + 1];

            if (c - 1 > -1) {
                if (r[c - 1] != -1) {
                    r[c - 1] += 1;
                }
            }

            if (r[c] != -1) {
                r[c] += 1;
            }

            if (9 > c + 1) {
                if (r[c + 1] != -1) {
                    r[c + 1] += 1;
                }
            }
        }
    }
    
    
    public static int[] commandInput(int[][] m, int[][] e, long startTime) {
     
        String[] letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i"};
        String[] numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8"};

        while (true) {
            System.out.print("Input coordinates for square (ex. A4) or place a marker (ex.MB4): ");
            String chooseSquare = sc.nextLine().toLowerCase();

            if (chooseSquare.length() == 3 && chooseSquare.charAt(0) == 'm' && contains(letters, String.valueOf(chooseSquare.charAt(1))) && contains(numbers, String.valueOf(chooseSquare.charAt(2)))) {
                int c = chooseSquare.charAt(1) - 97;
                int r = Integer.parseInt(String.valueOf(chooseSquare.charAt(2)));
                marker(r, c, e);
                play(m, e, startTime);
                break;
            } else if (chooseSquare.length() == 2 && contains(letters, String.valueOf(chooseSquare.charAt(0))) && contains(numbers, String.valueOf(chooseSquare.charAt(1)))) {
                return new int[]{chooseSquare.charAt(0) - 97, Integer.parseInt(String.valueOf(chooseSquare.charAt(1)))};
            } else {
                continue;
            }
        }
        return null;
    }
    
    
    public static void zeroOpenSquares(int r, int c, int[][] e, int[][] m) {
        if (r - 1 > -1) {
            int[] row = e[r - 1];

            if (c - 1 > -1) {
                row[c - 1] = coordValue(r - 1, c - 1, m);
            }

            row[c] = coordValue(r - 1, c, m);

            if (9 > c + 1) {
                row[c + 1] = coordValue(r - 1, c + 1, m);
            }
        }
    }
    
    
    public static void checkZeros(int[][] e, int[][] m, int r, int c) {
        int[][] emptyGrid = deepCopy(e);
        zeroOpenSquares(r, c, e, m);

        if (Arrays.deepEquals(emptyGrid, e)) {
            return;
        }

        while (true) {
            emptyGrid = deepCopy(e);

            for (r = 0; r < 9; r++) {
                for (c = 0; c < 9; c++) {
                    if (coordValue(r, c, e) == 0) {
                        zeroOpenSquares(r, c, e, m);
                    }
                }
            }

            if (Arrays.deepEquals(emptyGrid, e)) {
                return;
            }
        }
    }

    
    public static int[][] deepCopy(int[][] original) {
        int[][] copy = new int[original.length][];
        for (int i = 0; i < original.length; i++) {
            copy[i] = Arrays.copyOf(original[i], original[i].length);
        }
        return copy;
    }
    
    
  
    
    


}