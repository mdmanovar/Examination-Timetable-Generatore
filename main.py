from datetime import date, timedelta

# Tuple: days -->
days = ("Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday")
        


# Function: Date check :
def get_date(date_text):
    try:
        parts = date_text.split("-")

        if len(parts) != 3:
            return None

        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])

        return date(year, month, day)

    except ValueError:
        return None


# Function: Timetable create :
def create_timetable(subjects, start_date, holidays):

    timetable = []
    exam_date = start_date

    for subject in subjects:

        # Sunday aur holiday ko skip karna
        while exam_date.weekday() == 6 or exam_date in holidays:
            exam_date = exam_date + timedelta(days=1)

        # Dictionary: Exam ki details
        exam = {
            "Subject": subject,
            "Date": exam_date.strftime("%d-%m-%Y"),
            "Day": days[exam_date.weekday()]
        }

        timetable.append(exam)

        exam_date = exam_date + timedelta(days=1)

    return timetable


# Main program : 

print("EXAMINATION TIMETABLE GENERATOR : ")
print("--------------------------------")

# List: Subjects check

subject_text = input("Enter subjects: ")

subjects = []
if subject_text.strip().lower() not in ("none" ,"(none)" , ""):
    for subject in subject_text.split(","):
        subject = subject.strip()

        if subject != "":
            subjects.append(subject)


# Empty subjects check 
if len(subjects) == 0:
    print("At least one subject is required.")

else:

    # Set: Duplicate subjects check:
    unique_subjects = set()

    duplicate_found = False

    for subject in subjects:

        if subject.lower() in unique_subjects:
            duplicate_found = True
            print("Duplicate subject found:", subject)

        else:
            unique_subjects.add(subject.lower())

    if duplicate_found:
        print("Please enter each subject only once.")

    else:

        # Starting date :
        start_text = input("Enter starting date (DD-MM-YYYY): ")
        start_date = get_date(start_text)

        if start_date is None:
            print("Invalid date.Please enter the date as DD-MM-YYYY.")

        else:

            # Holidays  list :
            holiday_text = input("Enter holidays date(DD-MM-YYYY): ")

            holidays = []
            holiday_error = False

            if holiday_text.lower() != "none":

                for holiday in holiday_text.split(","):

                    holiday = holiday.strip()
                    holiday_date = get_date(holiday)

                    if holiday_date is None:
                        holiday_error = True
                        print("Invalid holiday date:", holiday)

                    else:
                        holidays.append(holiday_date)

            if holiday_error:
                print("Please enter valid holiday dates.")

            else:

                # Function call and create time table :
                timetable = create_timetable(
                    subjects, start_date, holidays
                )

                # Final timetable display :
                print("\nEXAMINATION TIMETABLE :")
                print("-------------------------")
                # print("_" * 45)


                for exam in timetable:
                    print(exam["Subject"],":",exam["Date"], "("+ exam["Day"] + ")" )

                print("-------------------------")
                # print("_" * 45)

                print("Timetable generated successfully")