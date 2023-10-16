import subprocess

def run_command(user_input):
    # Insecure command execution
    result = subprocess.check_output("echo " + user_input, shell=True)
    return result

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    output = run_command(user_input)
    print("Output: " + output.decode())


# The run_command function takes user input and uses it to construct a shell command using string concatenation.
# The constructed command is executed using subprocess.check_output with shell=True. This makes the code susceptible to command injection if the user input contains malicious commands.
