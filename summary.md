# Examination Timetable Generator – **Project Summary** :

## 1. **Introduction** :-->

>The Examination Timetable Generator is a Python-based application designed to automatically generate examination schedules for multiple subjects.

>It takes subject names, a starting date, and holiday information from the user and generates an organized examination timetable.

## 2. **Objective** :-->

>The main objective of this project is to simplify examination scheduling by automatically assigning examination dates while avoiding Sundays and  holidays.

## 3. **Working Process** :-->

> The program follows these steps:

1. Accepts subject names from the user.
2. Checks whether the subject list is empty.
3. Detects duplicate subjects.
4. Accepts and validates the starting date.
5. Accepts holiday dates.
6. Skips Sundays and specified holidays.
7. Assigns examination dates and weekdays to subjects.
8. Displays the final timetable.

## 4. **Python Concepts Implemented** :-->

> **Tuple:** --> Stores the names of the weekdays.
> **List:**  --> Stores subjects, holidays, and timetable records.
> **Set:**  --> Identifies duplicate subject names.
> **Dictionary:** --> Stores examination details.
> **Functions:** --> Separates date validation and timetable generation logic.
> **For Loop:**  --> Iterates through subjects and holidays.
> **While Loop:** --> Skips Sundays and holidays.
> **Exception Handling:** --> Handles invalid date inputs.
> **datetime Module:** --> Performs date validation and date calculations.

 

## 5. Input and Output -->

**Input:**

> Subject names
> Starting examination date
> Holiday dates

**Output:** 

> Subject name
> Examination date
> Day of the week
> Successfully generated timetable

## 6.**Important Functions** :-->

# get_date(date_text):

> This function validates the date entered by the user in DD-MM-YYYY format and converts it into a Python date object.

# create_timetable(subjects, start_date, holidays):

> This function generates the examination timetable by assigning dates to subjects and automatically skipping Sundays and holidays.

## 7. **Advantages** :-->

> Saves time in preparing examination schedules.
> Prevents duplicate subject entries.
> Avoids scheduling examinations on Sundays.
> Allows users to specify holidays.
> Provides an organized timetable.
> Demonstrates practical Python programming skills.

## 8. **Limitations** :-->

> It does not provide a graphical user interface.
> It does not store generated timetables permanently.
> It does not include subject-specific examination durations.


## 9. **Conclusion** :-->

>The Examination Timetable Generator successfully demonstrates how Python can be used to automate a basic examination scheduling process.

>This project provides practical experience with Python data structures, functions, loops, conditional statements, exception handling, and date manipulation.