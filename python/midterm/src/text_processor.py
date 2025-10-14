#text_processor.py

def process_input():
    # Read input from the user
    # Repeatedly prompt the user until they provide a non-empty string
    # Handle the 'show' function to print the list, and the 'exit' function to terminate the program
    input_list = []
    # Prompt the user for input
    while True:
        # Get user input
        user_input = input("Enter a string (or 'show' to display, 'exit' to quit): ").strip().lower()
        # Check for exit condition
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        # Check for show condition
        elif user_input.lower() == 'show':
            print("Current list:", input_list)
        #
        elif user_input:
            input_list.append(user_input)

        #
        else:
            print("Empty input. Please enter a valid string.")
