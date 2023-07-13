# Progression Outcome Predictor - Coursework Solution

This program allows students to predict their progression outcome based on their credit scores.

## Installation

To run this program, make sure you have Python installed on your machine.

## Usage

1. Run the program.
2. Enter the number of credits at pass, defer, and fail when prompted.
3. The program will display the appropriate progression outcome for the student.

### Validation

- The program will display "Integer required" if a credit input is of the wrong data type.
- The program will display "Out of range" if credits entered are not in the range 0, 20, 40, 60, 80, 100, and 120.
- The program will display "Total incorrect" if the total of the pass, defer, and fail credits is not 120.

### Multiple Outcomes

- The program allows a staff member to predict progression outcomes for multiple students.
- Enter the credits at pass, defer, and fail for each student.
- The program will display the appropriate progression outcome.
- Continue entering data until you enter 'q' to quit.

### Histogram

- When 'q' is entered, the program will generate a histogram showing the number of students in each progression category.
- The histogram will include the categories: progress, trailing, module retriever, and exclude.
- The total number of students will also be displayed.

## Part 2: List (extension)

The program stores the input progression data in a list.
The stored data is then printed in the following format:

Part 2:
- Progress - 120, 0, 0
- Progress (module trailer) - 100, 0, 20
- Module retriever - 80, 20, 20
- Module retriever - 60, 0, 60
- Exclude - 40, 0, 80

## Part 3: Text File (extension)

The program saves the inputted progression data to a text file.
Later, it accesses the stored data and prints it out in the following format:

Part 3:
- Progress - 120, 0, 0
- Progress (module trailer) - 100, 0, 20
- Module retriever - 80, 20, 20
- Module retriever - 60, 0, 60
- Exclude - 40, 0, 80

## Part 4: Dictionary (separate program)

A separate program saves the input progression data to a dictionary or nested dictionary.
The data is then accessed and displayed, including the unique student IDs.

Part 4:
- w1234567: Progress - 120, 0, 0
- w1234566: Progress (module trailer) - 100, 0, 20
- w1234565: Module retriever - 80, 20, 20
- w1234564: Module retriever - 60, 0, 60
- w1234563: Exclude - 40, 0, 80

Please refer to the individual program files for more details on each part's implementation.
