import openai
import subprocess
import json

# Function to set up OpenAI API
def setup_openai(api_key):
    openai.api_key = api_key

# Function to send code to OpenAI for suggestions
def get_openai_suggestions(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Please debug the following code and suggest fixes:\n{code}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to run mypy and capture type errors
def run_mypy(file_path):
    result = subprocess.run(['mypy', file_path], capture_output=True, text=True)
    return result.stdout

# Function to run pylint and capture code quality issues
def run_pylint(file_path):
    result = subprocess.run(['pylint', file_path], capture_output=True, text=True)
    return result.stdout

# Function to run flake8 and capture style issues
def run_flake8(file_path):
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    return result.stdout

# Main function to orchestrate the debugging process
def main(file_path, api_key):
    setup_openai(api_key)
    
    with open(file_path, 'r') as file:
        code = file.read()
    
    # Run mypy
    mypy_results = run_mypy(file_path)
    print("Mypy Results:\n", mypy_results)
    
    # Run pylint
    pylint_results = run_pylint(file_path)
    print("Pylint Results:\n", pylint_results)
    
    # Run flake8
    flake8_results = run_flake8(file_path)
    print("Flake8 Results:\n", flake8_results)

    # Get suggestions from OpenAI
    suggestions = get_openai_suggestions(code)
    print("OpenAI Suggestions:\n", suggestions)

if __name__ == "__main__":
    # Example usage
    main('your_script.py', 'your_openai_api_key')
