# Quotation mark issues
# Double quotes (") and single quotes (') can be used interchangeably but the
# same type of quotation mark must be used to open and close the string.
# It is best practice to remain consistent with your use of quotation marks.
# If a string needs to include one type of quotation mark, you can use the
# other kind to open and close the string.

# What if you want to use both types of quotation marks in your string?
# Then you can use the backslash (\) escape character. This tells Python to
# treat the following character differently than it ordinarily would.

# You can also use triple quotes to print over multiple lines

# Often, we don't want to use triple quotes to store text across multiple
# lines, as the text can't be indented when we get to complex decisions.
# In those situations, we can insert a new line character instead.
print("I'm Having a great day")
print('She said "I\'m having a great day"')
# Print a new line character: \n
print ("Hello\nWorld")

# Ask the user for an input string and concatenate it with a new line
name_input = str(input("Hello\nWhat is your name?"))
print("Hello", name_input)
# Print formatting options:

# f-strings
print(f"You said: {name_input}")
# Repeating strings
print(f"Let's print you name 5 times: \n {name_input * 5}" )
# Lowercase strings
print(f"Lowercase: {name_input.lower()}")
# Uppercase strings
print(f"Uppercase: {name_input.upper()}")
# Title case strings
print(f"Title: {name_input.title()}")
# Multiline f-strings
radius = 4
pi = 3.14159265358979323846
print(
    f"Radius: {radius}cm\n"
    +f"Circumfrence: {2 * pi *radius}cm\n"
    +f"Area: {pi * radius **2}cm\n"
)
# Format floating point values
print(f"Pi to two decimal place is {pi:.2f}\n")
# Add a thousands comma to a number
print(f"I have ${4500:,} to spend on vacation.")

# Create a string of 50 dashes
dash_string= "-" * 50
print(dash_string)
# Long text as an f-string
input_string = "Pretty Good"
long_text = f"""Welcome to Python class!
Your answer to "How are you enjoying Python class" was {input_string}
What was that?
{input_string * 5}
{dash_string}

Lowercase: {input_string.lower()}
Uppercase: {input_string.upper()}
Title case: {input_string.title()}
{dash_string}

Radius: {radius}cm
Circumference: {2 * pi * radius}cm
Area: {pi * radius ** 2}cm

Pi to two decimal places is {pi:.2f}

I have ${3500:,} to spend on my vacation this year."

Bye now!
"""

print(long_text)