text= "Hello, Engineers! Welcome to Python String Functions."
#print("1. Case Convuppercase:")
#print("Uppercase:", text.upper())
#print("Lowercase:", text.lower())
#print("Titlecase:", text.title())

#print("2. String checking:")
#print("Is Alphanumeric?","Python123".isalnum())
#print("Is Alphabetic?","Python".isalpha())
#print("Is Digit?","12345".isdigit())
#print("Is Lower?","python".islower())
#print("Is Upper?","PYTHON".isupper())
#print("Is Title?","Hello World".istitle())
#print("Contains Only Spaces?","     ".isspace())

# print("3. Replacing and formatting:")
# print("Replace 'Python' with 'C++':", text.replace("Python", "C++"))
# print("Formatted String:", "Hello{}, Welcome!".format("Siddhi"))
# print(f"Using f-srings: Hello{'Siddhi'}, Welcome!")
# print()

print("4. Splitting and Joining:")
words = text.split()
print("Splitting into words:", words)
print("Joining words back:", " ".join(words))
csv_string = "apple,banana,grape,orange"
print("Splitting CSV:", csv_string.split(","))
print()

# print("Trimming Whitespaces:")
# extra_spaces = "  Hello, World!   "
# print("Stripped:", extra_spaces.strip())
# print("Left Stripped:", extra_spaces.lstrip())
# print("Right Stripped:", extra_spaces.rstrip())
# print()