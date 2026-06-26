# Topic 06 Collaborative Assignment
# Your Name: Bradley Moore
# Date: 25 June 2026

# --- STARTER CODE ---
# This function takes a number and returns its square.
def square(n):
    return n * n

# This loop calls the function for numbers 1 through 5.
for i in range(1, 6):
    result = square(i)
    print(i, "squared is", result)

# --- YOUR EXTENSION BELOW THIS LINE ---
# Ideas: Write a second function, change the range,
# change what the function does, or add a while loop
# that lets the user keep entering numbers until they type "quit".

# Strange Math formula
def one_step_back(n):
    return n * (n - 1)

value = input("Enter a number to calculate or type the quit code:\n")
quit_code = ("quit", "q", "Quit", "Q", "QUIT")

while value not in quit_code:
    value = int(value)
    result = one_step_back(value)
    print(result)
    value = input("\nEnter a number to calculate or type the quit code:\n")

else:
    print("GOODBYE!!")
