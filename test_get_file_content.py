from functions.get_file_content import get_file_content

def test():
    print("--- Testing Truncation (lorem.txt) ---")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(result)}")
    print(f"Ends with: {result[-50:]}")
    
    print("\n--- Testing main.py ---")
    print(get_file_content("calculator", "main.py"))

    print("\n--- Testing pkg/calculator.py ---")
    print(get_file_content("calculator", "pkg/calculator.py"))

    print("\n--- Testing /bin/cat (Should Error) ---")
    print(get_file_content("calculator", "/bin/cat"))

    print("\n--- Testing Missing File (Should Error) ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()