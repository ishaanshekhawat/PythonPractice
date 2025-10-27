# Function to count the occurrences of a substring within a string
def count_substring(string, sub_string):
    # Initialize a counter to store the number of occurrences
    count1 = 0
    
    # Loop through each index of the main string
    for i in range(len(string)):
        # Check if the first character of the substring matches the current character in the string
        if sub_string[0] == string[i]:
            # If the substring matches starting from the current index, increment the count
            if sub_string == string[i:len(sub_string) + i]:
                count1 += 1  # Increase the counter by 1 for each match
    
    # Return the total number of matches found
    return count1

# Main code block that runs when the program is executed
if __name__ == '__main__':
    # Read the main string and the substring to search for
    string = input().strip()
    sub_string = input().strip()
    
    # Call the function to count the occurrences of the substring in the string
    count = count_substring(string, sub_string)
    
    # Print the result, which is the number of times the substring appears in the string
    print(count)
