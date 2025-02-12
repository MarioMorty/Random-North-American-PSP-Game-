import random

def randomize_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        lines = [line.strip().split("USA")[0] for line in lines]  # Remove everything after "USA", including "USA" itself
        
        lines = [line for line in lines if line]  # Remove empty lines after filtering
        
        if lines:
            print("You should play")
            print(random.choice(lines))  # Pick one random line and print it
        else:
            print("Error: No valid lines after filtering.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
def main():
    filename = input("Enter the filename (with .txt extension): ")
    while True:
        randomize_lines(filename)
        key = input("Press space once, then enter to run again or any other key then enter to exit: ")
        if key != " ":
            break

main()
