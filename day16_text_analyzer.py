text = input("Enter a sentence: ")

characters = len(text)
words = len(text.split())
spaces = text.count(" ")

print("Characters:", characters)
print("Words:", words)
print("Spaces:", spaces)
