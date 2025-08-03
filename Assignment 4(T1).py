#Task 1: Read a File and Handle Errors
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            file.write("This is a sample text file.\n")
            file.write("It contains multiple lines.\n")
            print(f"File '{filename}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
create_file('sample.txt')

def read_file(file):
    try:
        with open(file, 'r') as f:
            print("Reading File content:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file}' does not exist.")
read_file('Sample.txt')
