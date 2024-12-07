from collections import namedtuple
import csv

# Input the total number of students
n = int(input().strip())

# Input the column headers
headers = input().strip().split()

# Create a namedtuple for storing student data
Student = namedtuple('Student', headers)

# Initialize total marks
total_marks = 0

# Process student data
for _ in range(n):
    row = input().strip().split()
    student = Student(*row)  # Create a Student object using unpacking
    total_marks += int(student.MARKS)  # Access 'MARKS' field by name

# Calculate and print the average marks, rounded to 2 decimal places
average_marks = total_marks / n
print(f"{average_marks:.2f}")




# Input the total number of students
n = int(input().strip())

# Input the column headers
headers = input().strip().split()

# Find the index of the 'MARKS' column
marks_index = headers.index('MARKS')

# Initialize total marks and student count
total_marks = 0

# Read the next n lines for student data
for _ in range(n):
    row = input().strip().split()
    total_marks += int(row[marks_index])

# Calculate and print the average marks, rounded to 2 decimal places
average_marks = total_marks / n
print(f"{average_marks:.2f}")