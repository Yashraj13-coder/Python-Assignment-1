# Task 2: Write and Append Data to a File
def write_to_file(filename):
    user_input = input("Enter text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print(f"Data Successfully written to '{filename}'.")

def append_to_file(filename):
    additional_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Additional data appended to the file.")

def read_file(filename):
    print("\nFinal content of the file:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

filename = 'output.txt'

write_to_file(filename)
append_to_file(filename)
read_file(filename)
