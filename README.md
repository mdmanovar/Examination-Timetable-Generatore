## Examination Timetable Generator :
                  
# **Project Overview** :-->

> PS NO - 86.

> The Examination Timetable Generator is a Python-based project that automatically generates an examination schedule for multiple         subjects.

> The program takes subject names, a starting date, and holiday dates from the user. It automatically assigns examination dates to each subject while skipping Sundays and specified holidays.

> The main objective of this project is to simplify the examination scheduling process and generate an organized timetable.

# **Features** :-->

> Accepts multiple subjects from the user.
> Checks for empty subject input.
> Detects duplicate subjects.
> Validates dates in DD-MM-YYYY format.
> Accepts holiday dates.
> Automatically skips Sundays.
> Assigns dates and weekdays to each subject.
> Displays the final examination timetable in an organized format.

# **Technologies Used** :-->

> Programming Language: Python
> Module: datetime
> Data Structures: List, Tuple, Set, Dictionary
> Concepts: Functions, Loops, Conditional Statements, Exception Handling

#  **Project Structure** :-->

Examination-Timetable-Generator :
│
├── main.py
├── README.md
└── SUMMARY.md

##  **Requirements** :-->

> Any Python-supported code editor (VS Code, PyCharm, etc.)


##  **How It Works** :--> 

1. The program asks the user to enter subject names separated by commas.
2. It checks whether at least one subject is provided.
3. It detects duplicate subjects.
4. It asks for the examination starting date.
5. It validates the entered date.
6. It accepts holiday dates from the user.
7. It generates the timetable by skipping Sundays and holidays.
8. Finally, it displays the subject name, examination date, and day.

## **Input Format** :-->

>Example:

| Subjects | --> | Python, Java, C++ |

| Starting Date |--> | 01-12-2026 |

| Holidays | --> | 03-12-2026|

| No Holidays | --> |none |


## **Sample Output** :-->


EXAMINATION TIMETABLE GENERATOR :
---------------------------------
Enter subjects: Python, Java, C++

Enter starting date (DD-MM-YYYY): 01-12-2026

Enter holidays date(DD-MM-YYYY): 03-12-2026

EXAMINATION TIMETABLE :
-------------------------
Python : 01-12-2026 (Tuesday)
Java : 02-12-2026 (Wednesday)
C++ : 04-12-2026 (Friday)
-------------------------
Timetable generated successfully!


## **Project Objective** :-->

>The objective of this project is to create a simple and efficient examination timetable generation system using Python. It demonstrates the practical implementation of Python programming concepts and data structures.