# (i) Define a function called lastCharacter
def lastCharacter(code_line):
    return code_line.strip().endswith(':')

# (ii) Add space equivalent to one tab if lastCharacter returns true
def addTabSpace(code_line):
    if lastCharacter(code_line):
        return code_line + '    '  # Assuming one tab is equivalent to four spaces
    else:
        return code_line

# (iii) Repeat (ii) until 'class' or 'def' is entered as the first string
code_block = []
while True:
    line = input("Enter a line of code: ")
    code_block.append(addTabSpace(line))
    if line.strip().startswith('class') or line.strip().startswith('def'):
        break

# Print the modified code block
print("Modified Code Block:")
for line in code_block:
    print(line)

# (iv) Determine if List1 is a tuple
List1 = [1, 2, 3]  # Replace this with your actual variable
if isinstance(List1, tuple):
    print("List1 is a tuple")
else:
    print("List1 is not a tuple")

# (v) Exception handling for List1 being a tuple
try:
    if isinstance(List1, tuple):
        raise ValueError("You cannot modify a tuple.")
    # Add other code here if needed
except ValueError as e:
    print(f"Error: {e}")
#    (i) The lastCharacter function checks if the last character of a given string is a colon.
  #  (ii) The addTabSpace function adds space equivalent to one tab if lastCharacter returns true.
  #  (iii) A while loop is used to continuously take input from the user and modify the code block until 'class' or 'def' is entered as the first string of a line.
  #  (iv) The isinstance function is used to check if List1 is a tuple.
   # (v) Exception handling is implemented to handle the case where a user tries to modify List1 if it is a tuple.
