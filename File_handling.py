# File creation, writing to the file, and error handling

try:
    # Step 1: Create a new file and write text
    with open("Moles.txt", "w") as file:
        file.write("Hello, this is mole 1.\n")
        file.write("This is line 2 with a number: 42.\n")
        file.write("Another molecule on line 3.\n")
    print("File 'Moles.txt' created and initial content written.")

    # Step 2: Read the file contents and display them
    with open("Moles.txt", "r") as file:
        print("\nReading contents of 'Moles.txt':")
        content = file.read()
        print(content)

    # Step 3: Append new lines to the existing file content
    with open("Moles.txt", "a") as file:
        file.write("Appending line 4: More content here.\n")
        file.write("Appending line 5 with a number: 100.\n")
        file.write("Final line 6, just a message.\n")
    print("\nNew lines appended to 'Moles.txt'.")

    # Step 4: Read the updated file contents and display them
    with open("Moles.txt", "r") as file:
        print("\nReading updated contents of 'Moles.txt':")
        updated_content = file.read()
        print(updated_content)

# Error handling for common file-related exceptions
except FileNotFoundError as fnf_error:
    print(f"Error: File not found - {fnf_error}")
except PermissionError as perm_error:
    print(f"Error: Permission denied - {perm_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nExecution completed.")
