text = input("Enter a string: ")
result = ""
for ch in text:
    if ch not in result:
        result = result + ch
print("String after removing duplicates:", result)
