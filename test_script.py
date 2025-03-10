# This is a test script with intentional errors for debugging

def add_numbers(a, b):
    return a + b

def main():
    print("Adding numbers:")
    print(add_numbers(5, "10"))  # Intentional error: adding int and str

if __name__ == "__main__":
    main()
