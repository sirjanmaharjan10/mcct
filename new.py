items = ["apple", "banana", "orange", "apple", "mango"]

seen = []

for item in items:
    if item in seen:
        print("Duplicate element found:", item)
        break
    seen.append(item)
else:
    print("All elements are unique.")


print("=====  =====")


marks = []

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if all(mark >= 50 for mark in marks):
    result = "PASS"
else:
    result = "FAIL"

print("\n===== GRADE RESULT =====")
for i in range(5):
    print("Subject", i + 1, ":", marks[i])

print("Total Marks :", total)
print("Average Mark:", average)
print("Grade       :", grade)
print("Result      :", result)


text = input("Enter a string with at least 8 characters: ")

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    result = ""

    for i in range(len(text)):
        char = text[i]

        if i % 2 == 0:
            ascii_value = ord(char)

            if 97 <= ascii_value <= 122:
                ascii_value = ascii_value - 32

            char = chr(ascii_value)

        result = result + char

    print("Modified string:", result)
