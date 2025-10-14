#main.py

def process_input():
    # Read input from the user
    # Handle the 'exit' and 'show' conditions
    # Append items from the user input to an input_list
    # Use the split() method to add multiple numbers from the users input to peel off each number and add it to the sum, increment the count but 1
    # Handle invalid input nicely
    # Compute the average by dividing the sum total but the count
    # Keep a count of the numbers entered, a sum of the numbers entered and the average of the numbers entered
    # Handle the 'show' function to print the list, and the 'exit' function to terminate the program
    input_list = []
    #total = 0.0
    count = 0
    average = 0.0

    # Prompt the user for input
    while True:
        # Get user input
        user_input = input("Enter one or more numbers separated by spaces (or 'show' to display, 'exit' to quit): ").strip().lower()

        # Check for exit condition
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Check for show condition
        elif user_input.lower() == 'show':
            print("Current list:", input_list)            

        elif user_input:
            input_list.append(user_input)
            
            #split the input string into individual number strings
            number_strings = user_input.split()
            
            #convert the number strings to floats and update total and count
            for num_str in number_strings:
                try:
                    number = float(num_str)
                    total += number
                    count += 1
                except ValueError:
                    print(f"'{num_str}' is not a valid number and will be ignored.")
                if count > 0:
                    average = total / count
                    #print(f"Count: {count}, Sum: {total}, Average: {average}")
                else:
                    average = 0.0
            print(f"Count: {count}, Sum: {total}, Average: {average}")    
         
if __name__ == "__main__":
    print("Welcome to the Number Logger Processor Program for IT-566A Midterm!")
    process_input()
    print("Thank you for testing my program.")

    