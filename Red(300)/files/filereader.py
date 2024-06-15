# Open the file in read mode
with open('names.txt', 'r') as file:
    # Read all lines in the file
    names = file.readlines()

# Count the occurrences of 'Kate'
kate_count = names.count('Kate\n')

# Print the result
print(f"The name 'Kate' appears {kate_count} times in the file.")
