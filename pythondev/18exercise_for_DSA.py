from collections import Counter

sentence = "This is a common interview question"
letters = [char for char in sentence if char.isalpha()]  # Filter only alphabetic characters
counter = Counter(letters)

most_common = counter.most_common(1)  # Get the most common letter
if most_common:
    print(f"The most repeated letter is: '{most_common[0][0]}' with {most_common[0][1]} occurrences.")
else:
    print("No letters found!")
