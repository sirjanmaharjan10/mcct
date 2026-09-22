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
    