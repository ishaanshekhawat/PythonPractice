# Function to print a personalized greeting message using the provided first and last name
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

# Main code block that executes when the script is run directly
if __name__ == '__main__':
    # Read the user's first name as input
    first_name = input()
    # Read the user's last name as input
    last_name = input()
    
    # Call the function with the provided inputs to display the greeting
    print_full_name(first_name, last_name)
