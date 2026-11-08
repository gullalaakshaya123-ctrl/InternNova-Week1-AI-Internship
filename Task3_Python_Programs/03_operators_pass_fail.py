
# Student Pass or Fail Checker

name = input("Enter student name: ")

mark1 = float(input("Enter subject 1 marks: "))
mark2 = float(input("Enter subject 2 marks: "))
mark3 = float(input("Enter subject 3 marks: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
