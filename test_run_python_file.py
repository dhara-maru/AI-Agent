from functions.run_python_file import run_python_file

def test():
    print("--- Test 1: main.py (No Args) ---")
    print(run_python_file("calculator", "main.py"))

    print("\n--- Test 2: main.py (With Args) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("\n--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))

    print("\n--- Test 4: Security Breach ---")
    print(run_python_file("calculator", "../main.py"))

    print("\n--- Test 5: Missing File ---")
    print(run_python_file("calculator", "nonexistent.py"))

    print("\n--- Test 6: Wrong Extension ---")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    test()